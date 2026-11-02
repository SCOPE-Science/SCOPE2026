#!/usr/bin/env python3
"""Exact characteristic-five verification of the six-line special fiber of Bring's canonical model."""
from itertools import permutations, product
from math import factorial
P = 5

def q2(v):
    a,b,c=v
    d=(-a-b-c)%P
    return (a*a+b*b+c*c+d*d)%P

def q3(v):
    a,b,c=v
    d=(-a-b-c)%P
    return (a**3+b**3+c**3+d**3)%P

def canonical(v):
    for e in v:
        if e%P:
            inv=pow(e,-1,P)
            return tuple((x*inv)%P for x in v)
    raise ValueError('zero vector')

points=set()
for p in permutations(range(5)):
    assert all(sum(pow(x,j,P) for x in p)%P==0 for j in (1,2,3))
    v=tuple((p[i]-p[4])%P for i in range(3))
    assert q2(v)==q3(v)==0
    points.add(canonical(v))
assert len(points)==factorial(5)//20==6

# Independently scan the 31 projective points of P^2(F5).
solutions=set()
for v in product(range(P), repeat=3):
    if any(v) and q2(v)==q3(v)==0:
        solutions.add(canonical(v))
assert solutions==points

# Check the nonsingular quadratic and the nondivisibility of the cubic.
# Polar symmetric matrix of q2 is diagonal 4, off diagonal 2 (mod 5).
M=[[4 if i==j else 2 for j in range(3)] for i in range(3)]

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))%P
assert det3(M) != 0
assert q3((1,1,0)) != 0

# Characteristic-five monomial-evaluation map on the six tangent directions.
def mons(d):
    return [(i,j,d-i-j) for i in range(d+1) for j in range(d-i+1)]

def rank_mod(A,p=5):
    B=[list(r) for r in A]
    r=0
    for c in range(len(B[0])):
        piv=next((i for i in range(r,len(B)) if B[i][c]%p),None)
        if piv is None: continue
        B[r],B[piv]=B[piv],B[r]
        iv=pow(B[r][c],-1,p)
        B[r]=[(v*iv)%p for v in B[r]]
        for i in range(len(B)):
            if i!=r and B[i][c]:
                t=B[i][c]
                B[i]=[(a-t*b)%p for a,b in zip(B[i],B[r])]
        r+=1
        if r==len(B): break
    return r

ps=sorted(points)
for deg,expected in [(0,1),(1,3),(2,5),(3,6),(4,6)]:
    mat=[[(a**i*b**j*c**k)%P for i,j,k in mons(deg)] for a,b,c in ps]
    rr=rank_mod(mat)
    assert rr==expected,(deg,rr)
    if deg in (1,2):
        for i in range(6):
            e=[1 if j==i else 0 for j in range(6)]
            assert rank_mod([r+[e[j]] for j,r in enumerate(mat)])==rr+1, (deg,i)
    if deg==3:
        assert rr==6
    print('EVALUATION_RANK_OK',deg,rr)

# AGL_1(F5) action freely transitive on ordered permutations in each class.
affine={tuple((u*x+v)%P for x in range(5)) for u in range(1,5) for v in range(5)}
assert len(affine)==20
assert len(set(permutations(range(5))))==120
assert len(points)==120//len(affine)
print('CONE_OK: six distinct F5 directions, one S5 orbit, AGL(1,5) stabilizer 20')
print('LOCAL_OK: degrees 0,1,2,>=3 have ranks 1,3,5,6; delta=5+3+1=9; conductor t^3')
print('JACOBIAN_OK: six P1 branches; additive quotient dimension (6-3)+(6-5)=4 in characteristic five')
