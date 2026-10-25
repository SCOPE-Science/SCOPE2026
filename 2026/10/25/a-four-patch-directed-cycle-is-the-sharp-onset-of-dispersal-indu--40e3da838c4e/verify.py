"""Independent numerical consistency checks for finite cyclic patch spectra.

The analytic proof in RESULT.md, rather than this finite computation,
establishes the claims for continuous parameters and unbounded delay.
Run with Python 3 and its standard library: python verify.py
"""
import cmath
import math

PI = math.pi

def threshold_equation(t):
    return (PI/2)*(math.sin(t)+math.cos(t)-1)-t

def bisect_root(lo, hi, iterations=100):
    assert threshold_equation(lo)>0 and threshold_equation(hi)<0
    for _ in range(iterations):
        mid=(lo+hi)/2
        if threshold_equation(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

tstar=bisect_root(0.4,1.0)
qstar=math.sin(tstar)
assert 0.58145670170 < qstar < 0.58145670172
assert threshold_equation(.4)>0 and threshold_equation(1.0)<0
assert 0<qstar<1/math.sqrt(2)

# Check imaginary characteristic roots with all modal eigenvalues.
# Dimensionless characteristic equation z=q*(zeta-1)-exp(-z*s).
for n in (2,3,4):
    for q in (.1, .25, .5, .6, .8, 1.1):
        for k in range(n):
            zeta=cmath.exp(2j*PI*k/n)
            a=q*(zeta-1)
            A=-a.real
            B=abs(a.imag)
            if A>1+1e-10:
                continue
            r=math.sqrt(max(0.,1-A*A))
            w=B+r
            if w<1e-10:
                continue
            s=math.acos(-A)/w
            # Orient Fourier mode so the imaginary part of a is positive.
            aa=complex(-A,B)
            residual=1j*w-aa+cmath.exp(-1j*w*s)
            assert abs(residual)<2e-12, (n,q,k,residual)
            if 0<A<1:
                e=cmath.exp(-1j*w*s)
                derivative=(1j*w*e)/(1-s*e)
                expected=w*r/((1+s*A)**2+(s*r)**2)
                assert abs(derivative.real-expected)<2e-12
                assert derivative.real>0

for q in (.01,.1,.25,.5,.6):
    if q<=2/3:
        t=math.asin(1.5*q)
        t3=(PI/2+t)/(math.cos(t)+math.sin(t)/math.sqrt(3))
        assert t3>PI/2
for q in (.01,.1,.25,.5,qstar-.001):
    trot=math.acos(-q)/(q+math.sqrt(1-q*q))
    assert trot<PI/2
for q in (qstar+.001,.65,.85,.99,1.):
    trot=math.acos(-q)/(q+math.sqrt(1-q*q))
    assert trot>PI/2

rot=math.acos(-.5)/(.5+math.sqrt(.75))
assert abs(rot-4*PI/(3*(1+math.sqrt(3))))<1e-14
assert rot<PI/2
assert abs((PI/2)-rot-0.037592700719656)<1e-12
print('PASS: unique-transition bracket, modal imaginary roots, transverse crossings, mode ordering, and exact witness')
print('q_star=',format(qstar,'.15f'),'witness_T=',format(rot,'.15f'))
