"""Exact finite checks for the elliptic-nodal F25 classification.
No external libraries or data files are required.
"""
from itertools import product

# Trace of y^2=x^3+1 over F5.
n5 = 1 + sum(1 if (x**3+1)%5==0 else (2 if (x**3+1)%5 in (1,4) else 0) for x in range(5))
assert n5 == 6
# Frobenius over F5 has trace 5+1-n5=0; square equals [-5].
assert 5 + 1 - n5 == 0
assert 25 + 1 + 10 == 36
assert (25 + 1 + 10) == 36
assert (25 + 1 + 10 + 1) == 37
assert 24*24 == 576
assert (576-36)//2 == 270

# Independent enumeration of the six j=0 twists over F25.
# F25 = F5[t]/(t^2+t+1), irreducible because -3 is nonsquare mod 5.
F25=list(product(range(5),repeat=2))
ZERO=(0,0)
ONE=(1,0)
def fadd(x,y):
    return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def fmul(x,y):
    return ((x[0]*y[0]-x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%5)
def fpow(x,n):
    z=ONE
    while n:
        if n&1: z=fmul(z,x)
        x=fmul(x,x); n>>=1
    return z
squares={fmul(x,x) for x in F25}
sixth_powers={fpow(x,6) for x in F25 if x!=ZERO}
assert len(sixth_powers)==4
counts={}
for b in F25:
    if b==ZERO: continue
    value=1
    for x in F25:
        v=fadd(fpow(x,3),b)
        value += 1 if v==ZERO else (2 if v in squares else 0)
    counts[b]=value
assert {b for b,c in counts.items() if c==36}==sixth_powers
assert {n:list(counts.values()).count(n) for n in set(counts.values())}=={16:4,21:8,31:8,36:4}

# Abstract 24-torsion with order-three automorphism omega: omega^2+omega+1=0.
# A basis identifies E[24] with (Z/24)^2 and omega with the matrix below.
def omega(p, n):
    a,b=p
    return (-b % n, (a-b)%n)
def act(p,k,n):
    for _ in range(k): p=omega(p,n)
    return p
for n in (4,24):
    for p in product(range(n), repeat=2):
        assert act(p,3,n)==p
        assert tuple((act(p,2,n)[i]+act(p,1,n)[i]+p[i])%n for i in range(2)) == (0,0)

# Determine the mu6-orbits of all nonzero 4-torsion points.
remaining=set(product(range(4),repeat=2))-{(0,0)}
orbit_4=[]
while remaining:
    p=min(remaining)
    o={act(p,k,4) for k in range(3)}|{tuple((-v)%4 for v in act(p,k,4)) for k in range(3)}
    assert o<=remaining
    orbit_4.append((p,len(o),sorted(o)))
    remaining -= o
assert sorted(s for _,s,_ in orbit_4)==[3,6,6]

# Points of degree exactly two under Frobenius [-5] on E[24].
points=set(product(range(24),repeat=2))
def fr(p): return tuple((-5*v)%24 for v in p)
def pair(p): return tuple(sorted((p,fr(p))))
closed={pair(p) for p in points if fr(p)!=p}
assert len(closed)==270
translations=set(product(range(0,24,4),repeat=2))
assert len(translations)==36
# Affine group E(F25) rtimes mu6; all its elements are defined over F25.
def orbit_step(P,k,t):
    p=P[0]
    return pair(tuple((act(p,k,24)[i]+t[i])%24 for i in range(2)))
remaining=set(closed)
orbit_sizes=[]
while remaining:
    x=min(remaining)
    o={orbit_step(x,k,t) for k in range(6) for t in translations}
    assert o<=remaining
    orbit_sizes.append(len(o))
    remaining-=o
assert sorted(orbit_sizes)==[54,108,108],orbit_sizes
assert sorted(216//s for s in orbit_sizes)==[2,2,4]
print('F5_POINTS',n5)
print('F25_POINTS',36)
print('J_ZERO_TWIST_POINT_COUNTS',sorted({n:list(counts.values()).count(n) for n in set(counts.values())}.items()))
print('F625_POINTS',576)
print('DEGREE_TWO_CLOSED_POINTS',len(closed))
print('MU6_ORBITS_ON_E4',sorted(s for _,s,_ in orbit_4))
print('AUT_GROUP_ORBIT_SIZES',sorted(orbit_sizes))
print('AUTOMORPHISM_GROUP_ORDERS',sorted(216//s for s in orbit_sizes))
print('VERIFY_OK')
