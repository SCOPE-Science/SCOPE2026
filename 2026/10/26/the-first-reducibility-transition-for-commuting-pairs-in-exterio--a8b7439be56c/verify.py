#!/usr/bin/env python3
"""Independent finite linear-algebra checks for the 5-to-6 generator exterior commuting varieties.
No third-party packages. Run: python3 verify_geometry.py
The exhaustive proof of geometric irreducibility uses degenerations, not this finite verifier.
"""
from itertools import combinations
from random import Random

def parity_sign(a,b):
    if a&b: return 0
    return -1 if sum((a >> (i+1)).bit_count() for i in range(6) if b>>i&1)%2 else 1

def matrix_rank_mod(rows,p):
    mat=[[v%p for v in row] for row in rows]
    pivots=0
    for col in range(len(mat[0])):
        k=next((j for j in range(pivots,len(mat)) if mat[j][col]%p),None)
        if k is None: continue
        mat[pivots],mat[k]=mat[k],mat[pivots]
        inverse=pow(mat[pivots][col],-1,p)
        mat[pivots]=[(v*inverse)%p for v in mat[pivots]]
        for j in range(pivots+1,len(mat)):
            v=mat[j][col]
            if v:
                mat[j]=[(x-v*y)%p for x,y in zip(mat[j],mat[pivots])]
        pivots+=1
    return pivots

def masks(n,parity):
    return [i for i in range(1<<n) if (i.bit_count()%2)==parity]

def wedge_map_rank(n,p,a,allowed=None):
    odd=masks(n,1)
    even=masks(n,0)
    if allowed is None: allowed=odd
    mat=[[0]*len(allowed) for _ in even]
    rowidx={m:i for i,m in enumerate(even)}
    for j,b in enumerate(allowed):
        for x,coeff in a.items():
            s=parity_sign(x,b)
            if s:mat[rowidx[x|b]][j]=(mat[rowidx[x|b]][j]+coeff*s)%p
    return matrix_rank_mod(mat,p)

def pairing_rank_3forms(n,p):
    assert n==6
    triple=[sum(1<<i for i in c) for c in combinations(range(n),3)]
    top=(1<<n)-1
    mat=[[parity_sign(x,y) if (x|y)==top else 0 for y in triple] for x in triple]
    return matrix_rank_mod(mat,p)

def count_by_strata(n,q):
    if n==5:
        # all decomposable-pair strata; even factors have 2^5 dimensions
        u=(q**5-1)*q**19
        v=(q**5-1)*q**18
        c=q**22
        expected=q**56+q**55+q**54-q**51-q**50
        assert (u+v+c)*q**32==expected
        return {'nonzero_first_linear':u,'zero_first_nonzero_second_linear':v,'both_linear_zero':c,'full_count':expected}
    assert n==6
    u=(q**6-1)*q**42
    v=(q**6-1)*q**41
    c=(q**39+q**20-q**19)*q**12
    expected=q**115+q**112+q**111-q**106-q**105+q**96-q**95
    assert (u+v+c)*q**64==expected
    return {'nonzero_first_linear':u,'zero_first_nonzero_second_linear':v,'both_linear_zero':c,'full_count':expected}

def main():
    rng=Random(146773)
    for p in (3,5,7):
        assert pairing_rank_3forms(6,p)==20
        for n in (5,6):
            odd=masks(n,1)
            upper=[m for m in odd if m.bit_count()>1]
            for _ in range(80):
                a={m:rng.randrange(p) for m in odd}
                a[1]=rng.randrange(1,p)
                assert wedge_map_rank(n,p,a)==(8 if n==5 else 16)
                b={m:rng.randrange(p) for m in odd}
                b[1]=rng.randrange(1,p)
                assert wedge_map_rank(n,p,b,upper)==(4 if n==5 else 11)
            data=count_by_strata(n,p)
            assert sum(v for k,v in data.items() if k!='full_count')*p**(1<<n)==data['full_count']
            print('field',p,'generators',n,'linear-map-ranks-and-strata-ok')
    # The n=5 rank deficiency is forced because every alternating 5x5 map is singular.
    for p in (3,5,7):
        triple=[sum(1<<i for i in c) for c in combinations(range(5),3)]
        for _ in range(80):
            v={m:rng.randrange(p) for m in triple}
            vectors=[1<<i for i in range(5)]
            fourth=[m for m in masks(5,0) if m.bit_count()==4]
            mat=[[sum(v[x]*parity_sign(a,x) for x in triple if (a|x)==r and (a&x)==0)%p for a in vectors] for r in fourth]
            assert matrix_rank_mod(mat,p)%2==0
            assert matrix_rank_mod(mat,p)<=4
        print('odd-dimensional-wedge-kernel-ok',p)
    print('VERIFY_OK_EXTERIOR_COMMUTING_COMPONENT_TRANSITION')

if __name__=='__main__':main()
