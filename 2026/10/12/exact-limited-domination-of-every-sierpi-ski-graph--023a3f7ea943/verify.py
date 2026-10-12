#!/usr/bin/env python3
"""Independent finite tests of the Sierpinski k-limited domination formula.
No external dependencies. The analytic proof is in RESULT.md.
"""
from itertools import product

def vertices(n,m):
    return list(product(range(m),repeat=n))

def adjacency(n,m):
    vs=vertices(n,m); ix={v:i for i,v in enumerate(vs)}
    adj=[set() for _ in vs]
    for i,u in enumerate(vs):
        for j in range(i+1,len(vs)):
            v=vs[j]
            h=next((h for h in range(n) if u[h]!=v[h]), None)
            if h is None:continue
            if all(u[t]==v[t] for t in range(h)) and all(u[t]==v[h] and v[t]==u[h] for t in range(h+1,n)):
                adj[i].add(j);adj[j].add(i)
    return vs,adj

def rel(m,r):
    # Symmetric r-regular relation with constant diagonal.
    d= int(m%2==1 and r%2==1)
    q=r-d
    R=set()
    for a in range(m):
        if d:R.add((a,a))
        for t in range(1,q//2+1):
            R.add((a,(a+t)%m));R.add((a,(a-t)%m))
        if (m%2==0 and q%2==1):R.add((a,(a+m//2)%m))
    assert all(sum((a,b) in R for b in range(m))==r for a in range(m))
    assert all(((a,b) in R)==((b,a) in R) for a in range(m) for b in range(m))
    assert len({(a,a) in R for a in range(m)})==1
    return R

def feasible(mask,adj,k):
    n=len(adj)
    for i in range(n):
        out=sum(not(mask>>j&1) for j in adj[i])
        if mask>>i&1:
            if out>k:return False
        elif not any(mask>>j&1 for j in adj[i]):return False
    return True

def check():
    constructions=0; optimum_exhaustive=0; brute_subsets=0; cycles=0
    for m in range(2,9):
        for k in range(1,m):
            r=m-k; R=rel(m,r)
            for n in range(1,5):
                if m**n>125:continue
                vs,adj=adjacency(n,m)
                if n==1:sel=[i for i in range(m) if i<r]
                else:sel=[i for i,u in enumerate(vs) if u[-2:] in R]
                assert len(sel)==r*m**(n-1),(n,m,k,len(sel))
                mask=sum(1<<i for i in sel)
                assert feasible(mask,adj,k),(n,m,k)
                # Check every edge crossing distinct base cliques is monochromatic.
                if n>=2:
                    for i in sel:
                        for j in adj[i]:
                            if vs[i][:-1]!=vs[j][:-1]:
                                assert j in sel,(n,m,k,vs[i],vs[j])
                constructions+=1
                if m**n<=16:
                    best=m**n+1
                    for mask2 in range(1<<(m**n)):
                        if mask2.bit_count()>best:continue
                        brute_subsets+=1
                        if feasible(mask2,adj,k):best=min(best,mask2.bit_count())
                    assert best==r*m**(n-1),(n,m,k,best)
                    optimum_exhaustive+=1
    print('ALL CHECKS PASSED')
    print(f'construction_parameter_profiles={constructions}; exhaustive_minimum_profiles={optimum_exhaustive}; tested_candidate_subsets={brute_subsets}')

if __name__=='__main__':check()
