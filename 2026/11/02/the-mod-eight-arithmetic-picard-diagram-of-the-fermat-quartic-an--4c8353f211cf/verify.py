#!/usr/bin/env python3
"""Exact arithmetic of the classical-line lattice on the Fermat quartic."""
from fractions import Fraction
from itertools import product
from collections import Counter

LABELS=[(k,i,j) for k in range(3) for i in range(4) for j in range(4)]

def meet(x,y):
    k,i,j=x; h,t,u=y
    if k==h:
        return (i==t)!=(j==u)
    a,b,c,d=2*i+1,2*j+1,2*t+1,2*u+1
    if k==0 and h==1: return (a+d-b-c)%8==0
    if k==0 and h==2: return (a+b+d-c)%8==0
    if k==1 and h==2: return (a+b-c-d)%8==0
    return meet(y,x)

M=[[-2 if i==j else int(meet(LABELS[i], LABELS[j])) for j in range(48)] for i in range(48)]

def rank(matrix):
    a=[[Fraction(x) for x in row] for row in matrix]
    h=len(a);w=len(a[0]);r=0
    for c in range(w):
        pivot=next((j for j in range(r,h) if a[j][c]!=0),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        d=a[r][c]
        a[r]=[v/d for v in a[r]]
        for j in range(r+1,h):
            if a[j][c]:
                d=a[j][c]
                a[j]=[v-d*w for v,w in zip(a[j],a[r])]
        r+=1
        if r==h:break
    return r

def index(k,i,j):return 16*k+4*i+j

def frob_map(p):
    return [index(k,((p*(2*i+1))%8-1)//2,((p*(2*j+1))%8-1)//2) for k,i,j in LABELS]

def orbit_gram(p):
    f=frob_map(p);used=set();orbits=[]
    for i in range(48):
        if i in used:continue
        cyc=[];j=i
        while j not in used:
            used.add(j);cyc.append(j);j=f[j]
        assert j==i
        orbits.append(cyc)
    matrix=[[sum(M[i][j] for i in x for j in y) for y in orbits] for x in orbits]
    return orbits,matrix

def points(p):
    total=0
    for pivot in range(4):
        # The earliest nonzero homogeneous coordinate is normalized to 1.
        for tail in product(range(p),repeat=3-pivot):
            x=(0,)*pivot+(1,)+tail
            total+=int(sum(pow(t,4,p) for t in x)%p==0)
    return total

assert len(LABELS)==48
assert all(M[i][j]==M[j][i] for i in range(48) for j in range(48))
assert all(M[i][i]==-2 for i in range(48))
assert Counter(sum(v==1 for v in row) for row in M)=={14:48}
assert rank(M)==20
print('classical_lines 48; intersection_valency 14; rational_gram_rank 20')
for p,want in zip([1,3,5,7],[20,11,8,11]):
    f=frob_map(p)
    assert all(f[f[i]]==i for i in range(48))
    orbits,gram=orbit_gram(p)
    got=rank(gram)
    assert got==want
    lengths=dict(Counter(map(len,orbits)))
    print(f'p_mod8={p}; orbit_size_counts={lengths}; invariant_gram_rank={got}; line_minus_dim={20-got}')
for p in (3,7):
    got=points(p)
    assert got==(p+1)**2
    print(f'points_F{p}={got}; split_quadric_count={(p+1)**2}')
assert (12+10)==22 and (12-10)==2
assert (12-11,10-9)==(1,1)
print('VERIFY_OK')
