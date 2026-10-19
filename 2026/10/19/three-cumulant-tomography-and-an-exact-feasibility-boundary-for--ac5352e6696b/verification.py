"""Reproducible checks for stationary beta--Gaussian cumulant tomography."""
from fractions import Fraction as F
import math

def active_raw_even(n, b, a):
    # E[(aY)^(2n)], Y^2 ~ Beta(1/2,(b-1)/2).
    out = F(1)
    for j in range(n):
        out *= F(2*j+1,1)/ (b+2*j)
    return a**(2*n)*out

def gaussian_even(n, w):
    out = F(1)
    for j in range(1,n+1):
        out *= (2*j-1)*w
    return out

def raw_even(n,b,a,w):
    return sum(F(math.comb(2*n,2*j))*active_raw_even(j,b,a)*gaussian_even(n-j,w) for j in range(n+1))

def cumulants_from_raw(b,a,w):
    m2,m4,m6=(raw_even(n,b,a,w) for n in (1,2,3))
    return m2, m4-3*m2*m2,m6-15*m4*m2+30*m2**3

def cumulants_closed(b,a,w):
    return w+a*a/b, -6*a**4/(b*b*(b+2)),240*a**6/(b**3*(b+2)*(b+4))

def invert(k2,k4,k6):
    assert k2>0 and k4<0 and k6>0
    R=k6/(-k4)**1.5
    assert 0<R<4*math.sqrt(2)
    q=3*R**2/800
    b=(1-8*q+math.sqrt(1-8*q))/(2*q)
    a=((-k4)*b*b*(b+2)/6)**0.25
    w=k2-a*a/b
    assert b>1 and w>0
    return b,a,w

nchecks=0
for bd in range(2,22):
    b=F(bd,1)
    for an in range(1,7):
        a=F(an,3)
        for wd in range(1,8):
            w=F(wd,5)
            vals=cumulants_from_raw(b,a,w)
            assert vals==cumulants_closed(b,a,w)
            nchecks+=1
            bb,aa,ww=invert(*map(float,vals))
            assert math.isclose(bb,float(b),rel_tol=3e-10,abs_tol=5e-11)
            assert math.isclose(aa,float(a),rel_tol=3e-10,abs_tol=5e-11)
            assert math.isclose(ww,float(w),rel_tol=3e-10,abs_tol=5e-11)
            nchecks+=3

# Demonstrate continuum of indistinguishable second/fourth cumulants.
b0,a0,w0=F(3),F(2),F(1,2)
k2,k4,_=cumulants_closed(b0,a0,w0)
for b in [2.7,2.9,3.0,3.1,3.3]:
    aa=(-float(k4)*b*b*(b+2)/6)**.25
    ww=float(k2)-aa*aa/b
    assert ww>0
    k2a,k4a,_=cumulants_closed(b,aa,ww)
    assert abs(k2a-float(k2))<1e-11 and abs(k4a-float(k4))<1e-11
    nchecks+=3

for b in [1.000001,1.1,2,3,7,10,100,1000]:
    q=(b+2)/(b+4)**2
    R=(800*q/3)**.5
    inverse=(1-8*q+math.sqrt(1-8*q))/(2*q)
    assert math.isclose(inverse,b,rel_tol=3e-12)
    nchecks+=1
print(f'{nchecks} independent exact-rational or numeric assertions passed')
