#!/usr/bin/env python3
"""Exact finite sanity checks of one-anchor refinement on subspace-disjointness graphs.
Independent matrix enumeration using reduced-row-echelon pivot representatives; prime fields only.
"""
import itertools
from collections import Counter
from math import prod

def qbinom(n, r, q):
    if r < 0 or r > n: return 0
    a,b=1,1
    for i in range(r): a*=q**(n-i)-1; b*=q**(r-i)-1
    return a//b

def vectorspace_subspaces(n, k, p):
    for pivots in itertools.combinations(range(n),k):
        positions=[(i,j) for i,pi in enumerate(pivots) for j in range(pi+1,n) if j not in pivots]
        for entries in itertools.product(range(p),repeat=len(positions)):
            rows=[[0]*n for _ in range(k)]
            for i,j in enumerate(pivots):rows[i][j]=1
            for (i,j),v in zip(positions,entries):rows[i][j]=v
            mask=0
            for coefs in itertools.product(range(p),repeat=k):
                if not any(coefs): continue
                vec=[sum(coefs[i]*rows[i][j] for i in range(k))%p for j in range(n)]
                idx=sum(z*p**j for j,z in enumerate(vec))
                mask|=1<<idx
            yield mask

def refinement(classes,neighbors):
    keys=[]
    for i,col in enumerate(classes):
        counts=Counter(classes[j] for j in neighbors[i])
        keys.append((col,tuple(sorted(counts.items()))))
    dictionary={key:index for index,key in enumerate(sorted(set(keys)))}
    return tuple(dictionary[key] for key in keys)

def test(p,k):
    n=2*k
    subspaces=list(vectorspace_subspaces(n,k,p))
    assert len(subspaces)==qbinom(n,k,p),('rref',p,k,len(subspaces))
    anchor=next(mask for mask in subspaces if all((mask>>p**j)&1 for j in range(k)))
    aid=subspaces.index(anchor)
    svalues=[]
    for mask in subspaces:
        overlap=(mask&anchor).bit_count()+1
        s=0
        while p**s<overlap:s+=1
        assert p**s==overlap
        svalues.append(s)
    adj=[[] for _ in subspaces]
    for i,u in enumerate(subspaces):
        adj[i]=[j for j,v in enumerate(subspaces) if not (u&v) and i!=j]
    degree=p**(k*k)
    assert all(len(N)==degree for N in adj)
    initial=(tuple(1 if j==aid else 0 for j in range(len(subspaces))))
    after1=refinement(initial,adj)
    after2=refinement(after1,adj)
    assert len(set(after2))==k+1,(p,k,len(set(after2)))
    assert all((after2[i]==after2[j])==(svalues[i]==svalues[j]) for i in range(len(subspaces)) for j in range(len(subspaces)))
    assert len(set(after1))==3,(p,k)
    if k>=3:assert len(set(after1))<k+1
    orbit_counts=Counter(svalues)
    cn=Counter()
    neigh_anchor=set(adj[aid])
    for i,s in enumerate(svalues):
        z=len(neigh_anchor.intersection(adj[i]))
        want=p**(k*k-(k-s)*(k-s+1)//2)*prod(p**j-1 for j in range(1,k-s+1))
        assert z==want,(p,k,s,z,want)
        cn[s]=z
    for s in range(k+1):
        expected=p**((k-s)**2)*qbinom(k,s,p)**2
        assert orbit_counts[s]==expected,(p,k,s,orbit_counts[s],expected)
    assert sum(orbit_counts.values())==len(subspaces)
    return f'p={p} k={k} vertices={len(subspaces)} degree={degree} round1={len(set(after1))} round2={len(set(after2))} common_neighbors={[cn[i] for i in range(k+1)]} orbit_sizes={[orbit_counts[i] for i in range(k+1)]} OK'

if __name__=='__main__':
    for p,k in [(2,2),(3,2),(2,3)]: print(test(p,k))
    print('ALL_BRUTEFORCE_CHECKS_OK')
