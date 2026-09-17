#!/usr/bin/env python3
"""
Verification for:
Every generalized parking-function polytope X_3(a,b,c), a,b,c >= 1,
is magic positive.

The script:
1. derives L_3 from Hill--Luo--Trinh--Vindas-Melendez's lattice-count recursion;
2. substitutes the dilation parameters (1+(a-1)t, bt, ct);
3. converts the Ehrhart polynomial into the degree-3 magic basis;
4. verifies the manifestly nonnegative shifted formulas symbolically;
5. independently enumerates lattice points for 1<=a,b,c<=5 and 1<=t<=4.
"""

import itertools
import sympy as sp

x, y, z, a, b, c, t, r = sp.symbols(
    "x y z a b c t r", integer=True, positive=True
)
A, B, C = sp.symbols("A B C", integer=True, nonnegative=True)

def L2(u, v):
    return sp.expand((u + v)**2 - v*(v + 1)/2)

L3 = sp.expand(
    x * L2(x + y, z)
    + sp.summation(L2(x + y - r, z + r), (r, 1, y))
    + sp.summation(L2(x, y + z - r), (r, 1, z))
)

ehr = sp.expand(L3.subs({x: 1 + (a - 1)*t, y: b*t, z: c*t}))
P = sp.Poly(ehr, t)

e0, e1, e2, e3 = [sp.simplify(P.nth(i)) for i in range(4)]

# If p(t)=mu0(t+1)^3+mu1*t(t+1)^2+mu2*t^2(t+1)+mu3*t^3:
mu0 = e0
mu1 = sp.expand(e1 - 3)
mu2 = sp.expand(e2 - 2*e1 + 3)
mu3 = sp.expand(e3 - e2 + e1 - 1)

shifted = [
    sp.expand(mu.subs({a: A+1, b: B+1, c: C+1}))
    for mu in (mu1, mu2, mu3)
]

expected = [
    (18*A + 16*B + 11*C + 9) / 6,
    (
        18*A**2 + 36*A*B + 27*A*C + 27*A
        + 15*B**2 + 24*B*C + 22*B
        + 6*C**2 + 14*C + 9
    ) / 6,
    (
        6*A**3 + 18*A**2*B + 18*A**2*C + 18*A**2
        + 18*A*B**2 + 36*A*B*C + 36*A*B
        + 9*A*C**2 + 27*A*C + 18*A
        + 5*B**3 + 12*B**2*C + 12*B**2
        + 6*B*C**2 + 12*B*C + 7*B
        + C**3 + 3*C**2 + 2*C
    ) / 6,
]

for got, want in zip(shifted, expected):
    assert sp.simplify(got - want) == 0

def direct_count(a0, b0, c0, t0):
    # Theorem 2.2 inequalities for t*X_3(a,b,c):
    # xi >= t
    # xi <= t(a+b+c)
    # xi+xj <= t(2a+2b+c)
    # x1+x2+x3 <= t(3a+2b+c)
    U1 = t0 * (a0 + b0 + c0)
    U2 = t0 * (2*a0 + 2*b0 + c0)
    U3 = t0 * (3*a0 + 2*b0 + c0)
    lo = t0
    count = 0
    for x1 in range(lo, U1 + 1):
        for x2 in range(lo, U1 + 1):
            if x1 + x2 > U2:
                continue
            max_x3 = min(U1, U2 - x1, U2 - x2, U3 - x1 - x2)
            if max_x3 >= lo:
                count += max_x3 - lo + 1
    return count

def polynomial_count(a0, b0, c0, t0):
    return int(ehr.subs({a: a0, b: b0, c: c0, t: t0}))

tests = 0
for params in itertools.product(range(1, 6), repeat=3):
    for dil in range(1, 5):
        tests += 1
        lhs = direct_count(*params, dil)
        rhs = polynomial_count(*params, dil)
        assert lhs == rhs, (params, dil, lhs, rhs)

# Published spot checks:
assert sp.expand(ehr.subs({a:3,b:2,c:2})) == 172*t**3 + 84*t**2 + 15*t + 1
assert [sp.simplify(m.subs({a:3,b:2,c:2})) for m in (mu0,mu1,mu2,mu3)] == [1,12,57,102]
assert [sp.simplify(m.subs({a:2,b:3,c:1})) for m in (mu0,mu1,mu2,mu3)] == [1,sp.Rational(59,6),sp.Rational(115,3),54]

print("L3 =", sp.factor(L3))
print("magic coefficients after A=a-1, B=b-1, C=c-1:")
for i, coeff in enumerate([sp.Integer(1)] + shifted):
    print(f"mu_{i} =", sp.factor(coeff))
print(f"Independent lattice enumeration passed {tests} cases.")
print("PASS")
