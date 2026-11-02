#!/usr/bin/env python3
"""Exact algebraic and independent transient-chain checks for a three-site SIS model.

Requires Python 3 and SymPy. Run: python VERIFY.py
The finite checks supplement, rather than replace, the all-parameter proof.
"""
from itertools import product
from sympy import (Matrix, Poly, Rational, diff, factor, simplify,
                   symbols, zeros, ones, nroots)

x, y, b, B, r, t = symbols('x y b B r t', positive=True)

# Five orbit classes under exchange of the two endpoints:
# endpoint singleton; center singleton; center-endpoint pair; two endpoints; triple.
M = Matrix([
    [x+b,    0,          -b,          0,        0],
    [0,      y+2*b,      -2*b,        0,        0],
    [-y,     -x,         x+y+b,      0,       -b],
    [-2*x,    0,          0,          2*x+2*b, -2*b],
    [0,       0,         -2*x,       -y,        2*x+y],
])
num = (4*b**4 + 4*b**3*(4*x+y)
       + b**2*(24*x**2+32*x*y+y**2)
       + b*(16*x**3+28*x**2*y+18*x*y**2)
       + 4*x**4+6*x**3*y+9*x**2*y**2+3*x*y**3)
closed = num / (2*x**2*y*(2*b+x+y)*(4*b+2*x+y))
assert simplify((M.inv()*ones(5,1))[4] - closed) == 0
print('PASS: exact five-state first-step system and closed hitting-time formula')

# No quotient-chain assumption: construct the seven transient states independently.
def exact_full_hitting_time(x0, y0, b0):
    rates = (x0, y0, x0)
    states = tuple(range(1, 8))
    Q = zeros(7)
    for index, mask in enumerate(states):
        for vertex in range(3):
            bit = 1 << vertex
            if mask & bit:
                rate = rates[vertex]
                target = mask ^ bit
            else:
                neighbors = ((1,), (0,2), (1,))[vertex]
                rate = b0 * sum(bool(mask & (1 << u)) for u in neighbors)
                target = mask | bit
            if rate == 0:
                continue
            Q[index,index] += rate
            if target:
                Q[index,states.index(target)] -= rate
    return (Q.inv()*ones(7,1))[states.index(7)]

checks = 1
for x0,y0,b0 in product((Rational(1,7),Rational(1,4),Rational(1,2),Rational(3,5)),
                         (Rational(1,5),Rational(1,3),Rational(3,4)),
                         (Rational(0),Rational(1,8),Rational(1,2),Rational(1),Rational(7))):
    direct = exact_full_hitting_time(x0,y0,b0)
    expected = closed.subs({x:x0,y:y0,b:b0})
    assert direct == expected, (x0,y0,b0,direct,expected)
    checks += 1
print('PASS: 60 independent exact-rational seven-state transient-chain comparisons')

# Normalize budget B: x=B*t/(2*t+1), y=B/(2*t+1), b=B*r.
F = factor(B*closed.subs({x:B*t/(2*t+1), y:B/(2*t+1), b:B*r}))
assert not F.has(B)
coeffs = [
    4*(2*r+1)**4*(4*r+1),
    8*(2*r+1)**5,
    -(128*r**5+96*r**4+96*r**3+44*r**2+16*r+3),
    -2*(2*r+1)*(4*r+1)*(16*r**3+12*r**2+12*r+3),
    -(2*r+1)**2*(28*r**3+15*r**2+12*r+3),
    -2*r**2*(2*r+1)**3,
]
P = sum(a*t**(5-j) for j,a in enumerate(coeffs))
D = 2*t**3*(4*r+1)*(4*r*t+2*r+t+1)**2
assert simplify(diff(F,t)-P/D) == 0
assert simplify(P.subs(t,Rational(1,2))
  +(512*r**5+640*r**4+512*r**3+288*r**2+90*r+11)/4) == 0
assert simplify(P.subs(t,1)-r*(540*r**3+540*r**2+207*r+28)) == 0
assert factor(P.subs(r,0)) == t*(t-1)*(4*t**3+12*t**2+9*t+3)
assert simplify(Poly(P,r).coeff_monomial(r**5) - 16*(t-1)*(2*t+1)**4) == 0
assert diff(P,t).subs({r:0,t:1}) == 28
assert diff(P,r).subs({r:0,t:1}) == 28
assert diff(Poly(P,r).coeff_monomial(r**5),t).subs(t,1) == 1296
assert Poly(P,r).coeff_monomial(r**4).subs(t,1) == 540
checks += 10
print('PASS: derivative polynomial, signs, and both asymptotic coefficients')

# Coefficients of t^5 and t^4 positive; all t^3,...,t^0 negative
# for r>0. Descartes' rule and opposite signs at 1/2,1 prove uniqueness.
for rval in (Rational(1,100),Rational(1,10),Rational(1,2),1,2,10,100):
    pv = Poly(P.subs(r,rval),t)
    c = list(pv.all_coeffs())
    assert c[0]>0 and c[1]>0 and all(u<0 for u in c[2:])
    assert P.subs({r:rval,t:Rational(1,2)}) < 0
    assert P.subs({r:rval,t:1}) > 0
    checks += 3
print('PASS: rational sign audits across multiple infection intensities')

# A dimensionless benchmark used in the prose, with independent interval tests.
p1 = P.subs(r,1)
lo=Rational(836926,1000000)
hi=Rational(836928,1000000)
assert p1.subs(t,lo)<0<p1.subs(t,hi)
# Exact comparison is used instead of floating-point optimization.
assert F.subs({r:1,t:Rational(5,6)}) < F.subs({r:1,t:1})
assert F.subs({r:1,t:Rational(5,6)}) < F.subs({r:1,t:Rational(1,2)})
checks += 3
print('PASS: benchmark enclosure and exact improvement over both named designs')
print('TOTAL_EXACT_ASSERTIONS:', checks)

# Global optimum, not merely a restriction to equal endpoint rates.
# Construct all seven transient states again with independent endpoint rates.
u, v, h, z = symbols('u v h z', positive=True)
M7 = zeros(7)
for index, mask in enumerate(range(1,8)):
    for vertex in range(3):
        bit = 1 << vertex
        if mask & bit:
            rate = (u,y,v)[vertex]
            target = mask ^ bit
        else:
            near = ((1,), (0,2), (1,))[vertex]
            rate = b * sum(bool(mask & (1 << k)) for k in near)
            target = mask | bit
        M7[index,index] += rate
        if target:
            M7[index,target-1] -= rate
T7 = factor((M7.inv()*ones(7,1))[6])
assert simplify(T7.subs({u:x,v:x}) - closed) == 0
assert simplify(T7.subs({u:v,v:u},simultaneous=True)-T7) == 0
checks += 2
# Let u=x+h, v=x-h, and z=x^2-h^2>0. Exact algebra shows
# T7(u,y,v)-T7(x,y,x) = h^2*N/(positive factors*Q).
# Expanding N and Q in (b,x,y,z) gives respectively 55 and 16
# strictly positive integer coefficients; this proves global strict
# endpoint symmetrization for every b>0, y>0, 0<|h|<x.
Duv = factor(T7.subs({u:x+h,v:x-h}, simultaneous=True)-T7.subs({u:x,v:x},simultaneous=True))
Nraw, Draw = __import__('sympy').fraction(Duv)
N = factor(Nraw/h**2)
Q = factor(Draw/(2*x**2*y*(x-h)*(x+h)*(2*b+x+y)*(4*b+2*x+y)))
assert not N.has(u,v) and not Q.has(u,v)
assert Poly(N,h).degree() == 2 and Poly(Q,h).degree() == 2
Npositive = Poly(N.subs(h**2,x**2-z).expand(), b,x,y,z)
Qpositive = Poly(Q.subs(h**2,x**2-z).expand(), b,x,y,z)
assert len(Npositive.terms()) == 55
assert len(Qpositive.terms()) == 16
assert all(co>0 for mon,co in Npositive.terms())
assert all(co>0 for mon,co in Qpositive.terms())
checks += 6
print('PASS: exact unrestricted seven-state reduction and strict endpoint symmetrization')
print('SYMMETRY_CERTIFICATE_COUNTS: 55 positive numerator monomials, 16 positive denominator monomials')
print('TOTAL_EXACT_ASSERTIONS_WITH_GLOBAL_SYMMETRY:',checks)
