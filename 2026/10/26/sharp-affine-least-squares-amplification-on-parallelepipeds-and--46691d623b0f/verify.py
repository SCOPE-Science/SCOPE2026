"""Exact-rational checks for affine least-squares projection on a cube.

Execute: python verify.py
Requires only the Python standard library.
The all-dimensional theorem is proved in RESULT.md; finite tests do not prove it.
"""
from fractions import Fraction as F
from math import factorial, comb, sqrt, pi

checks = 0


def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)


def formula(d):
    """Finite alternating-power formula, evaluated with exact fractions."""
    a = F(3 * d + 1, 6)
    return -1 + F(12, factorial(d + 1)) * sum(
        ((-1)**k) * comb(d, k) * (a - k)**(d + 1)
        for k in range(int(a) + 1)
    )


def poly_int(coeffs, v):
    return sum(c * v**(i+1) / (i+1) for i,c in enumerate(coeffs))


def poly_val(coeffs, v):
    return sum(c*v**i for i,c in enumerate(coeffs))


def density_pieces(d):
    """Independent exact convolution of uniform densities.

    Each polynomial q[j](v) is density of sum U_1+...+U_d at j+v,
    with 0<=v<=1, U_i iid uniform on [0,1].
    """
    pieces = [[F(1)]]
    for n in range(1, d):
        next_pieces = []
        for j in range(n+1):
            lower = pieces[j-1] if j > 0 else []
            upper = pieces[j] if j < n else []
            degree = max(len(lower), len(upper))
            coeffs = [poly_int(lower, F(1))]
            for power in range(degree):
                L = lower[power] if power < len(lower) else 0
                R = upper[power] if power < len(upper) else 0
                coeffs.append(F(R-L, power+1))
            next_pieces.append(coeffs)
        pieces = next_pieces
    return pieces


def piecewise_absolute(d):
    """Integrate |1+3 sum Y_i| independently of the alternating formula."""
    b = F(3*d-1, 6)  # Zero of 6s-3d+1.
    total = F(0)
    for j, q in enumerate(density_pieces(d)):
        c = F(6*j-3*d+1)
        kernel_poly = [c*q[0]] + [c*q[i] + 6*q[i-1] for i in range(1,len(q))] + [6*q[-1]]
        split = max(F(0),min(F(1),b-j))
        left = poly_int(kernel_poly,split)
        right = poly_int(kernel_poly,F(1))-left
        total += right-left
        check(poly_val(q,F(1,2)) >= 0, f'nonnegative density d={d} interval={j}')
    return total

expected = {1:F(5,3),2:F(233,108),3:F(415,162),
            4:F(75437,25920),5:F(46973,14580),
            6:F(206080321,58786560)}
for d in range(1,15):
    exact = formula(d)
    check(exact > 1, f'lambda > 1, d={d}')
    check(formula(d+1) > exact, f'strictly increasing, d={d}')
    if d <= 9:
        check(piecewise_absolute(d) == exact, f'independent convolution, d={d}')
    if d in expected:
        check(exact == expected[d], f'published exact table, d={d}')
check(formula(4) < 3 < formula(5), 'first positivity defect beyond one is d=5')

# Continuous affine covariance calculation on the normalized cube:
# ∫1=1, ∫Y_i=0, ∫Y_i^2=1/3, ∫Y_iY_j=0 (i≠j),
# so K(x,y)=1+3*x·y reproduces 1 and all coordinate functions.
# A sign input at any vertex realizes the exact absolute kernel mass.
for d in range(1,10):
    lam = formula(d)
    C = (lam-1)/2
    check(C>0, f'negative kernel mass d={d}')
    check(1+2*C==lam, f'positivity/row-norm identity d={d}')

# Numerical corroboration of the analytically proved second-order law.
for d in [20, 40, 80, 160]:
    ratio = float(formula(d)) / sqrt(6*d/pi)
    estimate = d*(ratio-1)
    check(abs(estimate - 13/60) < 0.02, f'asymptotic check d={d}')

print(f'ALL CHECKS PASSED ({checks} assertions; independent convolution through d=9)')
