#!/usr/bin/env python3
"""Independent normal-form and orbit checks for finite modal relations."""
from itertools import permutations, product
from math import factorial

def preorders(n):
    pairs = [(i,j) for i in range(n) for j in range(n) if i!=j]
    for code in range(1 << len(pairs)):
        rows = [1<<i for i in range(n)]
        for k,(i,j) in enumerate(pairs):
            if code & (1<<k): rows[i]|=1<<j
        if all((not (rows[i] & (1<<j))) or (rows[j]&~rows[i])==0
               for i in range(n) for j in range(n)):
            yield tuple(rows)

def downsets(rows):
    n=len(rows)
    return [s for s in range(1<<n) if all(
        (not (s & (1<<j))) or (not (rows[i] & (1<<j))) or (s & (1<<i))
        for i in range(n) for j in range(n))]

def top(rows):
    t=(1<<len(rows))-1
    for r in rows: t &=r
    return t

def fixed_stats(n, perm):
    a=b=c=d=0
    for rows in preorders(n):
        if any(bool(rows[i]&(1<<j)) != bool(rows[perm[i]]&(1<<perm[j]))
               for i in range(n) for j in range(n)):
            continue
        a+=1
        t=bool(top(rows)); b+=t
        ds=sum(all(bool(s&(1<<i))==bool(s&(1<<perm[i])) for i in range(n))
               for s in downsets(rows))
        c+=ds
        if t:d+=ds
    return (a,b,c,d)

def count_from_stats(x,y):
    a,b,c,d=x; A,B,C,D=y
    return a*A + (c-a)*B + (C-A)*b + (d-b)*(D-B)

def relation(p,q,P,Q,S,T):
    n=p+q
    r=[0]*n
    for i in range(p):
        r[i]=P[i]|(((1<<q)-1 & top(Q))<<p if S&(1<<i) else 0)
    for j in range(q):
        r[p+j]=(Q[j]<<p)|(top(P) if T&(1<<j) else 0)
    return tuple(r)

def valid(p,q,rows):
    n=p+q
    if any(not(rows[i]&(1<<i)) for i in range(n)):return False
    if any((rows[i]&(1<<j)) and (rows[j]&~rows[i])
           for i in range(n) for j in range(n)):
        return False
    for l in range(p):
        for u in range(p,n):
            for v in range(n):
                if (rows[l]&(1<<v)) and not any(
                    (rows[u]&(1<<w)) and (v==w or (v<p and w>=p))
                    for w in range(n)):
                    return False
                if (rows[u]&(1<<v)) and not any(
                    (rows[l]&(1<<w)) and (v==w or (w<p and v>=p))
                    for w in range(n)):
                    return False
    return True

def structures(p,q):
    for P in preorders(p):
        for Q in preorders(q):
            ss=downsets(P) if top(Q) else [0]
            ts=downsets(Q) if top(P) else [0]
            for S,T in product(ss,ts):
                yield relation(p,q,P,Q,S,T)

def relabel(rows, p, q, sig, tau):
    n=p+q;perm=tuple(sig)+tuple(p+j for j in tau)
    out=[0]*n
    for i in range(n):
        for j in range(n):
            if rows[i]&(1<<j):out[perm[i]]|=1<<perm[j]
    return tuple(out)

def orbits(p,q):
    permsA=list(permutations(range(p)))
    permsB=list(permutations(range(q)))
    rels=set(structures(p,q))
    canon=set()
    for r in rels:
        canon.add(min(relabel(r,p,q,s,t) for s in permsA for t in permsB))
    return len(rels),len(canon)

if __name__=='__main__':
    ids={n:fixed_stats(n,tuple(range(n))) for n in range(1,5)}
    assert ids=={1:(1,1,2,2),2:(4,3,12,8),3:(29,16,130,59),4:(355,145,2338,746)},ids
    for p,q,nwant in [(1,1,4),(1,2,20),(2,2,89),(2,3,762),(3,2,762),(3,3,5922),(2,4,11534)]:
        got=count_from_stats(ids[p],ids[q]); assert got==nwant,(p,q,got)
        if max(p,q)<=3:
            rels=list(structures(p,q))
            assert len(rels)==len(set(rels))==got
            assert all(valid(p,q,r) for r in rels)
    for p,q in [(2,2),(2,3),(3,2)]:
        l,u=orbits(p,q)
        total=0
        for sig in permutations(range(p)):
            for tau in permutations(range(q)):
                total+=count_from_stats(fixed_stats(p,sig),fixed_stats(q,tau))
        assert total%(factorial(p)*factorial(q))==0
        assert (l,u)==(count_from_stats(ids[p],ids[q]),total//(factorial(p)*factorial(q)))
        print('labelled/unlabelled',p,q,l,u)
    p,q=3,3
    total=sum(count_from_stats(fixed_stats(p,s),fixed_stats(q,t))
              for s in permutations(range(p)) for t in permutations(range(q)))
    assert total//(factorial(p)*factorial(q))==452
    assert len(set(structures(p,q)))==5922
    print("labelled/unlabelled",p,q,5922,452)
    print('VERIFY_OK')
