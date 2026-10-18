"""Standalone exact-algebra checks of an environmental-feedback game theorem.

Requirements: Python 3 and SymPy. Run with: python verification.py
The analytic proof, not these finite tests, establishes the theorem.
"""
from fractions import Fraction
import random
import sympy as sp


def check(assertion, message):
    assert bool(assertion), message


x, y, B, C, A, s, z = sp.symbols('x y B C A s z', real=True)
X, Y, n1, n2, n12 = sp.symbols('X Y n1 n2 n12', real=True)
q = x * (1 - x)
r = y * (1 - y)
kappa = (2 * A - B * (x + y)) / C
h = kappa - s

# Full five-component dynamics obtained from payoff differences
# G(n,p)=A-B*p-C*n at balanced within/between-community mixing.
F = sp.Matrix([
    X*(1-X)*(A - B*(X+Y)/2 - C*(n1+n12)/2),
    Y*(1-Y)*(A - B*(X+Y)/2 - C*(n2+n12)/2),
    n1*(1-n1)*(X/x - 1),
    n2*(1-n2)*(Y/y - 1),
    n12*(1-n12)*((X+Y)/(x+y) - 1),
])
fixed = {X:x, Y:y, n1:h, n2:h, n12:s}
for i, expr in enumerate(F.subs(fixed)):
    check(sp.cancel(expr)==0, 'equilibrium equation '+str(i))

# Exact log-odds first integral at the feedback resonance.
Hd = (F[4]/(n12*(1-n12))
      - x/(x+y)*F[2]/(n1*(1-n1))
      - y/(x+y)*F[3]/(n2*(1-n2)))
check(sp.cancel(Hd)==0, 'log-odds conservation')

w = h*(1-h)
v = s*(1-s)
J = sp.simplify(F.jacobian([X,Y,n1,n2,n12]).subs(fixed))
a = B/2
b = C/2
Jexpected = sp.Matrix([
    [-a*q, -a*q, -b*q, 0, -b*q],
    [-a*r, -a*r, 0, -b*r, -b*r],
    [w/x, 0, 0, 0, 0],
    [0, w/y, 0, 0, 0],
    [v/(x+y), v/(x+y), 0, 0, 0],
])
for i in range(5):
    for j in range(5):
        check(sp.cancel(J[i,j]-Jexpected[i,j]) == 0, 'Jacobian '+str((i,j)))

# Characteristic polynomial and exact quartic Routh-Hurwitz minors
# in independent positive algebraic quantities.
alpha,beta,P,Q,U,V,W = sp.symbols('alpha beta P Q U V W', real=True)
L = sp.symbols('lam')
M = sp.Matrix([
    [L*L+alpha*P*L+beta*P*(U+W), alpha*P*L+beta*P*W],
    [alpha*Q*L+beta*Q*W, L*L+alpha*Q*L+beta*Q*(V+W)],
])
a3 = alpha*(P+Q)
a2 = beta*(P*(U+W)+Q*(V+W))
a1 = alpha*beta*P*Q*(U+V)
a0 = beta**2*P*Q*(U*V+W*(U+V))
poly = L**4+a3*L**3+a2*L**2+a1*L+a0
check(sp.expand(M.det()-poly)==0, 'block characteristic identity')
H2 = sp.factor(a3*a2-a1)
H3 = sp.factor(a3*a2*a1-a1*a1-a3*a3*a0)
check(sp.expand(H2-alpha*beta*(P*P*U+Q*Q*V+(P+Q)**2*W))==0, 'Hurwitz minor 2')
check(sp.expand(H3-alpha**2*beta**2*P*Q*(P*U-Q*V)**2)==0, 'Hurwitz minor 3')
check(sp.cancel(q*(w/x)-r*(w/y) -w*(y-x))==0, 'sensitivity contrast')

# In the equal-feedback case the undamped antisymmetric factor is exact.
t, u0, v0 = sp.symbols('t u0 v0')
sympoly=sp.expand(poly.subs({P:t,Q:t,U:u0,V:u0,W:v0}))
symfactor=(L**2+2*alpha*t*L+beta*t*(u0+2*v0))*(L**2+beta*t*u0)
check(sp.expand(sympoly-symfactor)==0, 'equal-community neutral oscillatory factor')

# Direct finite-rational, five-by-five determinant checks.
examples = [
    (sp.Rational(1,2),sp.Rational(1,4),sp.Integer(2),sp.Integer(1),sp.Integer(3),sp.Rational(1,2)),
    (sp.Rational(1,3),sp.Rational(2,3),sp.Rational(5,2),sp.Rational(1,2),sp.Integer(4),sp.Rational(1,2)),
    (sp.Rational(1,2),sp.Rational(1,2),sp.Integer(2),sp.Integer(1),sp.Integer(3),sp.Rational(1,2)),
]
rng = random.Random(871355)
for _ in range(24):
    x0=sp.Rational(rng.randint(1,9),10)
    y0=sp.Rational(rng.randint(1,9),10)
    B0=sp.Rational(rng.randint(1,9),10)
    A0=B0+sp.Rational(rng.randint(1,9),10)
    C0=A0+sp.Rational(rng.randint(1,9),10)
    s0=(2*A0-B0*(x0+y0))/(2*C0)
    examples.append((x0,y0,A0,B0,C0,s0))
for k,(xx,yy,aa,bb,cc,ss) in enumerate(examples):
    vals={x:xx,y:yy,A:aa,B:bb,C:cc,s:ss}
    JJ=J.subs(vals)
    p5=sp.Poly(JJ.charpoly(L).as_expr(),L)
    pred=sp.Poly((L*poly).subs({
        alpha:bb/2,beta:cc/2,P:xx*(1-xx),Q:yy*(1-yy),
        U:(kappa.subs(vals)-ss)*(1-(kappa.subs(vals)-ss))/xx,
        V:(kappa.subs(vals)-ss)*(1-(kappa.subs(vals)-ss))/yy,
        W:ss*(1-ss)/(xx+yy),
    }),L)
    check(p5==pred,'direct characteristic determinant, case '+str(k))
    if xx!=yy:
        import numpy as np
        ev=np.linalg.eigvals(np.array(JJ,dtype=float))
        check(sum(abs(ev)<1e-8)==1,'one simple neutral eigenvalue, case '+str(k))
        check(all(vv.real < -1e-11 for vv in ev if abs(vv)>1e-8),
              'strict transverse damping, case '+str(k))

print('PASS: exact equilibrium, conservation, 25 Jacobian entries,')
print('quartic determinant, two Hurwitz identities, symmetric factor,')
print(str(len(examples))+' independent full 5x5 characteristic-polynomial cases,')
print('and sampled transverse eigenvalue signs.')
