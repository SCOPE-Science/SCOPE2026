"""Reproduce finite numeric checks for the sharp Blaschke lift envelope.

Requires only the Python standard library. Analytic proofs are in RESULT.md.
"""
import cmath
import math

phi=(1+math.sqrt(5))/2
r=math.sqrt(phi/2)
t=1/math.sqrt(2*phi)
q=t*t
h=1-r*r
A=q*h
D=(1-r**4)/phi

def cubic(x):
    return x*x*x+2*q*x-A

lo,hi=0.0,0.25
for _ in range(90):
    mid=(lo+hi)/2
    if cubic(mid)>0: hi=mid
    else: lo=mid
delta=(lo+hi)/2
Dmin=D+4*q*delta**2+delta**4-4*A*delta
ratio=(1-r**4)/Dmin
assert 0.09414 < delta < 0.09415
assert 1.70750 < ratio < 1.70754
assert ratio > phi

def integral_4(f, n=8192):
    return sum(abs(f(cmath.exp(2j*math.pi*j/n)))**4 for j in range(n))/n

def integral_2(f, n=8192):
    return sum(abs(f(cmath.exp(2j*math.pi*j/n)))**2 for j in range(n))/n

for phase in (0.0, 0.73, 1.49, 2.34):
    lam=cmath.exp(1j*phase)
    def inner(z):return (r-lam*z)/(1-r*lam*z)
    def F(z):return z*(inner(z)-t)
    c=delta/lam
    numer=integral_4(lambda z:(inner(z)-r)/z)
    denom=integral_4(lambda z:F(z)+c)
    assert abs(numer-(1-r**4))<3e-10,(phase,numer)
    assert abs(denom-Dmin)<3e-10,(phase,denom,Dmin)
    assert abs(integral_2(lambda z:inner(z)-t)-q)<3e-10

# An inner function of degree two with the same value at zero is strictly worse.
s=math.sqrt(r)
def inner_two(z): return ((s-z)/(1-s*z))**2
deriv=-2*s*(1-s*s)
assert abs(inner_two(0)-r)<2e-15
assert abs(deriv)<h
for x in (0.0,0.05,0.11,-0.07):
    F=lambda z:z*(inner_two(z)-t)
    lhs=integral_4(lambda z:F(z)+x)
    rhs=D+4*q*x*x+x**4+4*q*deriv*x
    assert abs(lhs-rhs)<3e-10,(x,lhs,rhs)

print('PASS: exact algebraic coefficient intervals, 4 automorphism phases,')
print('      and 4 second-degree inner-function comparison checks')
print('delta* = %.15f'%delta)
print('exact family quotient fourth power = %.15f'%ratio)
print('sharp family fourth-root norm lower bound = %.15f'%(ratio**0.25))
print('first backward-shift norm = %.15f'%(phi**0.25))
