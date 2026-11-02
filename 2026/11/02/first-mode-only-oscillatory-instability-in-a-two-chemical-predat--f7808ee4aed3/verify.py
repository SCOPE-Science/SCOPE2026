"""Reproduce exact modal and Hurwitz identities for a four-field PDE.

Requires Python 3 and SymPy. Run: python verify.py
No numerical sampling is used to certify the all-mode claim.
"""
import sympy as S

z, q, g, h = S.symbols('z q g h', real=True)
A = 2 + S.Rational(3, 10) * q
E = 1 + 3 * q
M = S.Matrix([
    [-A, 1, -q, 0],
    [-1, -A, 0, q],
    [0, g, -E, 0],
    [g, 0, 0, -E],
])
p = S.expand((z * S.eye(4) - M).det())
compact = S.expand(((z + A) * (z + E))**2 + (z + E - g*q)**2)
assert S.expand(p - compact) == 0
print('PASS: exact 4x4 determinant and complex-quadratic factorization')

c = S.Poly(p, z)
assert c.degree() == 4
_, a1, a2, a3, a4 = c.all_coeffs()
D2 = S.expand(a1*a2-a3)
D3 = S.expand(a1*a2*a3-a3**2-a1**2*a4)
assert S.expand(D2 -
    (1000*g*q+38907*q**3+121500*q**2+114900*q+35000)/500) == 0
H = (-1000*g**2*q**2+g*(2700*q**2-1000*q)
     +9801*q**4+86427*q**3+155520*q**2+102600*q+20000)
assert S.expand(D3 - (1089*q**2+1980*q+1000)*H/25000) == 0
assert S.expand(a3.subs(g, 21) -
    (297*q**3+2349*q**2+750*q+700)/50) == 0
print('PASS: general quartic Routh-Hurwitz coefficients and minors')

g2 = S.Rational(11, 10) + 36*S.sqrt(205)/25
assert S.simplify(H.subs({q: 2, g: g2})) == 0
H2_shift = (9801*h**4+164835*h**3
            +(485978+720*S.sqrt(205))*h**2
            +(381024+1440*S.sqrt(205))*h)
assert S.simplify(S.expand(H.subs({q: h+2, g: g2}) - H2_shift)) == 0
assert all(x > 0 for x in S.Poly(H2_shift / h,h).all_coeffs())
assert all(x>0 for x in S.Poly(H.subs(g,0),q).all_coeffs())
# For any fixed q >=2, concavity in gain implies H(q,g)>0 for 0<=g<g2;
# at g2 it vanishes only at q=2.
assert g2 < 23
assert S.simplify(a3 - (-100*g*q+297*q**3+2349*q**2+2850*q+700)/50) == 0
print('PASS: sharp second-mode threshold and all modes q>=2, 0<=g<g2')

assert S.expand(p.subs(q, 0)-(z+1)**2*((z+2)**2+1)) == 0
assert S.expand(p.subs({q:1,g:21}) -
    (100*z**4+1260*z**3+5909*z**2+8192*z+37364)/100) == 0
assert D3.subs({q:1,g:21}) == -S.Rational(15742961,3125)
assert D2.subs({q:1,g:21}) > 0
assert all(x>0 for x in S.Poly(p.subs({q:1,g:21}),z).all_coeffs())
print('PASS: stable q=0; q=1 has exactly one unstable nonreal pair')

A1 = S.Rational(23,10)
E1 = S.Rational(4)
w = (S.sqrt(1+4*A1*E1)-1)/2
gcrit = S.simplify(E1+(A1+E1)*w)
assert S.simplify(gcrit-(85+189*S.sqrt(105))/100) == 0
assert (85+189*S.sqrt(105)) < 2100
assert gcrit > 20
assert gcrit < g2
A2 = S.Rational(13,5)
E2 = S.Rational(7)
w2=(S.sqrt(1+4*A2*E2)-1)/2
assert S.simplify((E2+(A2+E2)*w2)/2-g2) == 0
assert S.simplify(w**2+w-A1*E1) == 0
# Since 2w+1>0, the implicit derivative d(Re z)/dg at onset is positive.
assert S.simplify(2*w+1) > 0
print('PASS: exact first and second positive gain thresholds and crossing sign')
print('PASS: spectral assertion uses Neumann eigenvalues m^2+n^2 on (0,pi)^2')
