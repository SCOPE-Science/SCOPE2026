#!/usr/bin/env python3
"""Independent finite checks for one-way directed-cycle ladder multipath complexes.

The direct enumerator tests degree restrictions and acyclicity from the digraph.
The separate local model tests only pairwise conflicts and two forbidden rims.
Mod-two homology checks small cases; the all-length integral theorem has a
separate topological proof and is not inferred from these finite examples.
"""
from math import gcd

def direct_faces(n, k, phi):
    assert n >= 3 and gcd(n,k) == 1 and sorted(phi)==list(range(n))
    edges = ([(j,(j+1)%n) for j in range(n)]
           + [(n+j,n+(j+k)%n) for j in range(n)]
           + [(j,n+phi[j]) for j in range(n)])
    ans = set()
    for mask in range(1 << (3*n)):
        indeg=[0]*(2*n); outdeg=[0]*(2*n)
        nxt=[-1]*(2*n)
        good=True
        for j,(u,v) in enumerate(edges):
            if mask >> j & 1:
                indeg[v]+=1; outdeg[u]+=1; nxt[u]=v
                if indeg[v] > 1 or outdeg[u] > 1:
                    good=False; break
        if not good: continue
        # Kahn's directed-cycle test, independent of the rim model.
        queue=[v for v in range(2*n) if indeg[v]==0]
        seen=0
        while queue:
            u=queue.pop();seen+=1
            v=nxt[u]
            if v != -1:
                indeg[v]-=1
                if indeg[v] == 0: queue.append(v)
        if seen == 2*n:
            ans.add(mask)
    return ans

def model_faces(n,k,phi):
    ans=set()
    for mask in range(1<<(3*n)):
        if mask & ((1<<n)-1)==((1<<n)-1):continue
        if (mask>>n)&((1<<n)-1)==((1<<n)-1):continue
        for j in range(n):
            if mask>>(2*n+j)&1:
                o=bool(mask>>j&1)
                incoming_i=(phi[j]-k)%n
                i=bool(mask>>(n+incoming_i)&1)
                if o or i:break
        else:
            ans.add(mask)
    return ans

def mod2_homology(faces):
    bydim={}
    for mask in faces:
        bydim.setdefault(mask.bit_count()-1,[]).append(mask)
    lookup={d:{m:i for i,m in enumerate(ms)} for d,ms in bydim.items()}
    ranks={}
    for d in range(max(bydim)+1):
        basis={}
        for mask in bydim[d]:
            column=1 if d==0 else 0
            if d>0:
                t=mask
                while t:
                    e=t&-t;t-=e
                    column^=1<<lookup[d-1][mask^e]
            while column:
                lead=column.bit_length()-1
                if lead not in basis:
                    basis[lead]=column;break
                column^=basis[lead]
        ranks[d]=len(basis)
    return {d:len(ms)-ranks.get(d,0)-ranks.get(d+1,0) for d,ms in bydim.items()
            if len(ms)-ranks.get(d,0)-ranks.get(d+1,0)}

if __name__=='__main__':
    cases=[(3,1,[0,1,2]),(4,1,[0,1,2,3]),(4,1,[2,0,3,1]),
           (5,1,[2,0,4,1,3]),(5,2,[0,1,2,3,4])]
    for n,k,phi in cases:
        direct=direct_faces(n,k,phi)
        local=model_faces(n,k,phi)
        assert direct==local,(n,k,phi,'model differs from directed paths')
        assert len(direct)==5**n-2**(n+1)+1
        betti=mod2_homology(direct)
        assert betti=={n-1:1,2*n-3:1},(n,k,phi,betti)
        print('n=%d k=%d phi=%s faces=%d F2_betti=%s' %
              (n,k,phi,len(direct),betti))
    print('FINITE_CHECKS_OK')
