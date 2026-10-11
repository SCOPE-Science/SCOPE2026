"""Reproducible exact-rational geometry tests for the hexagonal transference stability statement.

These finite tests supplement the parameter-uniform analytic argument in RESULT.md.
Standard-library only: run `python verify.py`.
"""
from fractions import Fraction as F
from math import isqrt
from random import Random

Q = [(-1, -1), (0, -1), (1, 0), (1, 1), (0, 1), (-1, 0)]
R = [(Q[i-1][0]+Q[i][0], Q[i-1][1]+Q[i][1]) for i in range(6)]
H = [((Q[i-1][0]+R[i][0]+Q[i][0])/F(3),
      (Q[i-1][1]+R[i][1]+Q[i][1])/F(3)) for i in range(6)]

def det(x, y):
    return x[0]*y[1]-x[1]*y[0]

def sub(x, y):
    return x[0]-y[0],x[1]-y[1]

def dot(x, y):
    return x[0]*y[0]+x[1]*y[1]

def cross(a, b, p):
    return det(sub(b,a),sub(p,a))

def intersection(u, v, c, d):
    # u.x=c and v.x=d
    z=det(u,v)
    assert z
    return ((c*v[1]-u[1]*d)/z, (u[0]*d-c*v[0])/z)

def barycentric(i, p):
    base=Q[i]
    u=sub(Q[i-1],base)
    v=sub(R[i],base)
    x=sub(p,base)
    z=det(u,v)
    a=det(x,v)/z
    b=det(u,x)/z
    return a,b,1-a-b

# Prove a complete finite set assertion used in RESULT.md: all lattice points
# in the large auxiliary hexagon are precisely 0 and the two vertex orbits.
points={(x,y) for x in range(-2,3) for y in range(-2,3)
        if all(cross(R[i],R[(i+1)%6],(x,y))>=0 for i in range(6))}
assert points == set(Q)|set(R)|{(0,0)}

# Base support normals on the edges through Q_i.
N=[]
for i in range(6):
    dx,dy=sub(H[(i+1)%6],H[i]); N.append((dy,-dx))
for i in range(3): assert N[i+3] == tuple(-v for v in N[i])

rng=Random(20260429)
tested=0
for it in range(1500):
    # Rational perturbations of the three antipodal line pairs.
    n=[]
    for i in range(3):
        dx=F(rng.randrange(-13,14),1000)
        dy=F(rng.randrange(-13,14),1000)
        n.append((N[i][0]+dx,N[i][1]+dy))
    n.extend([(-u,-v) for (u,v) in n])
    c=[dot(n[i],Q[i]) for i in range(6)]
    p=[intersection(n[i-1],n[i],c[i-1],c[i]) for i in range(6)]
    assert all(p[i+3]==tuple(-z for z in p[i]) for i in range(3))
    abc=[barycentric(i,p[i]) for i in range(6)]
    assert all(min(x)>0 and sum(x)==1 for x in abc)
    assert all(cross(p[i],p[(i+1)%6],p[(i+2)%6])>0 for i in range(6))
    # All six Q_i are strictly inside the corresponding boundary segments.
    assert all(cross(p[i],p[(i+1)%6],Q[i])==0 for i in range(6))
    assert all(dot(sub(Q[i],p[i]),sub(p[(i+1)%6],Q[i]))>0 for i in range(6))
    # Product identity and exact short-direction width profile.
    a=[abc[i][0] for i in range(3)]
    b=[abc[i][1] for i in range(3)]
    d=[abc[i][2] for i in range(3)]
    assert (b[0]*b[1]*b[2])**2 == a[0]*d[0]*a[1]*d[1]*a[2]*d[2]
    u=[(1,0),(0,1),(1,-1)]
    widths=[max(dot(v,x) for x in p)-min(dot(v,x) for x in p) for v in u]
    assert sorted(widths) == sorted([2+2*t for t in b])
    eps=F(1,3)-min(b)
    assert eps>=0
    if eps<=F(1,90):
        for i in range(6):
            dist2=sum((p[i][j]-H[i][j])**2 for j in range(2))
            assert dist2 <= 100*eps
    tested+=1

# Exact-rational coarse control of the analytic one-parameter family:
# b(t)=(-1+2*sqrt(1-3t*t))/3, eps(t)=(2/3)*(1-sqrt(1-3t*t)).
# We use rational upper/lower brackets for the square root, avoiding floats.
def sqrt_interval(v,unit=10**30):
    scaled=v*unit*unit
    k=isqrt(scaled.numerator//scaled.denominator)
    return F(k,unit),F(k+1,unit)

for k in range(-100,101):
    t=F(k,1000)
    lo,hi=sqrt_interval(1-3*t*t)
    hi=min(hi,F(1))
    assert lo>0
    emin=F(2,3)*(1-hi)
    emax=F(2,3)*(1-lo)
    assert emin>=0 and emax<=2*t*t+F(1,10**25)
    if t:
        # h_K(-1,-1)-h_H(-1,-1) >= |t| - (1-sqrt(1-3t^2)).
        support_lower=abs(t)-(1-lo)
        assert support_lower >= abs(t)/2

print('VERIFY_OK:', tested, 'exact rational blocking-hexagon tests;',
      201, 'certified square-root brackets; 13 lattice points enumerated')
