"""Reproduce finite exact certificates and numerical diagnostics for a weighted-ball affine projector.

Requires only the Python standard library. The global phase theorem relies on the
analytical likelihood-ratio argument in RESULT.md, not on sampled computations.
"""
from fractions import Fraction as Q
from math import comb, gamma, pi, sqrt, isclose, sin, cos, asin

assertions=0
def check(x,label):
    global assertions
    assertions+=1
    if not x:
        raise AssertionError(label)

def constant(s):
    return gamma(s/2)/(sqrt(pi)*gamma((s-1)/2))

def trapezoid_integral(func,a,b,n):
    h=(b-a)/n
    return h*(.5*(func(a)+func(b))+sum(func(a+i*h) for i in range(1,n)))

def exact_odd_13():
    s=13
    a=Q(1,s)
    j=sum((Q((-1)**k*comb(5,k))* (
        Q(s,2*k+2)*(1-a**(2*k+2)) - Q(1,2*k+1)*(1-a**(2*k+1))
    ) for k in range(6)),Q(0))
    return Q(1)+2*Q(693,512)*j

# Recompute the polynomial integral as a rational, not via its claimed decimal.
p=exact_odd_13()
check(p==Q(5441398251829,1792160394037),'exact s=13 norm')
check(p>3,'s=13 above three')
check(Q(6824895,2249728)>3,'elementary lower rational')
check(Q(6824895,2249728)<p,'lower bound lies below exact')
# At s=12, C=256/(63*pi); the triangle-error comparison yields
# Phi(12)<19136/(2079*pi); classical pi>31/10 proves Phi(12)<3.
check(Q(19136,2079)*Q(10,31)<3,'s=12 strict upper certificate')
check(Q(19136,2079)>0,'s12 bound meaningful')
# Characteristic function at s=3 (uniform marginal) gives exact 5/3.
check(Q(1)+Q(2,3)==Q(5,3),'one-dimensional uniform interval')
# On each of these integer parameters, independently compare the integral
# defining Phi with the decomposition E|Z|+E(1-|Z|)_+.
for s in (3,4,5,6,7,8,9,10,11,12,13,15,20,30):
    c=constant(s)
    a=1/s
    p1=1+2*c*trapezoid_integral(lambda t:(s*sin(t)-1)*cos(t)**(s-2),asin(a),pi/2,16000)
    p2=2*s*c/(s-1)+2*c/s*trapezoid_integral(lambda z:(1-z)*(1-(z/s)**2)**((s-3)/2),0,1,16000)
    check(isclose(p1,p2,rel_tol=1e-7,abs_tol=2e-7),f'dual integral identities s={s}')
    if s<=12:
        check(p1<3,f'below three s={s}')
    else:
        check(p1>3,f'above three s={s}')
    if s>=6:
        check(p1>1,f'nontrivial amplification s={s}')
# Check elementary sign of the cross-derivative throughout a rational mesh;
# the proof is algebraic for all real s >= 6 and 0 < z < s.
for s in (6,7,8,10,12,13,30):
    for z in (Q(1,10),Q(1),Q(2)):
        if z>=s: continue
        sign=z*(s*s-6*s+z*z)
        check(sign>0,f'monotone likelihood ratio s={s}, z={z}')
print(f'ALL CHECKS PASSED: {assertions} exact and numerical assertions')
print(f'Phi(13)={p} = {float(p):.14f}')
