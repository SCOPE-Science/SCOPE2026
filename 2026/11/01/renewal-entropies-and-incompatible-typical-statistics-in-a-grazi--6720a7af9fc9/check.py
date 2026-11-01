"""Finite algebraic and numerical checks for a rank-one interval renewal family.

The universal mathematical claims require the analytical proof in RESULT.md.
"""
from fractions import Fraction
from math import log


def f(m, x):
    return -m * x - 1 if x <= 0 else x - 1


def adjacency(m):
    A = [[0 for _ in range(m)] for _ in range(m)]
    for j in range(m):
        A[0][j] = 1
    for j in range(1, m):
        A[j][j - 1] = 1
    return A


def perron(m):
    left, right = 1.0, 2.0
    for _ in range(120):
        mid = (left + right) / 2
        if sum(mid ** (-r) for r in range(1, m + 1)) > 1.0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def verify(m):
    assert m >= 2
    A = adjacency(m)
    rho = [Fraction(2 * (m - j), m * (m + 1)) for j in range(m)]
    assert sum(rho) == 1
    for j in range(m):
        rhs = rho[0] / m
        if j < m - 1:
            rhs += rho[j + 1]
        assert rhs == rho[j], (m, j)
    # Exact piecewise affine branch tests at midpoints and endpoints.
    for r in range(1, m + 1):
        j = r - 1
        # Branch of I_0 satisfying f(x) in J_{r-1}=[r-2,r-1].
        a = Fraction(-r, m)
        b = Fraction(-(r - 1), m)
        # because f(x)=-m*x-1, branch endpoints x=-r/m and -(r-1)/m
        # produce f(a)=r-1, f(b)=r-2.
        assert a >= -1 and b <= 0 and a < b
        assert f(m, a) == r - 1
        assert f(m, b) == r - 2
        mid = (a + b) / 2
        t = mid
        for k in range(1, r):
            t = f(m, t)
            if k < r:
                assert t > 0, (m, r, k, t)
        t = f(m, t)
        assert Fraction(-1) < t < 0
        # Return map has orientation-reversing slope -m.
        ret_a = a
        ret_b = b
        for _ in range(r):
            ret_a = f(m, ret_a)
            ret_b = f(m, ret_b)
        # Boundary conventions may assign a different itinerary,
        # so only use interior points for the branch derivative.
        eps = Fraction(1, 7 * m)
        t0, t1 = a + eps, b - eps
        for _ in range(r):
            t0, t1 = f(m, t0), f(m, t1)
        assert t1 - t0 == -m * (b - a - 2 * eps)
        assert Fraction(-1) < t0 < 0 and Fraction(-1) < t1 < 0
    beta = perron(m)
    assert abs(sum(beta ** (-r) for r in range(1, m + 1)) - 1) < 1e-12
    assert abs(beta ** m - sum(beta ** k for k in range(m))) < 1e-8 * beta ** m
    weights = [beta ** (-r) for r in range(1, m + 1)]
    mean = sum(r * weights[r - 1] for r in range(1, m + 1))
    nu_cells = [sum(weights[j:]) / mean for j in range(m)]
    assert abs(sum(nu_cells) - 1) < 1e-12
    # Each J_j has mass equal to probability of a return block visiting it,
    # divided by the mean length of a block.
    assert abs(nu_cells[0] - 1.0 / mean) < 1e-12
    for j in range(m - 1):
        assert abs((nu_cells[j] - nu_cells[j + 1]) - weights[j] / mean) < 1e-12
    return beta, 2 * log(m) / (m + 1), log(beta), float(rho[0]), nu_cells[0]


if __name__ == "__main__":
    for m in range(2, 13):
        b, hm, ht, p0, q0 = verify(m)
        print(f"MARKOV_RENEWAL_PASS m={m} beta={b:.12f} h_phys={hm:.9f} h_top={ht:.9f} physical_J0={p0:.9f} max_J0={q0:.9f}")
    for m in (32, 128, 512):
        b, hm, ht, p0, q0 = verify(m)
        print(f"SCALE_PASS m={m} top={ht:.9f} physical={hm:.9f} max_J0={q0:.9f}")
    print("UNBOUNDED_RETURN_AND_ENTROPY_LIMITS_REQUIRE_ANALYTICAL_PROOF")
