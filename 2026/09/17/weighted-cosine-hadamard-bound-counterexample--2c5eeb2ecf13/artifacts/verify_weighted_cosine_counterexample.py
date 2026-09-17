"""Exact checks for a weighted-cosine Frobenius-norm counterexample."""
import sympy as sp


def weighted_cosine_frobenius_sq(Sigma, U):
    B = sp.simplify(U * Sigma * U.T)
    d = [sp.simplify(B[i, i]) for i in range(B.rows)]
    return sp.simplify(sum(B[i, j] ** 2 / (d[i] * d[j])
                           for i in range(B.rows) for j in range(B.cols)))


def effective_dimension_bound(Sigma):
    sigma = [Sigma[i, i] for i in range(Sigma.rows)]
    gamma = sp.simplify(sum(sigma) ** 2 / sum(s ** 2 for s in sigma))
    return gamma, sp.simplify(Sigma.rows ** 2 / gamma)


t = sp.symbols("t", positive=True)
U = sp.Matrix([
    [1 / sp.sqrt(3), sp.sqrt(sp.Rational(2, 3)), 0],
    [-1 / sp.sqrt(3), 1 / sp.sqrt(6), 1 / sp.sqrt(2)],
    [1 / sp.sqrt(3), -1 / sp.sqrt(6), 1 / sp.sqrt(2)],
])
assert sp.simplify(U * U.T - sp.eye(3)) == sp.zeros(3)

Sigma3 = sp.diag(3, 1, sp.Rational(1, 3))
B3 = sp.simplify(U * Sigma3 * U.T)
expected_B3 = sp.Matrix([
    [sp.Rational(5, 3), sp.Rational(-2, 3), sp.Rational(2, 3)],
    [sp.Rational(-2, 3), sp.Rational(4, 3), -1],
    [sp.Rational(2, 3), -1, sp.Rational(4, 3)],
])
assert B3 == expected_B3
F3 = weighted_cosine_frobenius_sq(Sigma3, U)
gamma3, bound3 = effective_dimension_bound(Sigma3)
gap3 = sp.simplify(F3 - bound3)
assert F3 == sp.Rational(197, 40)
assert gamma3 == sp.Rational(13, 7)
assert bound3 == sp.Rational(63, 13)
assert gap3 == sp.Rational(41, 520)


# An order-4 counterexample as well, so the failure persists even when real
# Hadamard frames exist in the ambient dimension.
Sigma4 = sp.diag(3, 1, sp.Rational(1, 3), sp.Rational(7, 3))
U4 = sp.diag(1, 1, 1, 1)
U4[:3, :3] = U
assert sp.simplify(U4 * U4.T - sp.eye(4)) == sp.zeros(4)
F4 = weighted_cosine_frobenius_sq(Sigma4, U4)
gamma4, bound4 = effective_dimension_bound(Sigma4)
gap4 = sp.simplify(F4 - bound4)
assert F4 == sp.Rational(237, 40)
assert gamma4 == sp.Rational(20, 7)
assert bound4 == sp.Rational(28, 5)
assert gap4 == sp.Rational(13, 40)

Sigma_t = sp.diag(t, 1, 1 / t)
F_t = sp.factor(weighted_cosine_frobenius_sq(Sigma_t, U))
gamma_t, bound_t = effective_dimension_bound(Sigma_t)
gap_t = sp.factor(F_t - bound_t)
expected_F_t = sp.factor(
    9 * (4*t**5 + 4*t**4 + 9*t**3 + 9*t + 10)
    / ((t + 2) * (2*t**2 + t + 3)**2)
)
expected_gap_t = sp.factor(
    18 * (t - 1)**2 * (2*t**3 - t**2 - 4)
    / ((t + 2) * (t**2 + t + 1) * (2*t**2 + t + 3)**2)
)
assert sp.simplify(F_t - expected_F_t) == 0
assert sp.simplify(gap_t - expected_gap_t) == 0

print(f"sympy={sp.__version__}")
print("UUT=I")
print("B(t=3)=")
print(B3)
print(f"F(t=3)={F3}")
print(f"gamma(t=3)={gamma3}")
print(f"9/gamma(t=3)={bound3}")
print(f"gap(t=3)={gap3}")
print(f"F4={F4}, gamma4={gamma4}, 16/gamma4={bound4}, gap4={gap4}")
print(f"F(t)={F_t}")
print(f"gap(t)={gap_t}")
print("For t >= 3/2, 2*t^3-t^2-4 > 0 because it equals 1/2 at 3/2 and has derivative 2*t*(3*t-1)>0.")
