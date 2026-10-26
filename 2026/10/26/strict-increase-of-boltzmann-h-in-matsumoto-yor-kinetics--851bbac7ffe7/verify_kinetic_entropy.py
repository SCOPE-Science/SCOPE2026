"""Deterministic independent checks for the Matsumoto--Yor collision entropy identity.

Requires Python 3, numpy, scipy, sympy. The mathematical sign theorem
rests on the accompanying proof, not on these finite checks.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import roots_hermitenorm

x, y, p, c = sp.symbols('x y p c', positive=True)
u = 1/(x+y)
v = y/(x*(x+y))
# Map, involution, and its nonconstant Jacobian.
assert sp.simplify(u.subs({x:u,y:v}, simultaneous=True)-x) == 0
assert sp.simplify(v.subs({x:u,y:v}, simultaneous=True)-y) == 0
jac = sp.simplify(-sp.det(sp.Matrix([u,v]).jacobian([x,y])))
assert sp.simplify(jac*x*x*(x+y)**2 - 1) == 0
energy = x+y+1/x
assert sp.simplify((u+v+1/u)-energy) == 0

# The invariant product density is x^(-p-1) y^(p-1) exp[-c E/2].
monomial = x**(-p-1)*y**(p-1)
assert sp.simplify(sp.expand_power_base(
    (u**(-p-1)*v**(p-1)*jac)/monomial,force=True)-1)==0

# Gauss--Hermite integration for Y=Z^2/2, Z standard normal,
# so Y ~ Gamma(shape=1/2, scale=1). X ~ IG(mean=1, shape=2).
z, weights = roots_hermitenorm(128)
w = weights / math.sqrt(2*math.pi)
ys = z*z/2

def qlogx(t):
    return 2.0 - 0.5*t - 2.0*math.cosh(t) - 0.5*math.log(math.pi)

def expectation_x(fn):
    return quad(lambda t: math.exp(qlogx(t))*fn(math.exp(t)),
                -12, 12, epsabs=2e-10, epsrel=2e-10, limit=300)[0]

def m(xv):
    return -2*math.log(xv) -2*np.dot(w, np.log(xv+ys))

assert abs(expectation_x(lambda xx: 1.0)-1.0) < 1e-9
eta = expectation_x(lambda xx: xx/(1+xx))
h = lambda xx: xx/(1+xx)-eta
expected_log_j = expectation_x(m)
assert abs(expected_log_j) < 5e-6, expected_log_j
B = -expectation_x(lambda xx: h(xx)*m(xx))
assert 0.31 < B < 0.34, B
assert all(m(xv) > m(xv*1.2) for xv in [0.01,0.05,0.2,1,4,20])

def joint_check(eps):
    # First expression uses the product collision generator directly.
    def direct(xx):
        xu = 1/(xx+ys)
        yv = ys/(xx*(xx+ys))
        e0 = xx+ys+1/xx
        e1 = xu+yv+1/xu
        assert np.max(np.abs(e0-e1)) < 3e-9
        logqx = -1.5*math.log(xx) - (xx+1/xx)
        logqy = -0.5*np.log(ys) -ys
        logqu = -1.5*np.log(xu) -(xu+1/xu)
        logqv = -0.5*np.log(yv)-yv
        log_ratio = logqu+logqv-logqx-logqy
        log_ratio += np.log1p(eps*h(xu)) - math.log1p(eps*h(xx))
        return (1+eps*h(xx))*np.dot(w,log_ratio)
    derivative_direct=expectation_x(direct)
    # Second expression uses the exact KL identity.
    def entropy_kl(xx):
        xu = 1/(xx+ys)
        term = math.log1p(eps*h(xx))-np.log1p(eps*h(xu))
        return (1+eps*h(xx))*np.dot(w,term)
    KL = expectation_x(entropy_kl)
    derivative_identity=eps*B -KL-eps*expected_log_j
    assert abs(derivative_direct-derivative_identity) < 2e-7, (
         eps,derivative_direct,derivative_identity)
    assert KL>0 and KL<8*eps*eps
    assert derivative_direct>0
    return derivative_direct, -KL

results = [(e, *joint_check(e)) for e in (0.002, 0.01, 0.05)]
print('symbolic invariance and involution: PASS')
print('reference equilibrium normalization: PASS')
print('B (linear Boltzmann-H production):',format(B,'.12f'))
print('E_q[log Jacobian], integration error proxy:',format(expected_log_j,'.9g'))
for eps, hprime, fprime in results:
    print(f'epsilon={eps:g}; unweighted H derivative={hprime:.10g}; relative entropy derivative={fprime:.10g}')
print('all checks PASS')
