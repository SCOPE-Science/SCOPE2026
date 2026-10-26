#!/usr/bin/env python3
"""Exact symbolic checks for random edge-order Markov splitting.

Requires Python 3 and sympy. This checker verifies identities and bounded finite
rational tests; the written proof handles all positive real steps.
"""
from itertools import permutations
import sympy as s

q = s.symbols('q', positive=True, real=True)
I = s.eye(3)
u = s.ones(3, 1) / 3
Pi = I - s.ones(3) / 3
Es = []
for j in range(3):
    E = I.copy()
    E[j, j] = q
    E[(j + 1) % 3, j] = 1 - q
    Es.append(E)

products = []
for perm in permutations(range(3)):
    P = I.copy()
    for j in perm:
        P = Es[j] * P
    products.append((perm, P.applyfunc(s.factor)))

D = q**5 - 3*q**4 + 4*q**3 - q**2 + 6*q + 2
V = (1 - q)**3 * (q**2 - 3*q + 4)/(3*D)
Bmin = 2*(1 - q)**2/(3*(q + 2)**2)
Bmax = 2*(1 - q)**2/(3*(2*q + 1)**2)
F = q**3 * (1-q)**2 + 2*q**2 + 8*q - 4
checks = 0

def ck(expr):
    global checks
    if isinstance(expr, s.MatrixBase):
        for el in expr:
            ck(el)
        return
    assert s.cancel(expr) == 0, s.factor(expr)
    checks += 1

for j, E in enumerate(Es):
    ck(s.trace(E) - (2 + q))
    for x in (s.ones(1, 3) * E - s.ones(1, 3)):
        ck(x)
    for col in range(3):
        for row in range(3):
            ck(E[row, col] - (q if row == j and col == j else 1-q if row == (j+1)%3 and col == j else int(row == col)))

for perm, P in products:
    for x in (s.ones(1,3) * P - s.ones(1,3)):
        ck(x)

Pbar = (sum((P for _, P in products), s.zeros(3)) / 6).applyfunc(s.factor)
ck(Pbar*u-u)
for i in range(3):
    for j in range(3):
        ck(Pbar[i,j]-Pbar[(i+1)%3,(j+1)%3])

aval = s.factor(sum((s.trace(P*Pi*P.T) for _, P in products))/12)
bval = s.factor(sum(((P*u-u).dot(P*u-u) for _, P in products))/6)
ck(3*aval - (q**6-4*q**5+7*q**4-5*q**3+7*q**2-4*q+1))
ck(9*bval - (1-q)**4*(q**2-3*q+4))
ck((1-aval)-(1-q)*D/3)
ck((1-aval)*V-bval)

x0,x1,x2=s.symbols('x0 x1 x2')
x=s.Matrix([x0,x1,x2])
for perm,P in products:
    sol=s.solve(list(P*x-x)[:2]+[x0+x1+x2-1],[x0,x1,x2],dict=True)
    assert len(sol)==1
    px=x.subs(sol[0])
    squared=s.factor(((px-u).dot(px-u)))
    expected=Bmax if perm in ((0,1,2),(1,2,0),(2,0,1)) else Bmin
    ck(squared-expected)
    ck(P*px-px)

ck(V-Bmin+(1-q)**2*F/((q+2)**2*D))
T=2*q**4-6*q**3+7*q**2+2*q+1
ck(V-Bmax+q*(1-q)**2*T/((1+2*q)**2*D))
ck(s.diff(F,q)-(q**2*(1-q)*(3-5*q)+4*q+8))
ck(D-(q**3*(q**2-3*q+4)+q*(6-q)+2))
ck(T-(q**2*(2*q**2-6*q+7)+2*q+1))
ck(s.limit(V,q,0)-s.Rational(2,3))
ck(s.limit(Bmin,q,0)-s.Rational(1,6))
ck(s.limit(V/(1-q)**3,q,1)-s.Rational(2,27))
ck(s.limit(Bmin/(1-q)**2,q,1)-s.Rational(2,27))

# Finite exact-rational checks are supplementary rather than a proof of signs.
for k in range(1,200):
    val=s.Rational(k,200)
    av=s.factor(aval.subs(q,val))
    bv=s.factor(bval.subs(q,val))
    vv=s.factor(V.subs(q,val))
    assert 0 < av < 1 and bv > 0 and vv > 0
    assert vv < Bmax.subs(q,val)
    assert (vv < Bmin.subs(q,val)) == (F.subs(q,val) > 0)
    checks += 5

root=s.nsolve(F,s.Rational(9,20))
assert s.Rational(44,100) < root < s.Rational(45,100)
checks+=1
print(f'PASS: {checks} exact symbolic/rational assertions; q*={root}; h*={-s.log(root).evalf(16)}')
