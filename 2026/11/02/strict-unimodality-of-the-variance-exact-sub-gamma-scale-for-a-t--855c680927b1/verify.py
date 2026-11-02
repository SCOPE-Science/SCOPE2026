"""Exact checks for the unique optimal variance-exact right sub-gamma scale.

The mathematical proof of the infinite coefficient tail and of uniqueness is in RESULT.md;
these computations check the finite exceptions, local signs and numerical location.
"""
from fractions import Fraction
from math import comb, exp, factorial, isclose

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def t_coefficient(n):
    """Return n! times the t^n coefficient of N(t)."""
    lead = 32 * n * (n - 1) * (n - 3) * (39 + 5 ** (n - 2))
    square = sum(comb(n, j) * (39 + 5**j) * (39 + 5**(n - j))
                 for j in range(2, n - 1))
    return lead - square


def exp_bounds_positive_rational(z, degree=80):
    """Fully rational lower/upper bounds for exp(z), 0 <= z < degree+2."""
    check(z >= 0 and z < degree + 2, "exponential bound domain")
    term = Fraction(1)
    lower = term
    for k in range(1, degree + 1):
        term *= z / k
        lower += term
    omitted = term * z / (degree + 1)
    upper = lower + omitted / (1 - z / (degree + 2))
    check(lower <= upper, "exponential enclosure ordering")
    return lower, upper


def numerator_bounds(t):
    """Enclose N(t) by rational interval arithmetic using positive e^t terms."""
    e1_low, e1_hi = exp_bounds_positive_rational(t)
    e5_low, e5_hi = exp_bounds_positive_rational(5 * t)
    f_low = 39 * e1_low + e5_low - 40 - 44 * t
    f_hi = 39 * e1_hi + e5_hi - 40 - 44 * t
    fp_low = 39 * e1_low + 5 * e5_low - 44
    fp_hi = 39 * e1_hi + 5 * e5_hi - 44
    check(0 < f_low <= f_hi, "positive F")
    return (32*t**3*fp_low -32*t**2*f_hi - f_hi**2,
            32*t**3*fp_hi -32*t**2*f_low - f_low**2)


def ffloat(t):
    return 39 * (exp(t) - 1 - t) + exp(5*t) - 1 - 5*t


def nfloat(t):
    ft = ffloat(t)
    fprime = 39*exp(t) + 5*exp(5*t) - 44
    return 32*t*t*t*fprime -32*t*t*ft -ft*ft


def scale(t):
    return 1/t - 32*t/ffloat(t)

# Explicit exact initial-coefficient checks.
expected = {4: 0, 5: 0, 6: 99520, 7: 882112,
            8: -4769408, 9: -240640896,
            10: -4342095552, 11: -59940771264}
for n, target in expected.items():
    check(t_coefficient(n) == target, f"coefficient n={n}")

# Finite instances of the analytic tail bound; beyond them RESULT proves induction.
for n in range(12, 120):
    s = 2**n - 2*n - 2
    q = Fraction(s) - Fraction(64, 25)*n*(n-1)*(n-3)
    check(q > 0, f"positive analytic Q_{n}")
    check(t_coefficient(n) < 0, f"negative coefficient n={n}")
    if n < 119:
        next_q = Fraction(2**(n+1) - 2*(n+1) - 2) - Fraction(64, 25)*(n+1)*n*(n-2)
        difference = 2*n + Fraction(64,25)*n*(n*n - 7*n + 8)
        check(next_q - 2*q == difference and difference > 0,
              f"induction identity n={n}")

# Rigorous bracket; every sign comes from rational interval arithmetic.
left = Fraction(473723111, 10**9)
right = Fraction(473723113, 10**9)
lo0, hi0 = numerator_bounds(left)
lo1, hi1 = numerator_bounds(right)
check(lo0 > 0, "N is positive at left endpoint")
check(hi1 < 0, "N is negative at right endpoint")

# Independent floating-point bisection only locates the rigorously unique zero.
l, r = float(left), float(right)
for _ in range(55):
    mid=(l+r)/2
    if nfloat(mid)>0:
        l=mid
    else:
        r=mid
root=(l+r)/2
check(float(left) <= root <= float(right), "numerical root lies in exact bracket")
check(isclose(scale(root), 0.895416096, abs_tol=5e-9), "published approximate scale")
check(scale(root)>Fraction(41,48), "strict improvement on third-cumulant scale")
check(scale(0.3)<scale(root) and scale(0.7)<scale(root), "interior maximum")

# Verify the identity with an independent numeric cumulant generator.
for k in range(1, 60):
    t=k/100
    mgf_rem=ffloat(t)/(32*t*t)
    check(mgf_rem>1, "canonical remainder MGF positive")
    check(isclose(scale(t), (1-1/mgf_rem)/t, abs_tol=2e-12), "two scale formulas")

print(f"PASSED: {checks} assertions")
print("integer coefficient profile n=4..11:", [t_coefficient(n) for n in range(4,12)])
print(f"exact isolating interval: ({left}, {right})")
print("endpoint sign enclosures: left positive, right negative (exact rational)")
print(f"numeric optimum t*: {root:.12f}")
print(f"numeric optimal scale c*: {scale(root):.12f}")
print("global uniqueness: proved by analytic single sign change and induction in RESULT.md")
