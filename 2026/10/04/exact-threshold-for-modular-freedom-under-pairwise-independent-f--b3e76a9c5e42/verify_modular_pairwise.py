#!/usr/bin/env python3
from fractions import Fraction

def criterion(n, q, r):
    if not (q >= 2 and n >= 2 and 0 <= r < q):
        return False
    if n < r:
        return False
    N = (n - r) // q
    m = Fraction(n - 2*r, 2*q)
    v = Fraction(n, 4*q*q)
    if not (0 <= m <= N):
        return False
    a = m.numerator // m.denominator
    delta = m - a
    vmin = delta * (1 - delta)
    vmax = m * (N - m)
    return vmin <= v <= vmax

def construct_K(n, q, r):
    assert criterion(n, q, r)
    N = (n - r) // q
    m = Fraction(n - 2*r, 2*q)
    v = Fraction(n, 4*q*q)
    a = m.numerator // m.denominator
    delta = m - a
    vmin = delta * (1 - delta)
    vmax = m * (N - m)

    low = {}
    low[a] = low.get(a, Fraction(0)) + (1 - delta)
    low[a+1] = low.get(a+1, Fraction(0)) + delta
    low = {j:w for j,w in low.items() if w}

    if N == 0:
        high = {0: Fraction(1)}
    else:
        high = {0: 1 - m/Fraction(N), N: m/Fraction(N)}
        high = {j:w for j,w in high.items() if w}

    if vmax == vmin:
        t = Fraction(0)
    else:
        t = (v - vmin) / (vmax - vmin)
    assert 0 <= t <= 1

    J = {}
    for j,w in low.items():
        J[j] = J.get(j, Fraction(0)) + (1-t)*w
    for j,w in high.items():
        J[j] = J.get(j, Fraction(0)) + t*w
    J = {j:w for j,w in J.items() if w}

    K = {r + q*j: w for j,w in J.items()}
    return K

def check_distribution(n, q, r, K):
    assert sum(K.values(), Fraction(0)) == 1
    assert all(w >= 0 for w in K.values())
    assert all(0 <= k <= n for k in K)
    assert all(k % q == r for k in K)
    EK = sum(Fraction(k)*w for k,w in K.items())
    EKK1 = sum(Fraction(k*(k-1))*w for k,w in K.items())
    assert EK == Fraction(n, 2)
    assert EKK1 == Fraction(n*(n-1), 4)
    assert EK / n == Fraction(1,2)
    assert EKK1 / (n*(n-1)) == Fraction(1,4)

def bad_residue_at_boundary(q):
    if q % 2:
        return q - 1
    return q//2 - 1

def run():
    feasible_cases = 0
    infeasible_cases = 0
    construction_checks = 0
    threshold_checks = 0

    for q in range(2, 31):
        upper = q*q + 12
        for n in range(2, upper + 1):
            for r in range(q):
                ok = criterion(n, q, r)
                if ok:
                    feasible_cases += 1
                    K = construct_K(n, q, r)
                    check_distribution(n, q, r, K)
                    construction_checks += 1
                else:
                    infeasible_cases += 1

    for q in range(2, 61):
        start = q*q - 1
        for n in range(start, start + 20):
            assert all(criterion(n, q, r) for r in range(q))
            threshold_checks += q
        nbad = q*q - 2
        rbad = bad_residue_at_boundary(q)
        assert not criterion(nbad, q, rbad)
        threshold_checks += 1

    print(
        "VERIFY_OK "
        f"feasible_cases={feasible_cases} "
        f"infeasible_cases={infeasible_cases} "
        f"construction_checks={construction_checks} "
        f"threshold_checks={threshold_checks}"
    )

if __name__ == "__main__":
    run()
