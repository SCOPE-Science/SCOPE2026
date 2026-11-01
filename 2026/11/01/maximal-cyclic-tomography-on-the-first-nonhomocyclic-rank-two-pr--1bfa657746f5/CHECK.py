#!/usr/bin/env python3
"""Exact integer verification for maximal cyclic coset-sum tomography on C_(p^2) x C_p.
Requires only Python 3; optional NumPy not required. This is finite corroboration.
"""
from collections import Counter

def generated(g, p):
    a,b=g
    return frozenset(((i*a)%(p*p),(i*b)%p) for i in range(p*p))

def maximal_subgroups(p):
    G=[(x,y) for x in range(p*p) for y in range(p)]
    cyc={generated(g,p) for g in G if g!=(0,0)}
    return sorted((H for H in cyc if not any(H<K for K in cyc)), key=lambda H:(-len(H),tuple(sorted(H))))

def gram_from_cosets(p,hs):
    G=[(x,y) for x in range(p*p) for y in range(p)]
    ids={g:i for i,g in enumerate(G)}
    N=len(G)
    M=[[0]*N for _ in range(N)]
    row_count=0
    for H in hs:
        remain=set(G)
        while remain:
            g=min(remain)
            coset=sorted((((g[0]+h[0])%(p*p),(g[1]+h[1])%p) for h in H))
            assert set(coset)<=remain
            remain.difference_update(coset)
            j=[ids[x] for x in coset]
            for a in j:
                for b in j: M[a][b]+=1
            row_count+=1
    return G,M,row_count

def check(p):
    hs=maximal_subgroups(p)
    assert len(hs)==2*p
    group_a=[generated((1,t),p) for t in range(p)]
    group_b=[generated((p*s,1),p) for s in range(p)]
    assert set(hs)==set(group_a+group_b)
    G,M,rows=gram_from_cosets(p,hs)
    assert rows==p**3+p**2
    eigen_counts=Counter()
    annihilator_counts=Counter()
    for k in range(p*p):
        for l in range(p):
            eig=sum(len(H) for H in hs if all((k*x + p*l*y)%(p*p)==0 for x,y in H))
            eigen_counts[eig]+=1
            annihilator_counts[(k,l)]=eig
            # Fourier diagonalization checked entirely by root-free cyclotomic congruence:
            # M is a convolution kernel, and each subgroup indicator contributes its order
            # iff the character is trivial on the subgroup.
            if k==l==0: assert eig==p**3+p**2
            elif k%p: assert eig==p
            else: assert eig==p*p
    assert eigen_counts==Counter({p:p*p*(p-1),p*p:p*p-1,p**3+p**2:1})
    assert all(M[i][i]==len(hs) for i in range(len(G)))
    assert all(M[i][j]==M[j][i] for i in range(len(G)) for j in range(len(G)))
    # Confirm each of the 2p directions has an exclusive nonconstant Fourier witness.
    for H in hs:
        assert any(sum(1 for J in hs if all((k*x+p*l*y)%(p*p)==0 for x,y in J))==1
                   and all((k*x+p*l*y)%(p*p)==0 for x,y in H)
                   for k in range(p*p) for l in range(p) if k or l)
    # Exact convolution Gram entries checked from subgroup membership, independently
    # of coset construction.
    for i,g in enumerate(G):
        for j,h in enumerate(G):
            delta=((h[0]-g[0])%(p*p),(h[1]-g[1])%p)
            assert M[i][j]==sum(delta in H for H in hs)
    # Normalized-direction weights: |H|^{-1/2} gives eigenvalues
    # 1 on each uniquely-observed nonconstant frequency and p on the remaining p-1.
    weighted_counts=Counter()
    for k in range(p*p):
        for l in range(p):
            eigen=sum(1 for H in hs if all((k*x+p*l*y)%(p*p)==0 for x,y in H))
            weighted_counts[eigen]+=1
    assert weighted_counts==Counter({1:p**3-p,p:p-1,2*p:1})
    print('PASS p=',p,'size=',p**3,'rows=',rows,'maximal_directions=',len(hs),
          'integer_eigenvalues=',dict(sorted(eigen_counts.items())),
          'unit_direction_eigenvalues=',dict(sorted(weighted_counts.items())))

if __name__=='__main__':
    for prime in [2,3,5,7]:check(prime)
    print('VERIFY_OK four_primes=PASS direct_coset_Gram=PASS exact_abelian_Fourier=PASS witnesses=PASS weighted_spectrum=PASS')
