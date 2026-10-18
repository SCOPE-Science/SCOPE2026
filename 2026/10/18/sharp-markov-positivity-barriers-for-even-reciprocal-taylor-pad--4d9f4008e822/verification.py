#!/usr/bin/env python3
"""Exact finite algebraic checks for the reciprocal-Taylor Padé positivity theorem.
Requires SymPy 1.12 or newer. These checks complement, not replace, the proof.
"""
from math import factorial
import sympy as sp

h, z, t = sp.symbols('h z t')
q4 = sum((-z)**j / sp.factorial(j) for j in range(5))
r4 = 1 / q4
D = h**4 + 4*h**3 + 12*h**2 + 24*h + 24
assert sp.cancel(r4.subs(z, -h) - 24/D) == 0

# A unit-rate pure-birth generator on states 1,...,7, with 7 absorbing.
Q = sp.zeros(7)
for i in range(6):
    Q[i,i] = -1
    Q[i,i+1] = 1
assert Q*sp.ones(7, 1) == sp.zeros(7, 1)

c = [sp.factor(h**j * sp.diff(r4,z,j).subs(z,-h) / sp.factorial(j))
     for j in range(6)]
g = [None] + [sp.factor(1 - sum(c[:d])) for d in range(1,7)]
# Every transient coefficient, and every absorbing probability from distance <=5,
# has a positive polynomial numerator over a positive denominator.
positive_certificate_count = 0
for f in c + g[1:6]:
    num, den = sp.fraction(sp.factor(f))
    num_poly = sp.Poly(num, h)
    den_poly = sp.Poly(den, h)
    assert all(v >= 0 for v in num_poly.all_coeffs())
    assert all(v >= 0 for v in den_poly.all_coeffs())
    assert num_poly.eval(1) > 0 and den_poly.eval(1) > 0
    positive_certificate_count += 1

P = (h**18 + 24*h**17 + 312*h**16 + 2864*h**15
     + 17520*h**14 + 72960*h**13 + 201664*h**12
     + 319104*h**11 + 41472*h**10 - 1113600*h**9
     - 2488320*h**8 - 1078272*h**7 + 6552576*h**6
     + 19243008*h**5 + 28200960*h**4 + 25436160*h**3
     + 12939264*h**2 - 2654208)
assert sp.cancel(g[6] - h**6 * P / D**6) == 0
assert P.subs(h, 0) < 0 and P.subs(h, 1) > 0

# Descartes certificate: on 0<h<1, h=t/(1+t) gives exactly
# one sign change; on h>=1, P(1+t) has all positive coefficients.
polyP = sp.Poly(P, h)
low = sp.Poly(sp.expand(sum(coeff*t**k*(1+t)**(18-k)
                            for (k,),coeff in polyP.terms())), t)
high = sp.Poly(sp.expand(P.subs(h,t+1)), t)
low_signs = [sp.sign(a) for a in low.all_coeffs()]
assert all(s > 0 for s in low_signs[:12])
assert all(s < 0 for s in low_signs[12:])
assert len(low_signs) == 19
assert all(a > 0 for a in high.all_coeffs())
assert P.subs(h, sp.Rational(32606,100000)) < 0
assert P.subs(h, sp.Rational(32607,100000)) > 0

# Independent direct rational matrix inversion at two witness steps.
for x, expected in [(sp.Rational(1,10),-1), (sp.Rational(1,2),1)]:
    H = x*Q
    F = (sp.eye(7)-H+H**2/2-H**3/6+H**4/24).inv()
    assert F*sp.ones(7,1) == sp.ones(7,1)
    assert sp.cancel(F[0,6] - g[6].subs(h,x)) == 0
    assert sp.sign(F[0,6]) == expected
    for i in range(7):
        for j in range(7):
            if j < i:
                assert F[i,j] == 0
            elif j < 6:
                assert sp.cancel(F[i,j] - c[j-i].subs(h,x)) == 0
            elif i == 6:
                assert F[i,6] == 1
            elif i >= 1:
                assert sp.cancel(F[i,6] - g[6-i].subs(h,x)) == 0

# Check general even-order formal-coefficient identities in finite instances.
for m in range(2,20,2):
    q = [sp.Rational((-1)**j, factorial(j)) for j in range(m+1)]
    a = [sp.Integer(1)]
    for k in range(1,m+3):
        a.append(sp.expand(-sum(q[j]*a[k-j] for j in range(1,min(k,m)+1))))
    assert a[:m+1] == [sp.Rational(1, factorial(j)) for j in range(m+1)]
    assert a[m+1] == 0
    assert a[m+2] == -sp.Rational(2*(m+1), factorial(m+2))

print('VERIFY_OK: 11 positive-numerator certificates, exact root-sign certificates,')
print('7-state rational matrix evaluations at two steps, and 9 even-order series checks')
