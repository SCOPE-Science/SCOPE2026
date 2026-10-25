"""Interval verification for the dodecagon rounding coefficient.
Requires mpmath >= 1.3; run python verify.py.
The program does not assert global minimization over Fourier directions.
"""
from mpmath import iv
iv.dps=40
pi=iv.pi
s3=iv.sqrt(3)
R=iv.sqrt(pi/3)
r=R*iv.cos(pi/12)
ell=2*R*iv.sin(pi/12)
def sinc(x): return iv.sin(x)/x
def sincprime(x): return (x*iv.cos(x)-iv.sin(x))/(x*x)
def a(k):
    return (iv.sin(k*r)
       +s3*iv.sin(s3*k*r/2)*sinc(k*ell/4)
       +iv.sin(k*r/2)*sinc(s3*k*ell/4))
def aprime(k):
    return (r*iv.cos(k*r)
       +s3*((s3*r/2)*iv.cos(s3*k*r/2)*sinc(k*ell/4)
            +iv.sin(s3*k*r/2)*(ell/4)*sincprime(k*ell/4))
       +(r/2)*iv.cos(k*r/2)*sinc(s3*k*ell/4)
       +iv.sin(k*r/2)*(s3*ell/4)*sincprime(s3*k*ell/4))
def f(k): return 2*ell*a(k)/k
def definitely_positive(x): return x.a>0
def definitely_negative(x): return x.b<0
lo=iv.mpf('3.83171224396364')
hi=iv.mpf('3.83171224396366')
k=iv.mpf(['3.83171224396364','3.83171224396366'])
assert definitely_positive(f(lo)), f(lo)
assert definitely_negative(f(hi)), f(hi)
fprime=2*ell*aprime(k)/k-2*ell*a(k)/(k*k)
assert definitely_negative(fprime), fprime
sumcos=4*sum((iv.cos(k*R*iv.cos((2*j+1)*pi/12)) for j in range(3)),iv.mpf(0))
c=iv.tan(pi/12)-pi/12
coefficient=c*(sumcos/fprime-6*k/pi)
assert definitely_negative(coefficient), coefficient
assert coefficient.a > iv.mpf('-0.00014158574850')
assert coefficient.b < iv.mpf('-0.00014158574849')
print('Root bracket verified; first-root identification is sourced.')
print('F(left):',f(lo))
print('F(right):',f(hi))
print('Derivative:',fprime)
print('Quadratic coefficient:',coefficient)
print('Interval checks passed')
