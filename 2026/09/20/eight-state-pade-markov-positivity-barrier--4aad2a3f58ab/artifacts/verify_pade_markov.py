import sympy as sp
import numpy as np

x, z = sp.symbols('x z', positive=True, real=True)
r = (12 + 6*z + z**2)/(12 - 6*z + z**2)
D = x**2 + 6*x + 12

# Maclaurin coefficients through the first negative coefficient.
series = sp.series(r, z, 0, 8).removeO().expand()
coeffs = [sp.expand(series).coeff(z, k) for k in range(8)]
expected = [sp.Integer(1), sp.Integer(1), sp.Rational(1,2), sp.Rational(1,6),
            sp.Rational(1,24), sp.Rational(1,144), sp.Integer(0), -sp.Rational(1,1728)]
assert coeffs == expected

# Eight-state pure-birth generator with state 8 absorbing.
n = 8
Q = sp.zeros(n)
for i in range(n-1):
    Q[i,i] = -1
    Q[i,i+1] = 1
I = sp.eye(n)
# Build the rational map from the Jordan functional-calculus formula instead
# of asking a CAS for a symbolic 8x8 inverse.  Verify it by the defining
# denominator-times-map identity below.
M = sp.zeros(n)
for i in range(n-1):
    m = n-2-i
    transient_sum = 0
    for d in range(m+1):
        entry = x**d*sp.diff(r,z,d).subs(z,-x)/sp.factorial(d)
        M[i,i+d] = entry
        transient_sum += entry
    M[i,n-1] = 1-transient_sum
M[n-1,n-1] = 1
num = I + x*Q/2 + x**2*Q**2/12
den = I - x*Q/2 + x**2*Q**2/12
for i in range(n):
    for j in range(n):
        assert sp.cancel((den*M-num)[i,j]) == 0
assert M*sp.ones(n,1) == sp.ones(n,1)

p = 7*x**6 + 126*x**5 + 840*x**4 + 2520*x**3 + 3024*x**2 - 1728
m18 = 12*x**7*p/D**7
assert sp.simplify(M[0,7] - m18) == 0
m12 = 12*x*(12-x**2)/D**2
assert sp.simplify(M[0,1] - m12) == 0

# Jordan-block entries to transient states are scaled derivatives of r at -x.
for d in range(7):
    assert sp.simplify(M[0,d] - x**d*sp.diff(r,z,d).subs(z,-x)/sp.factorial(d)) == 0

# Absorbing-column Taylor remainders for rows with m=0,...,6 transient derivatives.
expected_tails = [
    12*x/D,
    24*x**2*(x+3)/D**2,
    36*x**3*(x+2)*(x+4)/D**3,
    48*x**4*(x+3)*(x**2+6*x+6)/D**4,
    12*x**5*(5*x**4+60*x**3+240*x**2+360*x+144)/D**5,
    72*x**7*(x+2)*(x+3)*(x+4)*(x+6)/D**6,
    m18,
]
for m, target in enumerate(expected_tails):
    tail = 1 - sum(x**d*sp.diff(r,z,d).subs(z,-x)/sp.factorial(d) for d in range(m+1))
    assert sp.simplify(tail-target) == 0

# Exact sign certificates for transient derivatives on 0 < x <= 2*sqrt(3).
# Each identity reduces positivity to 12-x**2 >= 0 plus manifestly
# nonnegative terms (strictly positive on the interval where needed).
deriv_nums = []
for d in range(7):
    expr = sp.factor(sp.diff(r,z,d).subs(z,-x))
    deriv_nums.append(sp.factor(sp.together(expr).as_numer_denom()[0]))
assert sp.expand((x**2 - 6*x + 12) - ((x-3)**2 + 3)) == 0
assert sp.expand((72 + 36*x - x**3) - (72 + 24*x + x*(12-x**2))) == 0
assert sp.expand((-x**4 + 72*x**2 + 288*x + 288) - ((12-x**2)*(12+x**2) + 72*x**2 + 288*x + 144)) == 0
assert sp.expand((-x**4 + 6*x**3 + 84*x**2 + 216*x + 144) - ((12-x**2)*(12+x**2) + 6*x**3 + 84*x**2 + 216*x)) == 0
assert sp.expand((-x**6 + 180*x**4 + 1440*x**3 + 4320*x**2 + 5184*x + 1728) - ((12-x**2)*(x**4+12*x**2+144) + 180*x**4 + 1440*x**3 + 4320*x**2 + 5184*x)) == 0
assert sp.expand((-x**6 + 252*x**4 + 2520*x**3 + 10080*x**2 + 18144*x + 12096) - ((12-x**2)*(x**4+12*x**2+144) + 252*x**4 + 2520*x**3 + 10080*x**2 + 18144*x + 10368)) == 0

# p has exactly one positive root because p(0)<0 and p'(x)>0 for x>0.
assert p.subs(x,0) < 0
assert all(c >= 0 for c in sp.Poly(sp.diff(p,x),x).all_coeffs())

# Unique positive root of p and the upper endpoint 2*sqrt(3).
roots = [rr for rr in sp.nroots(p, n=40, maxsteps=200) if abs(complex(rr).imag) < 1e-25 and float(sp.re(rr)) > 0]
assert len(roots) == 1
h0 = sp.N(sp.re(roots[0]), 30)
h1 = sp.N(2*sp.sqrt(3), 30)

# Numerical sign checks on both sides of each exact boundary.
def mat_at(v):
    return sp.matrix2numpy(sp.N(M.subs(x, sp.Rational(str(v))), 30), dtype=float)
for v, expected_nonnegative in [(0.1, False), (0.7, True), (3.0, True), (3.6, False)]:
    A = mat_at(v)
    minimum = float(A.min())
    assert (minimum >= -1e-12) == expected_nonnegative

print('SymPy version:', sp.__version__)
print('NumPy version:', np.__version__)
print('Maclaurin coefficients a_0,...,a_7:', coeffs)
print('unique lower positivity endpoint h0 =', h0)
print('upper positivity endpoint 2*sqrt(3) =', h1)
print('M_18 numerator factor p(h) =', p)
print('M_12 =', sp.factor(m12))
print('row sums verified symbolically: 1')
print('exact interval sign certificates: PASS')
print('symbolic identities and boundary sign checks: PASS')
