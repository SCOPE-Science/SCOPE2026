"""Exact coefficient and independent numerical checks for a cubic-harmonic support family.
Run: python3 verify_quartic.py; requires Python standard library only.
The continuum inequalities are proved analytically in RESULT.md; finite samples are corroborative.
"""
from fractions import Fraction as F
from math import sqrt, sin, cos, pi
from random import Random

# Sparse polynomial dictionary in a=u_1^2,b=u_2^2,c=u_3^2.
def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items(): out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}
def mul(p, q):
    out={}
    for x, a in p.items():
        for y, b in q.items():
            z=tuple(i+j for i,j in zip(x,y)); out[z]=out.get(z,F(0))+a*b
    return {k:v for k,v in out.items() if v}
def sc(p, k): return {j:v*k for j,v in p.items()}
def power(p,k):
    out={(0,0,0):F(1)}
    for _ in range(k): out=mul(out,p)
    return out
one={(0,0,0):F(1)}
a={(1,0,0):F(1)};b={(0,1,0):F(1)};c={(0,0,1):F(1)}
s=add(mul(a,b),mul(b,c),mul(c,a)); r=mul(mul(a,b),c)
y=add(sc(one,F(2,5)),sc(s,-2))
t=add(sc(s,36),sc(one,-F(36,5)))
d=add(sc(mul(s,s),180),sc(s,-F(648,5)),sc(one,F(324,25)),sc(r,432))
def double_factorial(n):
    v=1
    for k in range(n,0,-2):v*=k
    return v
def moment(k):
    # Sphere S^2: E[u_1^{2i}u_2^{2j}u_3^{2k}]
    p=sum(k); return F(double_factorial(2*k[0]-1)*double_factorial(2*k[1]-1)*double_factorial(2*k[2]-1),double_factorial(2*p+1))
def E(poly):return sum((v*moment(k) for k,v in poly.items()),F(0))
assert E(y)==0 and E(t)==0
assert E(d)==F(-48,175)
assert E(mul(y,t))==F(-96,175)
assert E(mul(y,d))==F(52224,125125)
q2=E(add(d,mul(y,t)));q3=E(mul(y,d))
assert q2==F(-144,175)
assert q3==F(52224,125125)
assert (1+q2*F(-10,39)**2+q3*F(-10,39)**3)==F(2654675,2827539)
assert (1+q2*F(5,18)**2+q3*F(5,18)**3)==F(229975,243243)
print('EXACT_SPHERICAL_MOMENTS_AND_VOLUME_POLYNOMIAL_OK',q2,q3)

# Exact equality configurations of the curvature extrema.
def eigenvalues_perturbation(u):
    x=[v*v for v in u]
    s0=x[0]*x[1]+x[1]*x[2]+x[2]*x[0]
    r0=x[0]*x[1]*x[2]
    delta=sqrt(max(0.,s0*s0-3*r0))
    return (18*s0-F(18,5)-12*delta,18*s0-F(18,5)+12*delta)
assert eigenvalues_perturbation((1.,0.,0.))==(-3.6,-3.6)
v1,v2=eigenvalues_perturbation((1/sqrt(2),1/sqrt(2),0.))
assert abs(v1+2.1)<1e-12 and abs(v2-3.9)<1e-12
print('EXACT_ENDPOINT_CURVATURE_TYPES_OK axes=6 face_diagonals=12')

# Schur certificate test on rational simplex lattice. Not a proof of the continuum claim.
for m in (20,60):
    for i in range(m+1):
        for j in range(m+1-i):
            k=m-i-j
            aa,bb,cc=F(i,m),F(j,m),F(k,m)
            ss=aa*bb+bb*cc+cc*aa; rr=aa*bb*cc
            schur=1+9*rr-4*ss
            cert=25-120*ss+80*ss*ss+192*rr
            assert schur>=0 and cert>=0
            assert cert==5*(1-4*ss)*(5-4*ss)+192*rr
print('RATIONAL_SCHUR_AND_QUARTIC_CERTIFICATE_GRID_OK')

# Independent Hessian comparison: principal curvatures of degree-four normal function.
rng=Random(240913)
for j in range(12000):
    u=[rng.gauss(0,1) for i in range(3)]
    norm=sqrt(sum(x*x for x in u));u=[x/norm for x in u]
    # choose v orthogonal to u
    v=[rng.gauss(0,1) for i in range(3)]; dot=sum(x*y for x,y in zip(u,v))
    v=[x-dot*y for x,y in zip(v,u)]; norm=sqrt(sum(x*x for x in v)); v=[x/norm for x in v]
    H=sum(x**4 for x in u); B=sum(x*x*y*y for x,y in zip(u,v))
    Q=12*B-3*H-.6
    assert -3.6000000001 <= Q <=3.9000000001
    lo,hi=eigenvalues_perturbation(u)
    assert lo-1e-10<=Q<=hi+1e-10
print('INDEPENDENT_TANGENT_QUADRATIC_FORM_OK 12000')

# Recompute closed volume factors from exact polynomial.
for e in (F(0),F(1,5),F(-10,39),F(5,18)):
    f=1+q2*e**2+q3*e**3
    assert f>0
print('VOLUME_ENDPOINTS_OK',F(2654675,2827539),F(229975,243243))
print('ALL_CUBIC_HARMONIC_CHECKS_OK')
