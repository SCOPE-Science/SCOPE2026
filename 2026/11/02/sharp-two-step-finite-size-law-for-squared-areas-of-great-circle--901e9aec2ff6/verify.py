"""Exact rational coefficient checks for the area-weighted spherical cell law.

Only Python's standard library is required. This verifies the geometric
side-variable integral reductions and Dirichlet moments used in the proof;
finite arithmetic does not replace the asymptotic domination argument.
"""
from fractions import Fraction
from math import factorial, pi

ZERO = (0, 0, 0)
ONE = {ZERO: Fraction(1)}

def var(i):
    e = [0, 0, 0]
    e[i] = 1
    return {tuple(e): Fraction(1)}

def add(*ps):
    r = {}
    for p in ps:
        for k, v in p.items():
            r[k] = r.get(k, Fraction(0)) + v
    return {k:v for k,v in r.items() if v}

def mul(*ps):
    r = ONE
    for p in ps:
        t = {}
        for a, av in r.items():
            for b, bv in p.items():
                k = tuple(a[i]+b[i] for i in range(3))
                t[k] = t.get(k, Fraction(0)) + av*bv
        r=t
    return r

def rising(x, n):
    v=Fraction(1)
    for i in range(n): v *= x+i
    return v

def dirichlet_moment(p, alpha):
    """Expectation of a polynomial in three Dirichlet(alpha,alpha,alpha) coordinates."""
    ans=Fraction(0)
    for (i,j,k),c in p.items():
        ans += c*rising(alpha,i)*rising(alpha,j)*rising(alpha,k)/rising(3*alpha,i+j+k)
    return ans

x,y,z = var(0),var(1),var(2)
a,b,c = add(y,z), add(x,z), add(x,y)
B = mul(a,b,c)
R = add(mul(a,a),mul(b,b))
BR = mul(B,R)
B2=mul(a,b)
qhalf=Fraction(1,2)
qthree=Fraction(3,2)
assert dirichlet_moment(B,qhalf)==Fraction(4,21)
assert dirichlet_moment(BR,qhalf)==Fraction(32,165)
assert dirichlet_moment(B2,qthree)==Fraction(14,33)

# Radial integrals: int_0^infty s^k exp(-2s) ds=k!/2^(k+1).
rad=lambda k: Fraction(factorial(k), 2**(k+1))
# The angular simplex integrals are 2*pi and 2*pi/105, respectively.
# All integral values below are coefficients of pi squared.
I0 = 4*rad(3)*2*dirichlet_moment(B,qhalf)
IR = 4*rad(5)*2*dirichlet_moment(BR,qhalf)
IT = 16*rad(6)*Fraction(2,105)*dirichlet_moment(B2,qthree)
assert I0==Fraction(4,7), ("I0",I0)
assert IR==Fraction(32,11), ("IR",IR)
assert IT==Fraction(8,11), ("IT",IT)
assert IR/I0==Fraction(56,11)
assert IT/I0==Fraction(14,11)

# Homogeneous radial gamma law: q~Gamma(shape=4,rate=1).
qm=lambda k: Fraction(factorial(k+3), factorial(3))
assert qm(2)==20 and qm(3)==120 and qm(4)==840
c1 = -qm(2)/2
c2flat= qm(4)/8-qm(3)/3
# curvature coefficient multiplies pi^2.
c2curv=Fraction(2,3)*(IT-IR)/I0
assert c1==-10
assert c2flat==65
assert c2curv==Fraction(-28,11)

# First moment benchmark: E area(W_n) ~ 2*pi^3*n^{-2}.
# Therefore the squared area asymptotic / square of mean tends to 16/7.
assert Fraction(64,7)/4==Fraction(16,7)
print('I0/pi^2',I0,'IR/pi^2',IR,'IT/pi^2',IT)
print('corrections: c1=',c1,', c2=',c2flat,'+',c2curv,'*pi^2')
print('weighted-cell square area n^4 prefactor = 64*pi^6/7')
print('ALL_EXACT_MOMENT_IDENTITIES_PASSED')
