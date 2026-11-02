#!/usr/bin/env python3
"""Independent symbolic and numerical checks for alternating-step AB3 on scalar decay.

The analytic proof is in RESULT.md; finite checks are supplementary evidence.
"""
import random
import sympy as sp
import numpy as np

x, y, z = sp.symbols('x y z', positive=True)
s, q = sp.symbols('s q', positive=True)


def transfer(cur, prev):
    nodes = (sp.Integer(0), -prev, -cur-prev)
    weights = []
    for i, node in enumerate(nodes):
        basis = sp.prod((z-nodes[j])/(node-nodes[j]) for j in range(3) if j != i)
        weights.append(sp.integrate(basis, (z, 0, cur)))
    return sp.Matrix([
        [1-weights[0], -weights[1], -weights[2]],
        [1, 0, 0], [0, 1, 0],
    ])

T_xy = transfer(x, y)
expected = sp.Matrix([
    [1-x*(5*x*x+12*x*y+6*y*y)/(6*y*(x+y)),
     x*(5*x+3*y)/(6*y), -x*(2*x+3*y)/(6*(x+y))],
    [1,0,0], [0,1,0],
])
assert all(sp.cancel(v) == 0 for v in T_xy-expected)
M = transfer(y, x)*T_xy
A = 1-(2-q)*s/3+(30+12*q+q*q)*s*s/36
B = (1+q)*s/3+q*(3+q)*s*s/18
C = q*(6+q)*s*s/36
subst = {s:x+y, q:x*y/(x+y)**2}
coeff = M.charpoly().all_coeffs()
assert all(sp.cancel(actual-expected_expr.subs(subst)) == 0 for actual, expected_expr in zip(coeff,[sp.Integer(1),-A,B,-C]))
assert sp.simplify((1-A+B-C)-s*(1-(5+2*q)*s/6)) == 0
assert sp.simplify((A-C)-(1-(2-q)*s/3+(5+q)*s*s/6)) == 0
assert sp.factor(1-B+A*C-C*C) != 0

# Exact recurrence compatibility with the standard constant-step AB3 method.
const = T_xy.subs({x:s, y:s})
assert sp.cancel(const[0,0]-(1-23*s/12)) == 0
assert sp.cancel(const[0,1]-4*s/3) == 0
assert sp.cancel(const[0,2]+5*s/12) == 0

# Exact threshold tests at rational ratios and positive steps.
for r in [sp.Rational(k,5) for k in range(1,51)]:
    qq = r/(1+r)**2
    ss = 6/(5+2*qq)
    poly = sp.Poly(z**3-A*z**2+B*z-C,z)
    assert sp.cancel(poly.eval(1).subs({s:ss,q:qq})) == 0

# Independent Vandermonde integration and numerical root tests.
rng = random.Random(43931)
checks = 0
for _ in range(1000):
    r = 10**rng.uniform(-2.5,2.5)
    ss = rng.uniform(0.03,1.45)
    aa,bb = ss/(1+r), ss*r/(1+r)
    def independent_transfer(cur,prev):
        nd=np.array([0.,-prev,-prev-cur],dtype=float)
        V=np.stack([nd**k for k in range(3)])
        integrals=np.array([cur**(k+1)/(k+1) for k in range(3)])
        w=np.linalg.solve(V,integrals)
        return np.array([[1-w[0],-w[1],-w[2]], [1.,0.,0.],[0.,1.,0.]])
    mon=independent_transfer(bb,aa)@independent_transfer(aa,bb)
    rho=max(abs(np.linalg.eigvals(mon)))
    qq=aa*bb/ss**2
    expected_stable=ss < 6/(5+2*qq)
    if abs(ss-6/(5+2*qq)) > 0.002:
        assert (rho<1) == expected_stable, (r,ss,rho,expected_stable)
        checks+=1

# Transient coefficient and singular-value limit under severe step contrast.
for ss in (sp.Rational(1,2),sp.Rational(1),sp.Rational(11,10)):
    r=sp.symbols('r',positive=True)
    cur=ss*r/(1+r); prev=ss/(1+r)
    big=expected.subs({x:cur,y:prev})
    target=sp.Matrix([[-5*ss/6,5*ss/6,0],[0,0,0],[0,0,0]])
    assert all(sp.limit(big[i,j]/r,r,sp.oo)==target[i,j]
               for i in range(3) for j in range(3))
    assert sp.simplify(big[0,1]-ss*r*(5*r+3)/(6*(1+r))) == 0

print('PASS symbolic coefficient/characteristic identities; 50 rational boundaries;',
      checks,'independent numerical stability checks; 3 transient asymptotic certificates')
