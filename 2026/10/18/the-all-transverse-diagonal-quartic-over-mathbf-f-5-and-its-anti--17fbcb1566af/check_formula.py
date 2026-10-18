#!/usr/bin/env python3
"""Closed discriminant and line-orbit proof checks for diagonal quartics over F5."""
from collections import Counter
from itertools import product,permutations
import json

q=5

def discr(a,b,c):
    sym=(a*a*b+a*a*c+a*b*b+a*c*c+b*b*c+b*c*c)
    return ((a*b)**3+(a*c)**3+(b*c)**3+3*a*b*c*sym+4*a*a*b*b*c*c)%q

def line_count(a,b,c):
    pair=sum((u+v)%5!=0 for u,v in ((a,b),(a,c),(b,c)))
    return 3+4*pair+16*(discr(a,b,c)!=0)

counts=Counter();maximizers=[];internal=Counter()
for a,b,c in product(range(1,5),repeat=3):
    d=discr(a,b,c)
    opposite=sum((u+v)%5==0 for u,v in ((a,b),(a,c),(b,c)))
    internal[(opposite,d==0)]+=1
    n=line_count(a,b,c)
    counts[n]+=1
    if n==31:maximizers.append((a,b,c))

expected={tuple(p) for lam in (1,2,3,4) for p in set(permutations((lam,lam,2*lam%5)))}
assert counts=={15:16,23:12,27:24,31:12}
assert set(maximizers)==expected
assert internal=={(0,False):12,(0,True):16,(1,False):24,(2,False):12}

D=[[discr(1,b,c) for c in range(1,5)] for b in range(1,5)]
assert D==[[0,2,0,2],[2,0,4,1],[0,4,3,1],[2,1,1,2]]

# Count rational fibers on each line directly from coordinate-support patterns.
# A rational projective line has six points, and the number of rational
# points above a plane point of branch value v is 1 + Legendre(v).
def chi(x):
    x%=5
    return 0 if x==0 else 1 if x in (1,4) else -1

def rational_section_spectrum(weights):
    total=sum(weights)%5
    contributions=[]
    for zero in range(3):
        j,k=[i for i in range(3) if i!=zero]
        n=sum(1+chi(weights[i]) for i in (j,k))+4*(1+chi(weights[j]+weights[k]))
        contributions.append(n)
    for k in range(3):
        i,j=[idx for idx in range(3) if idx!=k]
        n=(1+chi(weights[k]))+(1+chi(weights[i]+weights[j]))+4*(1+chi(total))
        contributions.extend([n]*4)
    all_three=sum(1+chi(weights[i]+weights[j]) for i,j in ((0,1),(0,2),(1,2)))+3*(1+chi(total))
    contributions.extend([all_three]*16)
    assert len(contributions)==31
    return Counter(contributions)

profile=rational_section_spectrum((1,1,2))
other=rational_section_spectrum((2,2,4))
assert profile=={2:2,4:1,6:16,8:4,10:8}
assert other=={2:8,4:4,6:16,8:1,10:2}
assert sum(n*k for n,k in profile.items())==216
assert sum(n*k for n,k in other.items())==156
assert other==Counter({12-n:k for n,k in profile.items()})

report={'normalized_discriminant_matrix':D,
        'singularity_pattern_counts':{f'opposite_pairs={k[0]},generic_discriminant_zero={k[1]}':v for k,v in sorted(internal.items())},
        'smooth_section_counts_by_coefficients':dict(sorted(counts.items())),
        'all_smooth_triples':[list(v) for v in sorted(maximizers)],
        'two_twist_point_spectra':{'square_scale':dict(sorted(profile.items())),
                                   'nonsquare_scale':dict(sorted(other.items()))}}
print(json.dumps(report,indent=2,sort_keys=True))
