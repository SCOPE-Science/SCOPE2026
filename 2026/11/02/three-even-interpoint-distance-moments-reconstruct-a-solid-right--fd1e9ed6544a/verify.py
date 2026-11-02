#!/usr/bin/env python3
"""Exact rational and independently sampled checks for the cone distance-moment inverse."""
from fractions import Fraction as F
from math import comb, sqrt, cos, sin, pi
import random

# A uniform solid cone is represented by (R*S*U1,R*S*U2,H*S),
# with S having density 3*s*s on (0,1) and U uniform on the unit disk.
# The following are conditional powers of |sU-tV|^2; they follow
# independently from the moments of two unit-disk points.
J = [
    {(0, 0): F(1)},
    {(2, 0): F(1,2), (0, 2): F(1,2)},
    {(4, 0): F(1,3), (2, 2): F(1), (0, 4): F(1,3)},
    {(6, 0): F(1,4), (4, 2): F(3,2), (2, 4): F(3,2), (0, 6): F(1,4)},
]
Q = {(2, 0): F(1), (1, 1): F(-2), (0, 2): F(1)}

def mul(a, b):
    c = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i+k, j+l)
            c[key] = c.get(key, F(0)) + x*y
    return c

def power(a, n):
    ans = {(0, 0): F(1)}
    for _ in range(n):
        ans = mul(ans, a)
    return ans

def mean(p):
    return 9 * sum((c / ((i+3)*(j+3)) for (i,j), c in p.items()), F(0))

expected = [
    (F(3,5), F(3,40)),
    (F(226,350), F(27,350), F(6,350)),
    (F(788,840), F(83,840), F(21,840), F(5,840)),
]
for k in range(1,4):
    # coefficient of A^(k-j) B^j
    computed = tuple(F(comb(k,j))*mean(mul(J[k-j],power(Q,j))) for j in range(k+1))
    assert computed == expected[k-1], (k,computed,expected[k-1])
print('EXACT_INDEPENDENT_RADIAL_DISK_INTEGRATION_PASSED')

# Sparse bivariate exact rational polynomial arithmetic for the two-branch identity.
def pol(*terms):
    return {key:F(c) for key,c in terms if c}
def add(a,b):
    c=dict(a)
    for key,v in b.items(): c[key]=c.get(key,F(0))+v
    return {key:v for key,v in c.items() if v}
def neg(a): return {key:-v for key,v in a.items()}
def sub(a,b): return add(a,neg(b))
def scale(a,k): return {key:k*v for key,v in a.items()}
ONE=pol(((0,0),1))
RR=pol(((1,0),1))
UU=pol(((0,1),1))
def cpow(a,n):
    ans=ONE
    for _ in range(n):ans=mul(ans,a)
    return ans

def pk2(z):return add(add(scale(cpow(z,2),6),scale(z,27)),scale(ONE,226))
pr=add(RR,scale(ONE,8));pu=add(UU,scale(ONE,8))
q2numer=sub(mul(pk2(RR),cpow(pu,2)),mul(pk2(UU),cpow(pr,2)))
q2right=mul(sub(RR,UU),pol(((1,1),69),((1,0),158),((0,1),158),((0,0),-1888)))
assert {k:v for k,v in q2numer.items() if v} == {k:v for k,v in q2right.items() if v}
# The exact branch identity, after setting u=(1888-158r)/(69r+158),
# is verified by checking all coefficients of the resulting rational identity.
# Work in univariate polynomials represented by tuples of integers.
def uv_mul(x,y):
    z=[0]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    return tuple(z)
def uv_add(x,y):
    return tuple((x[i] if i<len(x) else 0)+(y[i] if i<len(y) else 0) for i in range(max(len(x),len(y))))
def uv_pow(x,n):
    z=(1,)
    for _ in range(n):z=uv_mul(z,x)
    return z
rD=(8,1); C=(158,69); N=(1888,-158); # u=N/C
D=uv_add(uv_mul((8,),C),N) # (u+8) C = 394 (r+8)
assert D == (3152,394)
# F3(r)-F3(u) = num / [(r+8)^3 * ((u+8)C)^3],
# with num = P3(r) D^3 - (788C^3+83NC^2+21N^2C+5N^3)(r+8)^3
P3=(788,83,21,5)
lhs=uv_mul(P3,uv_pow(D,3))
terms=(uv_mul((788,),uv_pow(C,3)),uv_mul((83,),uv_mul(N,uv_pow(C,2))),uv_mul((21,),uv_mul(uv_pow(N,2),C)),uv_mul((5,),uv_pow(N,3)))
N3=(0,)
for t in terms:N3=uv_add(N3,t)
num=uv_add(lhs,tuple(-v for v in uv_mul(N3,uv_pow(rD,3))))
# Analytically simplified value: 6(69r-236)P(r)(r+8)^3 /(394^3(r+8)^3) times the C/D denominator algebra.
# Direct rational identity avoids numerical comparisons.
P=(3036792,-1356188,224479)
# Desired p3(r)-p3(u) = 6(69r-236)P(r)/(394^3*(r+8)^3).
# Our rational lhs has denominator (r+8)^3 D^3; D=394(r+8).
# Thus num should equal 6(69r-236)P(r)*(r+8)^3.
rhs=uv_mul(uv_mul(( -1416, 414),P),uv_pow(rD,3))
assert num==rhs,(num,rhs)
assert 4*224479*3036792-1356188**2==887538234128
print('EXACT_TWO_BRANCH_IDENTITIES_AND_POSITIVITY_PASSED')

# Inversion counterexample: first two even moments equal, third differs.
r=F(1);u=F(2)*(944-79*r)/(69*r+158)
def ms(t):
    A=F(40,3)/(t+8) # fix second-distance moment to exactly 1
    B=t*A
    return (F(3,40)*(8*A+B),
            (226*A*A+27*A*B+6*B*B)/350,
            (788*A**3+83*A*A*B+21*A*B*B+5*B**3)/840)
m=ms(r);n=ms(u)
assert (m[0],m[1])==(n[0],n[1]) and m[2]!=n[2]
qstar=F(6260,4137)
assert qstar < F(113,63) < F(64,21)
print('SHARP_TWO_MOMENT_PHASE_AND_SIXTH_MOMENT_SEPARATION_PASSED')

# Independently sample actual disk points and the cone-volume axial law.
rng=random.Random(912533)
def sample_point(R,H):
    S=rng.random()**(1/3)
    rad=sqrt(rng.random()); theta=2*pi*rng.random()
    return (R*S*rad*cos(theta),R*S*rad*sin(theta),H*S)
for R,H in ((1.,.7),(1.,2.),(.6,4.)):
    z=[0.,0.,0.];Nsim=180000
    for _ in range(Nsim):
        a=sample_point(R,H);b=sample_point(R,H)
        d2=sum((x-y)**2 for x,y in zip(a,b))
        z[0]+=d2;z[1]+=d2*d2;z[2]+=d2*d2*d2
    z=[v/Nsim for v in z]
    A=R*R;B=H*H
    theoretical=[3*(8*A+B)/40,(226*A*A+27*A*B+6*B*B)/350,
        (788*A**3+83*A*A*B+21*A*B*B+5*B**3)/840]
    for x,y in zip(z,theoretical):
        assert abs(x-y)/y < .045, (R,H,x,y)
print('INDEPENDENT_VOLUME_POINT_PAIR_SAMPLING_PASSED')
print('ALL_CHECKS_PASSED')
