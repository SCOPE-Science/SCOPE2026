#!/usr/bin/env python3
"""Exact complete determinant spectrum for 3x3 F5^2 Fourier apertures.
Only standard-library integer arithmetic; no floating-point approximations.
"""
from collections import Counter
from itertools import combinations

P=5
points=[(x,y) for x in range(P) for y in range(P)]

def shift(u,v):return ((u[0]-v[0])%5,(u[1]-v[1])%5)

def square_det(A,B):
    # Reduction of matrix entries under affine normalization of A,
    # expressed by the two independent row differences.
    v=shift(A[1],A[0]); w=shift(A[2],A[0]);
    a=shift(B[1],B[0]); b=shift(B[2],B[0]);
    dot=lambda q,z:(q[0]*z[0]+q[1]*z[1])%5
    j1=dot(v,a); j2=dot(w,b); j3=dot(v,b); j4=dot(w,a)
    c=[0]*5
    for k,s in [(j1+j2,1),(j1,-1),(j2,-1),(j3+j4,-1),(j3,1),(j4,1)]:c[k%5]+=s
    R=[sum(c[j]*c[(j-k)%5] for j in range(5)) for k in range(3)]
    return (2*R[0]-R[1]-R[2], R[1]-R[2]) # Q=(X+Y sqrt(5))/2

def determinant_polynomial(A,B):
    # Independent permutation expansion of 3x3 determinant over Z[zeta].
    from itertools import permutations
    from math import prod
    coeff=[0]*5
    dot=lambda u,v:(u[0]*v[0]+u[1]*v[1])%5
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        expo=sum(dot(A[i],B[perm[i]]) for i in range(3))%5
        coeff[expo]+=(-1)**inv
    correlation=[sum(coeff[j]*coeff[(j-k)%5] for j in range(5)) for k in range(3)]
    return (2*correlation[0]-correlation[1]-correlation[2],correlation[1]-correlation[2])

expected_collinear={(0,0):1050,(25,-5):625,(25,5):625}
expected_cap={(0,0):150,(15,-5):500,(10,0):900,(25,-5):75,(35,-5):50,(15,5):500,(25,5):75,(35,5):50}

def calc(A,expected):
    cnt=Counter()
    for B in combinations(points,3):
        val=square_det(A,B)
        assert val==determinant_polynomial(A,B),(A,B,val)
        cnt[val]+=1
    assert cnt==expected,(A,cnt,expected)
    assert sum(cnt.values())==2300
    return cnt

# Independent rooted count: any unordered triple B has exactly three
# translations carrying a chosen member to the origin; each rooted set
# corresponds to 25/3 unrooted translated sets in aggregate.
def rooted_counts(A):
    zero=(0,0)
    return Counter(determinant_polynomial(A,(zero,u,v))
                   for u,v in combinations([w for w in points if w!=zero],2))

A_line=((0,0),(1,0),(2,0))
A_cap=((0,0),(1,0),(0,1))
assert rooted_counts(A_line)=={(0,0):126,(25,-5):75,(25,5):75}
assert rooted_counts(A_cap)=={(0,0):18,(10,0):108,(15,-5):60,(15,5):60,
                              (25,-5):9,(25,5):9,(35,-5):6,(35,5):6}
for A,table in ((A_line,expected_collinear),(A_cap,expected_cap)):
    assert all(rooted_counts(A)[q]*25==table[q]*3 for q in table)
assert calc(A_line,expected_collinear)[(25,5)]==625
assert calc(A_cap,expected_cap)[(35,5)]==50

# Geometry is only collinear or noncollinear, and every affine transformation
# maps either class to its displayed normal form.
assert 30*10==300
assert 2300-300==2000
assert 300*625+2000*50==287500
assert 300*1050+2000*150==615000
assert 300*1250+2000*2150==4675000
assert 615000+4675000==2300*2300

# Check the geometrically explicit equality cases.
line_opt={B for B in combinations(points,3) if square_det(A_line,B)==(25,5)}
assert len(line_opt)==625
want_x={frozenset(((t+i)%5 for i in (0,1,3))) for t in range(5)}
assert {frozenset(x for x,y in B) for B in line_opt}==want_x
for B in line_opt:assert frozenset(x for x,y in B) in want_x
cap_opt={B for B in combinations(points,3) if square_det(A_cap,B)==(35,5)}
assert len(cap_opt)==50
anchored={tuple(sorted([q for q in B if q!=(0,0)])) for B in cap_opt if (0,0) in B}
assert len(anchored)==6,anchored
for B in cap_opt:
    assert any(tuple(sorted([shift(v,b) for v in B if v!=b])) in anchored for b in B)
print('COLLINEAR',dict(sorted(calc(A_line,expected_collinear).items())))
print('NONCOLLINEAR',dict(sorted(calc(A_cap,expected_cap).items())))
print('ANCHORED OPTIMIZERS',sorted(anchored))
print('OPTIMAL_PAIRS',287500)
print('SINGULAR_PAIRS',615000)
print('CHECK_PASS')
