#!/usr/bin/env python3
"""Direct finite checks for extremal cliques of two-symbol composition read graphs.
No external dependencies. This finite test complements, but does not replace, proof.
"""
from itertools import combinations, product
from collections import Counter


def read(w):
    # Boundary symbol -1 is outside the alphabet; distances are unchanged by zero padding.
    v=(-1,)+w+(-1,)
    return tuple(tuple(sorted((v[i],v[i+1]))) for i in range(len(v)-1))


def maximal_cliques(neigh):
    def bronk(R,P,X):
        if not P and not X:
            yield frozenset(R)
            return
        pivot=max(P|X,key=lambda v:len(P&neigh[v])) if P|X else None
        for v in list(P - (neigh[pivot] if pivot is not None else set())):
            yield from bronk(R|{v}, P&neigh[v], X&neigh[v])
            P.remove(v)
            X.add(v)
    yield from bronk(set(),set(neigh),set())


def predicted(q,n):
    words=tuple(product(range(q),repeat=n))
    qstars=set()
    for i in range(n):
        for outer in product(range(q),repeat=n-1):
            qstars.add(frozenset(outer[:i]+(a,)+outer[i:] for a in range(q)))
    alt=set()
    if n>=2:
        for a in range(q):
            for b in range(q):
                if a==b:continue
                z=tuple(a if i%2==0 else b for i in range(n+1))
                alt.add(frozenset(z[:i]+z[i+1:] for i in range(n+1)))
    else:
        alt=set()
    m=max(q,n+1)
    if n==1:
        return {frozenset(words)}
    return ({c for c in qstars if len(c)==m} | {c for c in alt if len(c)==m})


def inspect(q,n):
    W=tuple(product(range(q),repeat=n)); RD=tuple(read(x) for x in W)
    neigh={i:set() for i in range(len(W))}
    for i in range(len(W)):
        for j in range(i+1,len(W)):
            rdist=sum(a!=b for a,b in zip(RD[i],RD[j]))
            if rdist==2:
                neigh[i].add(j);neigh[j].add(i)
            elif rdist==1:
                raise AssertionError('Distinct inputs at read distance one')
    mx=set(); m=0; nummaximal=0
    for c in maximal_cliques(neigh):
        nummaximal+=1
        if len(c)>m:
            m=len(c);mx=set()
        if len(c)==m:
            mx.add(frozenset(W[i] for i in c))
    p=predicted(q,n)
    assert m==max(q,n+1),(q,n,m)
    assert mx==p,(q,n,m,len(mx),len(p),next(iter(mx-p),None),next(iter(p-mx),None))
    return len(W),sum(len(v) for v in neigh.values())//2,nummaximal,m,len(mx)


def main():
    families=[(q,n) for q,maxn in [(2,8),(3,5),(4,4),(5,3)] for n in range(1,maxn+1)]
    checked=[]
    for q,n in families:
        r=inspect(q,n);checked.append((q,n,r))
        print('PASS',q,n,'vertices',r[0],'edges',r[1],'maximal_cliques',r[2],'omega',r[3],'max_count',r[4],flush=True)
    print('VERIFY_OK families=%d vertices=%d edges=%d maximum_cliques=%d' % (len(checked),sum(x[2][0] for x in checked),sum(x[2][1] for x in checked),sum(x[2][4] for x in checked)))
if __name__=='__main__':main()
