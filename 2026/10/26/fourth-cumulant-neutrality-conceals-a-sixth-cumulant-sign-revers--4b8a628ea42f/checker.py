"""Independent symbolic and finite-time checks for a three-speed intermittent particle.

Requires Python 3 with sympy, numpy and scipy. The limiting theorems in the
accompanying proof are analytical; these tests are finite confirmations.
"""
from math import sqrt
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.optimize import brentq

N_CHECKS = 0

def check(statement):
    global N_CHECKS
    assert bool(statement)
    N_CHECKS += 1

# Independent characteristic-polynomial calculation for the tilted Markov generator.
a, b, h, v, q, z = sp.symbols('a b h v q z', real=True)
ell=sp.Symbol('ell')
K = sp.Matrix([[v*q-a-h, h, b/2], [h, -v*q-a-h, b/2], [a, a, -b]])
char = K.charpoly(ell).as_expr()
target = ell*(ell+a+b)*(ell+a+2*h)-(ell+b)*(v*q)**2
check(sp.factor(char-target) == 0)

# Perturbative coefficients outside fourth-cumulant neutrality.
c = a+2*h
L = a+b+c
A = b/(c*(a+b))
B = b*(a*c-b*(a+b))/(c**3*(a+b)**3)
f = lambda u, w: sp.expand(u*(u+a+b)*(u+c)-(u+b)*w)
series = A*z+B*z**2
check(sp.factor(f(series,z).coeff(z,1)) == 0)
check(sp.factor(f(series,z).coeff(z,2)) == 0)

# At the zero-fourth-cumulant boundary, the characteristic equation reduces
# to u^3+L u^2+b L u=(u+b) z. Check all coefficients through order four.
L0, b0 = sp.symbols('L0 b0', positive=True)
u = z/L0-z**3/(b0*L0**4)+z**4/(b0**2*L0**5)
f0 = sp.expand(u**3+L0*u**2+b0*L0*u-(u+b0)*z)
for degree in range(1,5):
    check(sp.factor(f0.coeff(z, degree)) == 0)

p = sp.symbols('p', positive=True)
threshold = (15+sp.sqrt(105))/60
check(sp.simplify(1-15*threshold+30*threshold**2) == 0)
b_ratio = (13+sp.sqrt(105))/32
h_ratio = (-167+29*sp.sqrt(105))/1024
check(sp.simplify(threshold-b_ratio/(1+b_ratio)) == 0)
check(sp.simplify((b_ratio**2+b_ratio-1)/2-h_ratio) == 0)

# Finite-time moments from an ODE independent of the tilted-eigenvalue expansion:
# M_n' = Q M_n + n diag(v,-v,0) M_{n-1} + n(n-1) D M_{n-2}.
def finite_moments(a, b, h, v, D, t, order=8):
    Q = np.array([[-a-h, h, b/2], [h, -a-h, b/2], [a, a, -b]], float)
    V = np.diag([v,-v,0.0]); big = np.zeros((3*(order+1),3*(order+1)))
    for n in range(order+1):
        big[3*n:3*n+3, 3*n:3*n+3] = Q
        if n >= 1: big[3*n:3*n+3,3*(n-1):3*n] = n*V
        if n >= 2: big[3*n:3*n+3,3*(n-2):3*(n-1)] = n*(n-1)*D*np.eye(3)
    initial = np.zeros(3*(order+1))
    initial[:3] = [b/(2*(a+b)), b/(2*(a+b)), a/(a+b)]
    res = expm(big*t)@initial
    return [float(sum(res[3*n:3*n+3])) for n in range(order+1)]

def cumulants(m):
    m2,m4,m6,m8=(m[2],m[4],m[6],m[8])
    return (m4-3*m2**2, m6-15*m4*m2+30*m2**3,
            m8-28*m6*m2-35*m4**2+420*m4*m2**2-630*m2**4)

# All parameter sets lie precisely on the critical surface. Finite-time
# cumulant/T must approach the analytically derived sixth and eighth slopes.
for aa, hh, vv, DD in [(1.,.5,1.,.2),(2.,.4,1.1,0.),(.8,1.2,.75,.15),(1.5,0.,1.2,.1)]:
    bb=(sqrt(5*aa*aa+8*aa*hh)-aa)/2
    LL=aa+bb+aa+2*hh
    predicted6=-720*vv**6/(bb*LL**4)
    predicted8=40320*vv**8/(bb**2*LL**5)
    check(abs(aa*(aa+2*hh)-bb*(aa+bb)) < 1e-12)
    check(predicted6 < 0 and predicted8 > 0)
    m = finite_moments(aa,bb,hh,vv,DD,150.0)
    C4,C6,C8 = cumulants(m)
    check(abs(C4)/150 < 0.01*vv**4 + 0.01)
    check(abs(C6/150-predicted6) < 0.12*abs(predicted6)+0.015)
    check(abs(C8/150-predicted8) < 0.13*abs(predicted8)+0.05)

# At a=b=1, h=1/2, stationary sixth-cumulant growth is negative, whereas
# the very short-time sixth cumulant is positive. There is a genuine zero.
short = cumulants(finite_moments(1.,1.,.5,1.,0.2,.3))[1]
late = cumulants(finite_moments(1.,1.,.5,1.,0.2,2.0))[1]
check(short > 0)
check(late < 0)
root = brentq(lambda t:cumulants(finite_moments(1.,1.,.5,1.,0.2,t))[1], .3, 2.0)
check(0.85<root<0.95)
print(f'PASS: {N_CHECKS} symbolic/numerical checks; sample sixth-cumulant zero at t={root:.9f}')
