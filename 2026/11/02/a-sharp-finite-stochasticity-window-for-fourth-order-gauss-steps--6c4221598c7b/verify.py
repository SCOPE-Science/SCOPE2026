"""Exact independent checks for the eight-cycle Gauss endpoint positivity theorem.

Requires Python 3.10+ and sympy>=1.10; does not use floating-point
certification. All matrices and coefficients are rational over Q(h).
"""
import sympy as sp

h, z = sp.symbols('h z')
D = 12 + 6*h*(1-z) + h*h*(1-z)**2
N = 12 - 6*h*(1-z) + h*h*(1-z)**2
mod = z**8 - 1
C = sp.rem(sp.invert(D, mod, z)*N, mod, z)
co = [sp.factor(sp.expand(C).coeff(z, j)) for j in range(8)]
assert sp.simplify(sum(co)-1) == 0

common = 4*(h*h+3*h+3)*(h**4+6*h**3+18*h*h+36*h+36)*(
    h**8+12*h**7+84*h**6+432*h**5+1800*h**4+5184*h**3
    +9504*h*h+10368*h+5184)
assert all(sp.denom(sp.cancel(c*common)) == 1 for c in co)
num = [sp.Poly(sp.cancel(c*common),h) for c in co]

# The polynomial numerator of each displacement probability has
# an exact factorization. Repeated zero factors h^k and h+2 are positive
# at h>0. The remaining factors are ordered from left to right.
expected = [
    4*h**14+63*h**13+420*h**12+1512*h**11+3276*h**10
    +4536*h**9+7344*h**8+58320*h**7+399168*h**6
    +1632960*h**5+4354560*h**4+7838208*h**3
    +9331200*h**2+6718464*h+2239488,
    -3*h*(5*h**12+96*h**11+792*h**10+3672*h**9+9288*h**8
    -111024*h**6-528768*h**5-1446336*h**4-2612736*h**3
    -3110400*h**2-2239488*h-746496),
    -9*h**2*(h+2)*(h**10+10*h**9-516*h**7-4248*h**6
    -19728*h**5-60912*h**4-128736*h**3-181440*h**2
    -155520*h-62208),
    -3*h**3*(h**10-12*h**9-396*h**8-3888*h**7-22176*h**6
    -84672*h**5-225072*h**4-414720*h**3-508032*h**2
    -373248*h-124416),
    3*h**4*(h**9+48*h**8+624*h**7+4284*h**6+18648*h**5
    +54432*h**4+106704*h**3+134784*h**2+98496*h+31104),
    9*h**5*(h+2)*(h**7+22*h**6+180*h**5+816*h**4
    +2232*h**3+3600*h**2+3024*h+864),
    3*h**7*(5*h**6+84*h**5+588*h**4+2268*h**3
    +5040*h**2+6048*h+3024),
    3*h**7*(7*h**6+84*h**5+420*h**4+1008*h**3
    +1008*h**2-432),
]
assert all(sp.expand(num[j].as_expr()-expected[j]) == 0 for j in range(8))

p1 = sp.Poly(-expected[1]/(3*h),h)
p2 = sp.Poly(-expected[2]/(9*h**2*(h+2)),h)
p3 = sp.Poly(-expected[3]/(3*h**3),h)
p7 = sp.Poly(expected[7]/(3*h**7),h)

def desc_sign_variations(p):
    nonzero = [sp.sign(v) for v in p.all_coeffs() if v != 0]
    return sum(nonzero[i] != nonzero[i+1] for i in range(len(nonzero)-1))

assert all(desc_sign_variations(p) == 1 for p in (p1,p2,p3,p7))
assert p7.eval(sp.Rational(1,2)) < 0 < p7.eval(sp.Rational(3,5))
assert p1.eval(sp.Rational(7,2)) < 0 < p1.eval(4)
assert p2.eval(4)<0 and p3.eval(4)<0
assert all(v>0 for p in (num[0],num[4],num[5],num[6]) for v in p.all_coeffs() if v)

# Endpoints: h=6x, with these primitive polynomials in x.
x = sp.symbols('x')
low = sp.Poly(756*x**6+1512*x**5+1260*x**4+504*x**3+84*x**2-1,x)
up = sp.Poly(14580*x**12+46656*x**11+64152*x**10+49572*x**9
    +20898*x**8-6939*x**6-5508*x**5-2511*x**4-756*x**3
    -150*x**2-18*x-1,x)
assert sp.Poly(p7.as_expr().subs(h,6*x),x).primitive()[1] == low
assert sp.Poly(p1.as_expr().subs(h,6*x),x).primitive()[1] == up

# Independent rational matrix checks (the modular calculation is not
# used here). The min-entry sign, row sums, and circulant identity are
# checked by direct exact inversion.
S = sp.zeros(8)
for i in range(8): S[i,(i+1)%8] = 1
Q = S-sp.eye(8)
for step, expected_nonnegative in [
    (sp.Rational(1,20),False), (sp.Rational(1,2),False),
    (sp.Rational(3,5),True), (sp.Rational(3,4),True),
    (sp.Rational(1),True), (sp.Rational(2),True),
    (sp.Rational(3),True), (sp.Rational(7,2),True),
    (sp.Rational(4),False), (sp.Rational(6),False),
]:
    numer=sp.eye(8)+step*Q/2+step**2*Q**2/12
    denom=sp.eye(8)-step*Q/2+step**2*Q**2/12
    M=denom.inv()*numer
    assert all(sum(M[i,j] for j in range(8)) == 1 for i in range(8))
    assert all(M[0,j] == co[j].subs(h,step) for j in range(8))
    assert all((M[i,j]>=0) for i in range(8) for j in range(8)) == expected_nonnegative
print('VERIFIED: exact circulant identities, four Descartes isolations, two algebraic endpoint polynomials, and ten rational matrix instances')
