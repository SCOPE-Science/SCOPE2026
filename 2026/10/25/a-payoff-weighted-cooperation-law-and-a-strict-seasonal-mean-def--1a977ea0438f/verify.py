"""Symbolic and numerical checks for the payoff-weighted cooperation law.

Run: python verify.py
Dependencies: sympy, numpy, scipy.
The analytical results and non-vacuity proof are in RESULT.md.
"""
from fractions import Fraction
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root

# The feedback payoff balance is symbolic and independent of the payoff law.
x, r, alpha, beta, eps, theta, C, D = sp.symbols(
    'x r alpha beta eps theta C D', real=True
)
fx = x * (1-x) * (C-D)
fr = eps * (r-alpha)*(beta-r)*(-x*C + theta*(1-x)*D)
Hprime = fr/(eps*(r-alpha)*(beta-r)) + fx/(1-x)
assert sp.simplify(Hprime-(theta-(1+theta)*x)*D) == 0
print('Generic payoff coboundary identity: PASS')

# The defector payoff is exactly independent of seasonal synergy for N=2.
w, rd = sp.symbols('w rd', real=True)
for N in range(2, 9):
    # Binomially averaged cumulative cooperation payoff for the defector.
    B = 0
    for k in range(1, N):
        geometric_sum = sum(w**j for j in range(k))
        B += sp.binomial(N-1, k)*x**k*(1-x)**(N-1-k)*geometric_sum
    target = sum(
        sp.binomial(N-1, j)*x**j*(w-1)**(j-1)
        for j in range(1,N)
    )
    assert sp.simplify(B-target) == 0
    if N == 2:
        assert sp.simplify(rd*B/N-rd*x/2) == 0
    if N >= 3:
        assert sp.simplify(sp.diff(B,w)).subs({x:sp.Rational(1,2),w:1}) > 0
print('Exact binomial payoff reductions N=2..8: PASS')

# An exact interior equilibrium and its Hurwitz Jacobian.
a = sp.Rational(6,5)
b = sp.Rational(9,5)
e = sp.Integer(10)
co = r*(1+w*x)/2 - 1
de = x/2
field = sp.Matrix([
    x*(1-x)*(co-de),
    e*(r-a)*(b-r)*(-x*co+(1-x)*de),
])
base = {x:sp.Rational(1,2),r:sp.Rational(5,3),w:1}
assert field.subs(base) == sp.zeros(2,1)
J = field.jacobian((x,r)).subs(base)
B = field.diff(w).subs(base)
assert J == sp.Matrix([[sp.Rational(1,12),sp.Rational(3,16)],
                       [-sp.Rational(56,135),-sp.Rational(7,30)]])
assert B == sp.Matrix([sp.Rational(5,48),-sp.Rational(7,54)])
assert sp.trace(J)==-sp.Rational(3,20)
assert J.det()==sp.Rational(7,120)
print('Exact equilibrium, Jacobian, and strict Hurwitz test: PASS')

# First harmonic x response to w(t)=1+delta cos(t).
frequency=sp.I
transfer=(frequency*sp.eye(2)-J).inv()*B
amp2=sp.simplify(transfer[0]*sp.conjugate(transfer[0]))
assert amp2==sp.Rational(625,52372)
print('Exact leading mean-deficit coefficient: ',amp2)

# Numerically find the small seasonal branch by Poincare shooting.
T=2*np.pi
for delta in (0.04,0.08,0.12,-0.12):
    def f(t,z):
        x0, r0 = z
        wt = 1 + delta*np.cos(t)
        pc = r0*(1+wt*x0)/2-1
        pd = x0/2
        return [x0*(1-x0)*(pc-pd),
                10*(r0-1.2)*(1.8-r0)*(-x0*pc+(1-x0)*pd)]
    def orbit(z, dense=False):
        return solve_ivp(f,(0,T),z,rtol=3e-12,atol=5e-14,
                         dense_output=dense,max_step=0.015)
    sol=root(lambda z: orbit(z).y[:,-1]-z,[0.5,5/3],tol=1e-10)
    assert np.linalg.norm(orbit(sol.x).y[:,-1]-sol.x,np.inf)<1e-10
    dense=orbit(sol.x,dense=True)
    times=np.linspace(0,T,6001)
    xx,rr=dense.sol(times)
    assert np.min(xx)>0 and np.max(xx)<1
    assert np.min(rr)>1.2 and np.max(rr)<1.8
    avgx=np.trapezoid(xx,times)/T
    varx=np.trapezoid((xx-avgx)**2,times)/T
    assert .5-avgx>0
    assert max(abs(varx-avgx*(.5-avgx)),abs(np.trapezoid((.5-xx)*xx,times)/T))<2e-10
    H=lambda xx,rr: np.log((rr-1.2)/(1.8-rr))/(10*.6)-np.log(1-xx)
    assert abs(H(xx[-1],rr[-1])-H(xx[0],rr[0]))<2e-9
    if abs(delta)<=.08:
        assert abs((.5-avgx)/delta**2-float(amp2))<0.0003
    print(f'delta={delta:+.2f} initial={sol.x} mean_x={avgx:.12f} '
          f'variance={varx:.12g} gap={(0.5-avgx):.12g} PASS')
print('All checks passed. Computations corroborate but do not replace proof.')
