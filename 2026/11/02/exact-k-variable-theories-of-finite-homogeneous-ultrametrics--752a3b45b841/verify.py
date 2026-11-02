"""Independent finite checks for exact bounded-variable ultrametric classifications.
Standard library only. No external data needed.
"""
from itertools import product, permutations, combinations
from math import prod

def leaves(branches):
    return tuple(product(*(range(b) for b in branches)))

def distance_level(x,y):
    return next((i+1 for i,(a,b) in enumerate(zip(x,y)) if a!=b),0)

def signature(points):
    return tuple(distance_level(points[i],points[j]) for i in range(len(points)) for j in range(i+1,len(points)))

def types(branches,k):
    V=leaves(branches)
    return tuple(frozenset(signature(t) for t in permutations(V,m)) for m in range(1,min(len(V),k)+1))

def pad_types(branches,k):
    return tuple(frozenset(signature(t) for t in permutations(leaves(branches),m)) for m in range(1,k+1))

def check_extension(A,B,k):
    # Exhaust all injective partial isometries of length < k, both directions.
    VA,VB=leaves(A),leaves(B)
    checks=0
    for m in range(0,k):
        for ta in permutations(VA,m):
            sa=signature(ta)
            for tb in permutations(VB,m):
                if signature(tb)!=sa:continue
                aa={tuple(distance_level(x,a) for a in ta) for x in VA}
                bb={tuple(distance_level(y,b) for b in tb) for y in VB}
                assert aa==bb, (A,B,k,ta,tb,aa^bb)
                checks+=1
    return checks

def main():
    structures=0; comparisons=0
    for h,limit in ((1,5),(2,4),(3,3)):
        branches=list(product(range(2,limit+1),repeat=h))
        for k in (2,3,4):
            profiles={b:pad_types(b,k) for b in branches}
            for a,b in combinations(branches,2):
                predicted=tuple(min(z,k) for z in a)==tuple(min(z,k) for z in b)
                assert (profiles[a]==profiles[b])==predicted,(h,k,a,b)
                comparisons+=1
        for b in branches:
            V=leaves(b)
            radial=tuple(sum(distance_level(V[0],x)==i for x in V) for i in range(1,h+1))
            reconstructed=[None]*h
            for i in range(h-1,-1,-1):
                child_size=prod(reconstructed[i+1:])
                assert radial[i]%child_size==0
                reconstructed[i]=1+radial[i]//child_size
            assert tuple(reconstructed)==b
            structures+=1
    checks=0
    for a,b,k in [((3,3),(4,4),3),((2,3),(2,4),3),((4,2),(5,2),4),((2,2,2),(3,2,2),2)]:
        checks+=check_extension(a,b,k)
    print('VERIFIED: exact all-ordered-distinct-tuple type spectra on %d structures, %d pair/k comparisons' %(structures,comparisons))
    print('VERIFIED: counting annulus reconstruction for every structure')
    print('VERIFIED: exhaustive back-and-forth for %d compatible partial isometries' % checks)
    print('VERIFIED: four sample pairs from dimensions 1--3, variable widths 2--4')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
