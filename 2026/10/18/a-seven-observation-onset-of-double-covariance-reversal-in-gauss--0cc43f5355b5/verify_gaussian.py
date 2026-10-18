#!/usr/bin/env python3
"""Exact finite-case checks for Gaussian sign-crossing/quadratic-energy formulas.

Needs Python 3 and SymPy. Prints tested identities; finite computations are not proofs
of the unrestricted statements. No network or external data required.
"""
from fractions import Fraction as F
from math import comb
import sympy as sp

x = sp.symbols('x')
checks = 0

def ck(test, desc):
    global checks
    if not test:
        raise AssertionError(desc)
    checks += 1

def f_matrix(n, r):
    cov = sp.Matrix(n, n, lambda j, k: r ** abs(j-k))
    h = sp.eye(n) - sp.ones(n, n)/n
    total = 0
    for i in range(n-1):
        a, b = cov[:,i], cov[:,i+1]
        total += r*((a.T*h*a)[0]+(b.T*h*b)[0])-2*(a.T*h*b)[0]
    return sp.factor(total)

def f_geom(n, r):
    ss = [sum((r ** abs(j-i) for j in range(n)), sp.S(0)) for i in range(n)]
    q = -2*r*(1-r*r)*sum(((n-d-1)*r**(2*d) for d in range(n-1)), sp.S(0))
    return sp.factor(q - sum((r*(ss[i]**2+ss[i+1]**2)-2*ss[i]*ss[i+1] for i in range(n-1)),sp.S(0))/n)

def f_half(n):
    return (sp.Rational(-3*n*n+31*n-78,1) + sp.Rational(18*n+90,2**n)
            -sp.Rational(4*n+12,4**n))/(3*n)

expected = {
  2: (sp.S(1), sp.S(1)),
  3: (sp.Rational(4,3), 1+x*x),
  4: (sp.Rational(1,2),3-2*x+5*x*x+x**3+3*x**4),
  5: (sp.Rational(4,5),2-3*x+3*x*x+x**3+4*x**4+x**5+2*x**6),
  6: (sp.Rational(1,3),5-12*x+5*x*x-x**3+14*x**4+5*x**5+11*x**6+3*x**7+5*x**8),
}
bernstein = {
  4: [3, sp.Rational(5,2), sp.Rational(17,6),sp.Rational(17,4),10],
  5: [2,sp.Rational(3,2),sp.Rational(6,5),sp.Rational(23,20),sp.Rational(5,3),sp.Rational(7,2),10],
  6: [5,sp.Rational(7,2),sp.Rational(61,28),sp.Rational(57,56),sp.Rational(1,5),sp.Rational(11,56),sp.Rational(9,4),sp.Rational(77,8),35],
}
for n in range(2,11):
    p = f_matrix(n,x)
    # Recheck at independent exact rational parameters, NOT derived from one another.
    for r in [sp.S(0),sp.Rational(1,5),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4)]:
        ck(sp.simplify(p.subs(x,r)-f_geom(n,r)) == 0, f'matrix versus geometric formula n={n},r={r}')
    ck(sp.simplify(p.subs(x,sp.Rational(1,2))-f_half(n))==0, f'closed half n={n}')
    ck(sp.simplify(p.subs(x,0)-sp.Rational(2*(n-1),n))==0, f'zero n={n}')
    ck(sp.simplify(sp.diff(p,x,2).subs(x,1)/2 - sp.Rational(2*(n*n-1),3))==0, f'endpoint coefficient n={n}')
for n,(k,p) in expected.items():
    ck(sp.expand(f_matrix(n,x)-k*(1-x)**2*(1+x)*p)==0, f'factor n={n}')
    if n in bernstein:
        d=sp.degree(p,x)
        a=[sp.expand(p).coeff(x,j) for j in range(d+1)]
        b=[sp.factor(sum(a[j]*sp.Rational(comb(i,j),comb(d,j)) for j in range(i+1))) for i in range(d+1)]
        ck(b==list(map(sp.sympify,bernstein[n])),f'Bernstein coefficients n={n}')
        for v in b: ck(v>0,f'Bernstein positive n={n}')
for n in [11, 20, 40, 100]:
    ck(sp.simplify(f_geom(n,sp.Rational(1,2))-f_half(n))==0, f'extended half geometric n={n}')
for n in range(7,101):
    ck(f_half(n)<0,f'negative at rho=1/2 for n={n}')
for n in range(2,7):
    ck(f_half(n)>0,f'positive at rho=1/2 for n={n}')
print(f'PASS: {checks} exact rational/polynomial assertions.')
print('Example n=7 rho=1/2 numerator:',f_half(7))
print('The all-n sign and limit assertions depend on the written analytic proof.')
