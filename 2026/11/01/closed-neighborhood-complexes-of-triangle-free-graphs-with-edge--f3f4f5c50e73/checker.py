#!/usr/bin/env python3
"""Independent finite checks of the closed-neighborhood collapse theorem.

Only tests a finite selection; the general result requires the written proof.
"""
from itertools import combinations
import random


def squares(V,E):
    E={frozenset(x) for x in E}
    out=[]
    for p in combinations(V,4):
        for cyc in ((p[0],p[1],p[2],p[3]),(p[0],p[1],p[3],p[2]),(p[0],p[2],p[1],p[3])):
            ed={frozenset((cyc[i],cyc[(i+1)%4])) for i in range(4)}
            if ed<=E:out.append((frozenset(p),ed))
    return out


def valid(V,E):
    E={frozenset(t) for t in E}
    N={u:set() for u in V}
    for x in E:
        a,b=tuple(x);N[a].add(b);N[b].add(a)
    if any(a in N[b] for u in V for a,b in combinations(N[u],2)):return False
    sq=squares(V,E)
    if any(x[1]&y[1] for x,y in combinations(sq,2)):return False
    seen={V[0]};stack=[V[0]]
    while stack:
        u=stack.pop()
        for w in N[u]-seen:seen.add(w);stack.append(w)
    return len(seen)==len(V)


def closure(maxfaces):
    faces=set()
    for b in maxfaces:
        b=tuple(b)
        for j in range(1,len(b)+1):
            faces.update(frozenset(t) for t in combinations(b,j))
    return faces


def rank_f2(rows, ncols):
    piv={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;break
    return len(piv)


def bettis(F):
    bydim={}
    for f in F:bydim.setdefault(len(f)-1,[]).append(f)
    maxdim=max(bydim)
    for i in bydim:bydim[i].sort(key=lambda f:tuple(sorted(f)))
    ranks={}
    for d in range(1,maxdim+1):
        ids={x:i for i,x in enumerate(bydim[d-1])}
        rows=[]
        for t in bydim.get(d,[]):
            mask=0
            for v in t:mask ^=1<<ids[t-{v}]
            rows.append(mask)
        ranks[d]=rank_f2(rows,len(ids))
    result={}
    for d in range(maxdim+1):
        b=len(bydim.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:b-=1
        if b:result[d]=b
    return result


def verify(V,E, homology=True):
    E={frozenset(x) for x in E}
    N={v:set() for v in V}
    for a,b in (tuple(x) for x in E):N[a].add(b);N[b].add(a)
    sq=squares(V,E)
    if not valid(V,E):return None
    K=closure(list(E)+[{v} for v in V]+[p-{u} for p,_ in sq for u in p])
    C=closure([N[v]|{v} for v in V]);old=len(C)
    removals=0
    for v in V:
        D={frozenset((a,b)) for p,ss in sq if v in p for a,b in combinations(N[v]&set(p),2) if frozenset((a,b)) not in ss}
        assert all(sum(a in d for d in D)<=1 for a in N[v])
        for h in range(len(N[v]),1,-1):
            for sub in combinations(sorted(N[v]),h):
                F=frozenset(sub)
                if F in D:continue
                top=F|{v}
                assert F in C and top in C,('missing face',V,E,v,F)
                # no extension above top, and exactly one immediate coface above F
                bigger=[t for t in C if F<t and len(t)==len(F)+1]
                assert bigger==[top],('not free',V,E,v,F,bigger)
                assert not any(top<t for t in C),('not maximal',V,E,v,F)
                C.remove(F);C.remove(top);removals+=1
    assert C==K,('not core', V,E,len(C),len(K),list(C-K)[:5],list(K-C)[:5])
    if homology:
        actual=bettis(K)
        want=({1:len(E)-len(V)+1-len(sq)} if len(E)-len(V)+1-len(sq)>0 else {})
        if sq:want[2]=len(sq)
        assert actual==want,('Betti',V,E,actual,want)
    return old,len(K),removals,len(sq)


def cycle(n,offset=0):return [(i+offset,(i+1)%n+offset) for i in range(n)]

def wedge_cycles(lengths):
    E=[];n=1
    for m in lengths:
        V=[0]+list(range(n,n+m-1));n+=m-1
        E.extend((V[i],V[(i+1)%m]) for i in range(m))
    return list(range(n)),E


def main():
    totals={'graphs':0,'faces':0,'collapse_pairs':0,'square_cases':0}
    def test(V,E):
        r=verify(V,E)
        if r:
            f,k,p,s=r
            totals['graphs']+=1;totals['faces']+=f;totals['collapse_pairs']+=p;totals['square_cases']+=s
    for n in range(1,12):
        test(list(range(n)),[(i,i+1) for i in range(n-1)])
    for n in range(4,13):test(list(range(n)),cycle(n))
    for lengths in [(4,4),(4,5),(4,6),(4,4,4),(5,4,5),(6,4,6),(4,4,5),(4,5,4,6)]:
        V,E=wedge_cycles(lengths);test(V,E)
    for n in range(3,7):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            E=[p for i,p in enumerate(pairs) if mask>>i&1]
            if valid(list(range(n)),E):test(list(range(n)),E)
    rng=random.Random(174)
    for n in (7,8,9):
        pairs=list(combinations(range(n),2))
        for _ in range(800):
            E=[p for p in pairs if rng.random()<.3]
            if valid(list(range(n)),E):test(list(range(n)),E)
    print('PASS:', totals, 'all facewise elementary collapses and independent mod-two Betti calculations')
if __name__=='__main__':main()
