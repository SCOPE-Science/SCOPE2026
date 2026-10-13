#!/usr/bin/env python3
"""Exact symbolic checks for the spin-one, two-qutrit entangling-power theorem.

Requires SymPy (tested with SymPy 1.13 or later). Executes without network access.
"""
import sympy as S

a, b, c = S.symbols('a b c', real=True)
x, y = S.symbols('x y', nonzero=True)
I = S.eye(9)
Sz = S.diag(1, 0, -1)
Sp = S.Matrix([[0, S.sqrt(2), 0], [0, 0, S.sqrt(2)], [0, 0, 0]])
Sm = Sp.T
X = S.kronecker_product(Sz, Sz) + (
    S.kronecker_product(Sp, Sm) + S.kronecker_product(Sm, Sp)
) / 2
P0 = (X + I) * (X - I) / 3
P1 = -(X + 2 * I) * (X - I) / 2
P2 = (X + 2 * I) * (X + I) / 6
for P, rank in [(P0, 1), (P1, 3), (P2, 5)]:
    assert P * P == P and P.T == P and S.trace(P) == rank
assert P0 + P1 + P2 == I
assert P0 * P1 == S.zeros(9) and P0 * P2 == S.zeros(9)
assert P1 * P2 == S.zeros(9)

U = x * P0 + y * P1 + P2
Ud = P0 / x + P1 / y + P2  # U conjugate, for x,y on unit circle
# U[(i,alpha),(j,beta)] with row index 3*i+alpha, col index 3*j+beta.
R = S.Matrix(9, 9, lambda row, col: U[3*(row//3)+(col//3), 3*(row%3)+(col%3)])
Rd = S.Matrix(9, 9, lambda row, col: Ud[3*(row//3)+(col//3), 3*(row%3)+(col%3)])
T = S.Matrix(9, 9, lambda row, col: U[3*(col//3)+(row%3),3*(row//3)+(col%3)])
Td = S.Matrix(9, 9, lambda row, col: Ud[3*(col//3)+(row%3),3*(row//3)+(col%3)])
IR = S.factor(S.trace((R * Rd.T) ** 2))
IT = S.factor(S.trace((T * Td.T) ** 2))
E_laurent = S.factor(S.Rational(10, 16) - (IR + IT) / 144)
E_fourier = (S.Rational(13, 54)
    - S.Rational(65, 648) * (x + 1/x)/2
    - S.Rational(5, 216) * (x/y**2 + y**2/x)/2
    - S.Rational(5, 324) * (x**2 + 1/x**2)/2
    - S.Rational(1, 108) * (x**2/y**2 + y**2/x**2)/2
    - S.Rational(5, 54) * (y**2 + 1/y**2)/2)
assert S.cancel(E_laurent - E_fourier) == 0

E = (S.Rational(13, 54)
    - S.Rational(65, 648)*S.cos(a)
    - S.Rational(5, 216)*S.cos(a - 2*b)
    - S.Rational(5, 324)*S.cos(2*a)
    - S.Rational(1, 108)*S.cos(2*a - 2*b)
    - S.Rational(5, 54)*S.cos(2*b))
A = (S.Integer(166)-65*c-20*c*c)/648
Q = 160*c*c+220*c+349
assert S.simplify(S.expand_trig(A.subs(c,S.cos(a))) -
    (S.Rational(13,54)-S.Rational(65,648)*S.cos(a)-S.Rational(5,324)*S.cos(2*a))) == 0
C_laurent=(20+5*x+2*x**2)*(20+5/x+2/x**2)
assert S.cancel(C_laurent-Q.subs(c,(x+1/x)/2))==0

elimination = 9*(320*c+220)**2-4*(65+40*c)**2*Q
assert S.expand(elimination + 500*(4*c+5)*(8*c+19)*(64*c*c+64*c+115)) == 0
assert S.discriminant(64*c*c+64*c+115,c) < 0

H=S.hessian(E,(a,b))
expected=[
 (0,0,S.Integer(0),[[S.Rational(2,9),-S.Rational(1,12)],[-S.Rational(1,12),S.Rational(1,2)]],S.Rational(5,48)),
 (0,S.pi/2,S.Rational(1,4),[[S.Rational(11,108),S.Rational(1,12)],[S.Rational(1,12),-S.Rational(1,2)]],-S.Rational(25,432)),
 (S.pi,0,S.Rational(20,81),[[-S.Rational(2,81),S.Rational(1,108)],[S.Rational(1,108),S.Rational(17,54)]],-S.Rational(275,34992)),
 (S.pi,S.pi/2,S.Rational(131,324),[[-S.Rational(17,324),-S.Rational(1,108)],[-S.Rational(1,108),-S.Rational(17,54)]],S.Rational(575,34992)),
]
for aa,bb,val,he,det in expected:
    point={a:aa,b:bb}
    assert S.simplify(E.subs(point)-val)==0
    assert all(S.simplify(S.diff(E,t).subs(point))==0 for t in (a,b))
    assert H.subs(point)==S.Matrix(he)
    assert H.subs(point).det()==det
    # The shift b->b+pi has unchanged value, gradient and Hessian.
    assert S.simplify(E.subs({a:aa,b:bb+S.pi})-val)==0
    assert H.subs({a:aa,b:bb+S.pi})==S.Matrix(he)

assert S.simplify(E.subs({a:S.pi,b:S.pi/2})-S.Rational(131,324))==0
print('VERIFY_OK; exact projectors, realignment and partial-transpose invariants,')
print('Fourier expansion, root exclusion polynomial, and eight critical-point Hessians.')
