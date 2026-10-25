"""Exact certificates for Radau IIA heat-step positivity on Boolean cubes.

Requires SymPy >= 1.10. Run: python verify.py
All inequalities used for arbitrary dimension are proved algebraically in RESULT.md;
these checks establish the finite polynomial identities and sample matrix identities.
"""
from math import comb
from fractions import Fraction
import sympy as s

h = s.symbols('h', nonnegative=True)

def radau_spectral(j, t):
    return (6 - 4*j*t) / (6 + 8*j*t + 4*j*j*t*t)

def coefficient(d, k, t):
    out = 0
    for j in range(d+1):
        K = sum((-1)**i * comb(k,i) * comb(d-k,j-i)
                for i in range(max(0,j-(d-k)),min(k,j)+1))
        out += K*radau_spectral(j,t)
    return s.factor(s.cancel(out/s.Integer(2)**d))

A = 2*h**2+4*h+3
B = 6*h**2+4*h+1
C = 8*h**2+8*h+3
D = 32*h**2+16*h+3
Q = 192*h**8-848*h**7-1300*h**6+168*h**5+2242*h**4+2216*h**3+1050*h**2+252*h+27
q3 = 12*h**6-14*h**5+22*h**4+83*h**3+98*h**2+45*h+9
expected3 = [
    q3/(A*B*C),
    h*(12*h**5+42*h**4+92*h**3+95*h**2+45*h+9)/(A*B*C),
    h**2*(12*h**4+58*h**3+76*h**2+45*h+9)/(A*B*C),
    3*h**3*(4*h**3+22*h**2+18*h+3)/(A*B*C),
]
expected4 = [
    Q/(A*B*C*D),
    h*(24*h**5+50*h**4+168*h**3+163*h**2+60*h+9)/(A*B*D),
    h**2*(16*h**2+36*h+9)/(C*D),
    3*h**3*(8*h**3+38*h**2+24*h+3)/(A*B*D),
    6*h**4*(32*h**4+200*h**3+210*h**2+60*h+3)/(A*B*C*D),
]
for d, targets in [(3,expected3),(4,expected4)]:
    for k, expected in enumerate(targets):
        assert s.cancel(coefficient(d,k,h)-expected)==0, (d,k)

assert s.factor(Q.subs(h,s.Rational(3,2))) == s.Rational(-24057,16)
assert s.cancel(coefficient(4,0,s.Rational(3,2))+s.Rational(3,1804))==0
assert s.expand(q3).coeff(h,4)==22
assert s.discriminant(12*h*h-14*h+22,h)<0
assert [s.sign(c) for c in s.Poly(Q,h).all_coeffs()] == [1,-1,-1,1,1,1,1,1,1]
for lo,hi in [(s.Rational(1465467,1000000),s.Rational(1465468,1000000)),
              (s.Rational(5529949,1000000),s.Rational(5529950,1000000))]:
    assert Q.subs(h,lo)*Q.subs(h,hi)<0
assert s.count_roots(Q,0,s.oo)==2

for d in range(4,18):
    t=s.Rational(3,2)
    diag=sum(s.binomial(d,j)*radau_spectral(j,t) for j in range(d+1))/s.Integer(2)**d
    assert diag<0

# Independent direct inversions against the Walsh formula at exact rational steps.
comparisons=0
for d in range(1,6):
    n=2**d
    L=s.diag(*([d]*n))
    for u in range(n):
        for b in range(d):
            v=u^(1<<b)
            L[u,v]=-1
    for t in [s.Rational(1,5),s.Rational(3,2)]:
        I=s.eye(n)
        T=(6*I-2*t*L)*(6*I+4*t*L+t*t*L*L).inv()
        for v in range(n):
            k=v.bit_count()
            assert s.cancel(T[0,v]-coefficient(d,k,t))==0,(d,v,t)
            comparisons+=1

# Verify fixed-step Walsh witness and its sign pattern on first four levels.
assert [radau_spectral(j,s.Rational(3,2)) for j in range(5)] == [s.Integer(1),s.Integer(0),-s.Rational(1,11),-s.Rational(4,41),-s.Rational(1,11)]
print(f'VERIFY_OK 9 symbolic kernel identities, 2 root isolations, 14 dimension checks, {comparisons} direct rational matrix entries')
