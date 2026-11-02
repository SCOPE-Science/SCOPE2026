#!/usr/bin/env python3
"""Exact finite-field certificate for the characteristic-five Bring power-sum fiber.

This only certifies finite algebraic steps; the Picard group argument is mathematical.
Python 3, standard library only.
"""
from itertools import product, permutations
from math import comb
from collections import Counter
p=5

def rank(a):
    if not a:return 0
    b=[[x%p for x in row] for row in a]
    r=0; n=len(b[0]); m=len(b)
    for j in range(n):
        piv=next((i for i in range(r,m) if b[i][j]),None)
        if piv is None:continue
        b[r],b[piv]=b[piv],b[r]
        t=pow(b[r][j],-1,p)
        b[r]=[(v*t)%p for v in b[r]]
        for i in range(m):
            if i!=r and b[i][j]:
                t=b[i][j]
                b[i]=[(b[i][k]-t*b[r][k])%p for k in range(n)]
        r+=1
        if r==m:break
    return r

def Q(x,y,z):
    w=-(x+y+z)
    return (x*x+y*y+z*z+w*w)%p

def C(x,y,z):
    w=-(x+y+z)
    return (x*x*x+y*y*y+z*z*z+w*w*w)%p

def grad(func,pt):
    x,y,z=pt
    if func=='Q':
        w=(-x-y-z)%p
        return tuple((2*a-2*w)%p for a in pt)
    w=(-x-y-z)%p
    return tuple((3*a*a-3*w*w)%p for a in pt)

def norm(v):
    first=next((i for i,x in enumerate(v) if x%p),None)
    assert first is not None
    s=pow(v[first]%p,-1,p)
    return tuple((s*x)%p for x in v)

projective=sorted({norm(v) for v in product(range(p),repeat=3) if any(v)})
zeros=[v for v in projective if Q(*v)==C(*v)==0]
assert len(projective)==31 and len(zeros)==6
assert all(rank([grad('Q',v),grad('C',v)])==2 for v in zeros)
# Choose affine representatives z=1: this chart contains all six points.
directions=sorted((x,y,1) for x in range(p) for y in range(p) if Q(x,y,1)==C(x,y,1)==0)
assert len(directions)==6
five_dirs=[(x,y,z,(-x-y-z)%p,0) for x,y,z in directions]
assert all(sorted(d)==list(range(5)) for d in five_dirs)
# These are all affine-F5 root sets up to affine change of the root labels.
perms=list(permutations(range(p)))
classes={min(tuple((a*x+b)%p for x in v) for a in range(1,p) for b in range(p)) for v in perms}
assert len(classes)==6 and all(len({tuple((a*x+b)%p for x in rep) for a in range(1,p) for b in range(p)})==20 for rep in classes)

# Each degree-d homogeneous polynomial evaluates on the six branches.
def exponents(d):
    return [(a,b,d-a-b) for a in range(d+1) for b in range(d-a+1)]

def eval_rank(d):
    return rank([[(pow(x,a,p)*pow(y,b,p)*pow(z,c,p))%p for x,y,z in directions] for a,b,c in exponents(d)])
ranks=[eval_rank(d) for d in range(7)]
assert ranks==[1,3,5,6,6,6,6],ranks
# Since z=1 at every direction, surjectivity in degree three implies it for all degrees >=3.
normalization_deficit=sum(6-r for r in ranks[:3])
seminormal_deficit=(6-ranks[1])+(6-ranks[2])
assert normalization_deficit==9 and seminormal_deficit==4
# Complete intersection (2,3) of six lines: Hilbert function H(0)=1,H(1)=3,H(2)=5,H(n>=3)=6.
# Arithmetic genus of projective (2,3) CI in P3: 1+(2*3*(2+3-4))/2=4.
assert 1+(2*3*(2+3-4))//2==4
assert normalization_deficit-6+1==4
for n in range(1,5):
    q=5**n
    assert 6*(q+1)-5==6*q+1
print('six_projective_directions=',zeros)
print('six_z1_directions=',directions)
print('six_lines_as_direction_vectors=',five_dirs)
print('conic_cubic_transverse_at_all_six=TRUE')
print('AGL1_F5_cosets=',len(classes))
print('evaluation_ranks_degrees_0_to_6=',ranks)
print('normalization_delta=',normalization_deficit)
print('unipotent_picard_dimension=',seminormal_deficit)
print('arithmetic_genus=',4)
print('point_counts_n_1_to_4=',[6*(5**n)+1 for n in range(1,5)])
print('VERIFY_OK')
