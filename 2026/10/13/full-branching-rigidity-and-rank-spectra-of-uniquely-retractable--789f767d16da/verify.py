#!/usr/bin/env python3
"""Independent finite checks of rigidity and rank spectra of ultrametric retractions."""
from itertools import product
from collections import Counter
from functools import lru_cache

# A canonical unordered branching hierarchy: a leaf is (), and every nonleaf
# is an ordered tuple of two or more canonical children.
@lru_cache(None)
def shape_size(tree):
    return 1 if not tree else sum(shape_size(c) for c in tree)

@lru_cache(None)
def shapes(n):
    if n == 1:
        return ((),)
    pool = [t for j in range(1, n) for t in shapes(j)]
    pool.sort(key=lambda t: (shape_size(t), repr(t)))
    ans = set()
    def rec(start, children, weight):
        if weight == n:
            if len(children) >= 2:
                ans.add(tuple(children))
            return
        for j in range(start, len(pool)):
            s = shape_size(pool[j])
            if weight + s <= n:
                rec(j, children + [pool[j]], weight + s)
    rec(0, [], 0)
    return tuple(sorted(ans, key=repr))

def build(tree):
    """Return leaf count, distance matrix, and all balls with child balls."""
    balls = []
    def visit(t, left):
        if not t:
            return {left}, 0
        children=[]
        k=left
        hs=[]
        for ch in t:
            leaves,h=visit(ch,k)
            children.append(leaves)
            hs.append(h)
            k+=len(leaves)
        level=1+max(hs)
        b=frozenset().union(*children)
        balls.append((b, tuple(map(frozenset,children)),level))
        return b,level
    leaves,height=visit(tree,0)
    n=len(leaves)
    dist=[[0]*n for _ in range(n)]
    for b,chs,h in balls:
        for a in range(len(chs)):
            for c in range(a+1,len(chs)):
                for x in chs[a]:
                    for y in chs[c]:
                        dist[x][y]=dist[y][x]=h
    assert all(dist[i][j]>0 for i in range(n) for j in range(i+1,n))
    assert all(dist[i][j]<=max(dist[i][k],dist[k][j]) for i in range(n) for j in range(n) for k in range(n))
    return n,dist,balls

def unique_criterion(n,balls,yset):
    return all(not (len(b & yset)>=2 and any(not(ch & yset) for ch in chs)) for b,chs,_ in balls)

def poly(tree):
    if not tree: return (0,1)
    acc=[1]
    for ch in tree:
        pc=poly(ch)
        nxt=[0]*(len(acc)+len(pc)-1)
        for i,a in enumerate(acc):
            for j,b in enumerate(pc):
                nxt[i+j]+=a*b
        acc=nxt
    if len(acc)<2: acc += [0]*(2-len(acc))
    acc[1]+=shape_size(tree)
    return tuple(acc)

def brute(tree):
    n,d,balls=build(tree)
    byimage=Counter(); endomorphisms=0
    for f in product(range(n), repeat=n):
        if any(d[f[i]][f[j]]>d[i][j] for i in range(n) for j in range(i+1,n)):
            continue
        endomorphisms+=1
        if all(f[f[i]]==f[i] for i in range(n)):
            mask=sum(1<<x for x in set(f))
            byimage[mask]+=1
    expected=Counter()
    for mask in range(1,1<<n):
        yy={i for i in range(n) if (mask>>i)&1}
        expected[len(yy)]+=int(unique_criterion(n,balls,yy))
        assert (byimage[mask]==1)==unique_criterion(n,balls,yy),(tree,mask,byimage[mask])
        assert byimage[mask]>=1,(tree,mask)
    p=poly(tree)
    assert expected==Counter({k:v for k,v in enumerate(p) if v}),(tree,expected,p)
    assert sum(byimage.values())<=endomorphisms
    return endomorphisms,sum(byimage.values()),sum(v==1 for v in byimage.values()),2**n-1

def regular(q,d):
    if d==0:return ()
    return tuple(regular(q,d-1) for _ in range(q))

def main():
    instances=0; subset_checks=0; idempotents=0; maps=0
    for n in range(1,6):
        ss=shapes(n)
        for t in ss:
            endo,idem,unique,subs=brute(t)
            instances+=1; subset_checks+=subs; idempotents+=idem; maps+=n**n
        print('SHAPES',n,len(ss))
    # Independently enumerate all maps on a six-point balanced hierarchy.
    for t in (regular(2,2), regular(3,1), ((),(),((),(),(),()))):
        n,d,balls=build(t)
        endo,idem,unique,subs=brute(t)
        instances+=1;subset_checks+=subs;idempotents+=idem;maps+=n**n
    for q in (2,3,4,5):
        u=1
        for d in range(1,5):
            t=regular(q,d)
            p=poly(t)
            u=q**d+u**q
            assert sum(p)==u
            assert {i for i,a in enumerate(p) if a}=={1+(q-1)*j for j in range((q**d-1)//(q-1)+1)}
            if d<=2 and q<=3:print('REGULAR',q,d,list(enumerate(p)),u)
    print(f'VERIFY_OK {instances} finite ultrametric shapes; {subset_checks} image-subset tests; {maps} total map candidates; {idempotents} idempotent maps; regular rank recurrences q=2..5,d=1..4')
if __name__=='__main__':main()
