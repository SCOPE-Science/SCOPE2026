#!/usr/bin/env python3
"""Exact symbolic verification for the periodic five-sample running median.

Requires SymPy. All symbolic comparisons use exact integer or algebraic
arithmetic; there are no floating-point tolerances in the certificates.
"""
from itertools import permutations
import sympy as S

q, t = S.symbols('q t', positive=True)
n = 5
L = S.zeros(n)
for i in range(n):
    L[i, i] += 2
    L[i, (i - 1) % n] -= 1
    L[i, (i + 1) % n] -= 1
A = S.eye(n) + q * L
d = 5*q*q + 5*q + 1
r = (10*q*q + 11*q + 3) / d

def matrix(index):
    P = S.zeros(n)
    for i, j in enumerate(index):
        P[i, j] = 1
    return P

def median_index(order):
    rank = {v: k for k, v in enumerate(order)}
    return tuple(sorted(((i-1)%n,i,(i+1)%n), key=lambda j: rank[j])[1]
                 for i in range(n))

# Full strict-order chamber enumeration and dihedral reduction.
selectors = {median_index(o) for o in permutations(range(n))}
assert len(selectors) == 60
symmetries = [tuple((sign*i + shift) % n for i in range(n))
              for sign in (1,-1) for shift in range(n)]
classes = []
rest = set(selectors)
while rest:
    rep = min(rest)
    orbit = {tuple(p[rep[p.index(i)]] for i in range(n))
             for p in symmetries}
    assert orbit <= selectors
    classes.append((rep, len(orbit)))
    rest -= orbit
expected = [
    ((0,0,1,2,0),10), ((0,0,1,4,0),5),
    ((0,0,2,2,4),10), ((0,0,2,4,4),5),
    ((0,0,3,2,0),5), ((0,0,3,2,3),10),
    ((0,0,3,3,4),5), ((0,0,3,4,3),10)]
assert classes == expected and sum(s for _,s in classes) == 60
P = [matrix(idx) for idx,_ in classes]

def charpoly(j):
    return S.factor((P[j].T*A*P[j] - t*A).det())

# The two potential winning classes have exactly the stated spectra.
assert S.simplify(charpoly(4).subs(t,r)) == 0
G = (
    25*q**4*t**3-125*q**4*t**2+160*q**4*t-60*q**4
    +50*q**3*t**3-240*q**3*t**2+336*q**3*t-140*q**3
    +35*q**2*t**3-165*q**2*t**2+244*q**2*t-112*q**2
    +10*q*t**3-48*q*t**2+74*q*t-36*q
    +t**3-5*t**2+8*t-4)
assert S.simplify(charpoly(7) + t**2*G) == 0
assert S.factor(G.subs(t,1)) == 2*q**2*(3*q+1)
assert S.factor(G.subs(t,2)) == -4*q**2*(2*q+1)*(5*q+1)

# Strict Loewner certificates: all leading principal minors of
# d(q)*(r(q) A - P_j^T A P_j) have nonnegative integer coefficients
# and are nonzero, hence positive for q>0.
count = 0
for j in (0,1,2,6):
    B = (S.cancel(d * (r*A-P[j].T*A*P[j]))).applyfunc(S.cancel)
    for k in range(1,n+1):
        minor = S.factor(B[:k,:k].det())
        coefficients = S.Poly(minor, q).all_coeffs()
        assert any(c > 0 for c in coefficients)
        assert all(c >= 0 for c in coefficients), (j,k,minor)
        count += 1
# Classes 2 and 3 share the same characteristic polynomial.
assert S.simplify(charpoly(2)-charpoly(3)) == 0

# Class 5 has a quadratic leading spectral root b(q); class 7
# strictly exceeds it. The comparison is an exact negative identity.
b = (10*q*q + 9*q + 2 + S.sqrt(5)*q*(2*q+1))/d
assert S.simplify(charpoly(5).subs(t,b)) == 0
assert S.simplify((b-2) - q*(2*S.sqrt(5)*q + S.sqrt(5)-1)/d) == 0
negative = -(2*q**3/d)*(
    (50+20*S.sqrt(5))*q**3 + (60+24*S.sqrt(5))*q**2
    +(23+9*S.sqrt(5))*q +(3+S.sqrt(5)))
assert S.factor(G.subs(t,b)-negative, extension=S.sqrt(5)) == 0

# The two winning branches cross at the unique positive root
# of this polynomial. Descartes' rule gives exactly one sign change.
h = 200*q**6+380*q**5+259*q**4+50*q**3-25*q**2-14*q-2
assert S.simplify(G.subs(t,r)+h/d) == 0
assert S.factor(r-2) == (q+1)/d
assert S.simplify(S.diff(r,q)+(5*q*q+10*q+4)/d**2) == 0
coeff = S.Poly(h,q).all_coeffs()
assert sum(1 for i in range(len(coeff)-1) if coeff[i]>0 and coeff[i+1]<0) == 1
assert h.subs(q,0)<0 and S.LC(S.Poly(h,q))>0

# Strong-energy limiting branch: roots of the leading coefficient.
assert S.expand(S.Poly(G,q).coeff_monomial(q**4)-25*(t-1)*(t**2-4*t+S.Rational(12,5))) == 0
print('PASS: 120 strict orders; 60 selector matrices; eight dihedral classes;')
print('PASS: two characteristic identities; 20 positive-minor certificates;')
print('PASS: strict competitor exclusion; unique positive phase root;')
print('PASS: exact strong-energy limiting polynomial.')
print('phase_root_approx =',
      [z for z in S.nroots(h) if abs(S.im(z))<S.Rational(1,10**8) and S.re(z)>0][0])
