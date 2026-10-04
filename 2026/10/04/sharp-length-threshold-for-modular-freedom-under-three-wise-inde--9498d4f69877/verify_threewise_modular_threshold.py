#!/usr/bin/env python3
from fractions import Fraction

def add_mass(D, x, p):
    D[x] = D.get(x, Fraction(0)) + p

def central_moments(D):
    total = sum(D.values(), Fraction(0))
    mean = sum(Fraction(x) * p for x, p in D.items())
    v2 = sum((Fraction(x) - mean) ** 2 * p for x, p in D.items())
    v3 = sum((Fraction(x) - mean) ** 3 * p for x, p in D.items())
    return total, mean, v2, v3

def low_law(m, N):
    a = m.numerator // m.denominator
    d = m - a

    if d == 0:
        return {a: Fraction(1)}
    if d == Fraction(1, 2):
        return {a: Fraction(1, 2), a + 1: Fraction(1, 2)}

    if d < Fraction(1, 2):
        den = a + 3 * d - 1
        assert a >= 1 and den > 0
        p0 = d * (1 - d) * (1 - 2 * d) / (a * (a + 1) * den)
        pa = (a + d) * (1 - d) * (a + 2 * d - 1) / (a * den)
        pb = d * (a + d) * (a + 2 * d) / ((a + 1) * den)
        D = {0: p0, a: pa, a + 1: pb}
        return {x: p for x, p in D.items() if p}

    # Reflection reduces the case d>1/2 to fractional part 1-d<1/2.
    reflected = low_law(Fraction(N) - m, N)
    return {N - x: p for x, p in reflected.items()}

def high_law(m, N):
    a = m.numerator // m.denominator
    d = m - a
    assert a >= 1
    assert a + 2 <= N

    # Two mean-matched two-point laws:
    # A on {a-1,a+1}, B on {a,a+2}.  Their third centered
    # moments have opposite signs.  The displayed mixture cancels them.
    alpha = (2 - d) / 3
    beta = (1 + d) / 3

    D = {}
    add_mass(D, a - 1, alpha * (1 - d) / 2)
    add_mass(D, a + 1, alpha * (1 + d) / 2)
    add_mass(D, a, beta * (2 - d) / 2)
    add_mass(D, a + 2, beta * d / 2)
    return {x: p for x, p in D.items() if p}

def mix(A, B, theta):
    D = {}
    for x, p in A.items():
        add_mass(D, x, (1 - theta) * p)
    for x, p in B.items():
        add_mass(D, x, theta * p)
    return {x: p for x, p in D.items() if p}

def low_variance(m, N):
    a = m.numerator // m.denominator
    d = m - a
    if d == 0:
        return Fraction(0)
    if d == Fraction(1, 2):
        return Fraction(1, 4)
    if d < Fraction(1, 2):
        return d * (1 - d) * m / (m - (1 - 2 * d))
    x = Fraction(N) - m
    return d * (1 - d) * x / (x - (2 * d - 1))

def build_residue_vertex(q, r):
    n = q * q + 2
    N = (n - r) // q
    m = Fraction(n - 2 * r, 2 * q)
    target_v = Fraction(n, 4 * q * q)

    L = low_law(m, N)
    H = high_law(m, N)
    sL, mL, vL, c3L = central_moments(L)
    sH, mH, vH, c3H = central_moments(H)

    assert sL == sH == 1
    assert mL == mH == m
    assert c3L == c3H == 0
    assert vL == low_variance(m, N)
    assert vL <= target_v <= vH
    assert vH >= Fraction(2, 3)

    theta = (target_v - vL) / (vH - vL)
    J = mix(L, H, theta)
    s, mJ, vJ, c3J = central_moments(J)
    assert s == 1
    assert mJ == m
    assert vJ == target_v
    assert c3J == 0
    assert len(J) <= 5
    assert all(0 <= j <= N for j in J)

    K = {r + q * j: p for j, p in J.items()}
    assert sum(K.values(), Fraction(0)) == 1
    assert all(0 <= k <= n for k in K)
    assert all(k % q == r for k in K)

    e1 = sum(Fraction(k) * p for k, p in K.items())
    f2 = sum(Fraction(k * (k - 1)) * p for k, p in K.items())
    f3 = sum(Fraction(k * (k - 1) * (k - 2)) * p for k, p in K.items())
    assert e1 == Fraction(n, 2)
    assert f2 == Fraction(n * (n - 1), 4)
    assert f3 == Fraction(n * (n - 1) * (n - 2), 8)
    return len(J)

def pairwise_obstruction_residue(q, n):
    # Choose a residue for which frac((n-2r)/(2q)) is either 1/2
    # or 1/(2q) away from 1/2.
    c = q if (n - q) % 2 == 0 else q - 1
    return ((n - c) // 2) % q

def check_pairwise_lower_obstruction(q, n):
    r = pairwise_obstruction_residue(q, n)
    m = Fraction(n - 2 * r, 2 * q)
    d = m - (m.numerator // m.denominator)
    required_v = Fraction(n, 4 * q * q)
    # Every integer-valued variable with mean m has variance at least d(1-d).
    assert d * (1 - d) > required_v

def explicit_boundary_residue(q, n):
    if q % 2 == 0:
        if n == q * q - 1:
            return q // 2 - 1
        if n == q * q:
            return q // 2 - 1
        if n == q * q + 1:
            return q // 2
    else:
        if n == q * q - 1:
            return 0
        if n == q * q:
            return 1
        if n == q * q + 1:
            return 0
    raise AssertionError("unexpected boundary")

def check_third_moment_boundary_obstruction(q, n):
    r = explicit_boundary_residue(q, n)
    N = (n - r) // q
    m = Fraction(n - 2 * r, 2 * q)
    required_v = Fraction(n, 4 * q * q)
    assert low_variance(m, N) > required_v

def run():
    construction_cases = 0
    support_points = 0
    for q in range(4, 201):
        for r in range(q):
            support_points += build_residue_vertex(q, r)
            construction_cases += 1

    pairwise_obstruction_checks = 0
    for q in range(4, 81):
        for n in range(3, q * q - 1):
            check_pairwise_lower_obstruction(q, n)
            pairwise_obstruction_checks += 1

    third_moment_boundary_checks = 0
    for q in range(4, 201):
        for n in (q * q - 1, q * q, q * q + 1):
            check_third_moment_boundary_obstruction(q, n)
            third_moment_boundary_checks += 1

    print(
        "VERIFY_OK "
        f"construction_cases={construction_cases} "
        f"support_points={support_points} "
        f"pairwise_obstruction_checks={pairwise_obstruction_checks} "
        f"third_moment_boundary_checks={third_moment_boundary_checks}"
    )

if __name__ == "__main__":
    run()
