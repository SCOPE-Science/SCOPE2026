#!/usr/bin/env python3
"""Exact exhaustive verifier of a five-vertex UST degree-covariance boundary.
Standard-library only. No numerical probabilities or random samples.
"""
from itertools import combinations, permutations
from fractions import Fraction


def connected(n, edges):
    seen={0}; todo=[0]
    nbr=[set() for _ in range(n)]
    for u,v in edges: nbr[u].add(v); nbr[v].add(u)
    while todo:
        for v in nbr[todo.pop()]-seen: seen.add(v); todo.append(v)
    return len(seen)==n


def tree(n, edges):
    return len(edges)==n-1 and connected(n,edges)


def covariances(n,edges):
    ts=[t for t in combinations(edges,n-1) if tree(n,t)]
    assert ts
    degs=[[sum(u==v or w==v for u,w in t) for v in range(n)] for t in ts]
    N=len(ts)
    sums=[sum(d[i] for d in degs) for i in range(n)]
    return N,{(i,j):Fraction(sum(d[i]*d[j] for d in degs)*N -sums[i]*sums[j],N*N)
              for i in range(n) for j in range(i+1,n)}


def canonical(n,edges):
    pairs=list(combinations(range(n),2)); e={tuple(sorted(x)) for x in edges}
    return min(''.join('1' if tuple(sorted((p[i],p[j]))) in e else '0' for i,j in pairs)
               for p in permutations(range(n)))


def classify():
    witnesses=[]
    for n in range(2,6):
        pairs=list(combinations(range(n),2)); positives={}; nconn=0; alltypes=set()
        for mask in range(1<<len(pairs)):
            edges=[e for i,e in enumerate(pairs) if mask>>i&1]
            if len(edges)<n-1 or not connected(n,edges):continue
            nconn+=1;signature=canonical(n,edges);alltypes.add(signature);N,cov=covariances(n,edges)
            if any(z>0 for z in cov.values()):
                signature=canonical(n,edges)
                positives.setdefault(signature,(edges,N,{q:v for q,v in cov.items() if v>0}))
        print('ORDER',n,'CONNECTED_LABELED',nconn,'CONNECTED_ISOMORPHISM_CLASSES',len(alltypes),'POSITIVE_ISOMORPHISM_CLASSES',len(positives))
        if n<5:assert not positives
        if n==5:
            assert len(alltypes)==21 and len(positives)==2
            cycle=[(i,(i+1)%5) for i in range(5)]
            assert set(positives)=={canonical(5,cycle),canonical(5,cycle+[(0,2)])}
            for sig,(edges,N,pp) in sorted(positives.items()):
                print('WITNESS',len(edges),'edges','TREES',N,'POSITIVE_PAIRS',len(pp),'COVARIANCES',sorted(set(pp.values())))
                witnesses.append((len(edges),N,len(pp),set(pp.values())))
    assert sorted(witnesses,key=lambda x:x[0])==[(5,5,5,{Fraction(1,25)}),(6,11,2,{Fraction(5,121)})]


def unicyclic_check():
    # Unique-cycle graphs obtained by adjoining arbitrary pendant paths to C_l.
    for ell in range(3,12):
        base=[(i,(i+1)%ell) for i in range(ell)]
        for arms in ((),(1,),(1,2)):
            edges=base.copy(); n=ell
            for k,arm in enumerate(arms):
                previous=k%ell
                for _ in range(arm):
                    edges.append((previous,n));previous=n;n+=1
            count,cov=covariances(n,edges)
            assert count==ell
            for (u,v),c in cov.items():
                expected=(Fraction(ell-4,ell*ell) if ((u+1)%ell==v or (v+1)%ell==u) else Fraction(-4,ell*ell)) if u<ell and v<ell else Fraction(0)
                assert c==expected,(ell,arms,u,v,c,expected)
        print('UNICYCLE',ell,'PASS')


if __name__=='__main__':
    classify();unicyclic_check();print('VERIFY_OK')
