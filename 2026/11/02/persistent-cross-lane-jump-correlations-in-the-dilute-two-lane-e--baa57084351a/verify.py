"""Exact rational cross-current covariance checks for a two-lane jump model.

Standard-library only. The computational check is independent of the
closed-form electrical-network derivation in the accompanying manuscript.
Run: python3 verify.py
"""
from fractions import Fraction as F


def solve(a, b):
    """Gauss-Jordan solution with exact rational arithmetic."""
    n = len(a)
    aug = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(a)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if aug[i][k] != 0), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[k], aug[pivot] = aug[pivot], aug[k]
        t = aug[k][k]
        aug[k] = [v / t for v in aug[k]]
        for i in range(n):
            if i != k:
                factor = aug[i][k]
                if factor:
                    aug[i] = [u - factor * v for u, v in zip(aug[i], aug[k])]
    return [row[-1] for row in aug]


def formula(n, p, a):
    """Proposed closed finite-ring current covariance."""
    p, a = F(p), F(a)
    delta = a / 2
    w = p + delta
    R = F(n-2) / p + F(2) / w
    E = (delta**2 / n) * (
        F(2) * (1 - F(2, n))**2 / w
        + F(4 * (n-3) * (n-2) * (n-1), 3 * n*n) / p
    )
    return (p + a / n - F(n) / R + E) / 2


def independent_mixed_tilt(n, p, a):
    """Use independently differentiated tilted-generator eigenvalue."""
    p, a = F(p), F(a)
    jump_x = [p + a * F(d in (0, 1), 2) for d in range(n)]
    jump_y = [p + a * F(d in (0, n-1), 2) for d in range(n)]
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for d in range(n):
        Q[d][(d-1) % n] += jump_x[d]
        Q[d][(d+1) % n] += jump_y[d]
        Q[d][d] -= jump_x[d] + jump_y[d]
    # Flat stationary measure must follow from equal inflow and outflow.
    assert all(sum(Q[d]) == 0 for d in range(n))
    assert all(sum(Q[d][j] for d in range(n)) == 0 for j in range(n))
    A = [row[:] for row in Q]
    A[0] = [F(1) for _ in range(n)]
    def poisson(rate):
        mean = sum(rate) / n
        rhs = [mean - v for v in rate]
        rhs[0] = 0
        return solve(A, rhs)
    h_x = poisson(jump_x)
    h_y = poisson(jump_y)
    # Cross derivative of principal eigenvalue of two-field tilted Q.
    return sum(
        jump_x[d] * h_y[(d-1) % n]
        + jump_y[d] * h_x[(d+1) % n]
        for d in range(n)
    ) / n



def independent_full_two_lane_tilt(n, p, a):
    """Second check from the unreduced n-by-n physical position chain."""
    p, a = F(p), F(a)
    states = [(x, y) for x in range(n) for y in range(n)]
    labels = {xy: i for i, xy in enumerate(states)}
    size = n * n
    Q = [[F(0) for _ in range(size)] for _ in range(size)]
    jumps = [[] for _ in range(size)]
    rx, ry = [], []
    for i, (x, y) in enumerate(states):
        # Directly apply the occupation-based rate definition.
        rate_x = p + a * F(y in (x, (x+1) % n), 2)
        rate_y = p + a * F(x in (y, (y+1) % n), 2)
        rx.append(rate_x)
        ry.append(rate_y)
        for direction, rate, destination in (
            (0, rate_x, ((x+1) % n, y)),
            (1, rate_y, (x, (y+1) % n)),
        ):
            j = labels[destination]
            Q[i][j] += rate
            Q[i][i] -= rate
            jumps[i].append((direction, rate, j))
    assert all(sum(row) == 0 for row in Q)
    assert all(sum(row[j] for row in Q) == 0 for j in range(size))
    A = [row[:] for row in Q]
    A[0] = [F(1)] * size
    def poisson(rates):
        avg = sum(rates) / size
        rhs = [avg - v for v in rates]
        rhs[0] = 0
        return solve(A, rhs)
    hx, hy = poisson(rx), poisson(ry)
    return sum(
        rate * (hy[j] if direction == 0 else hx[j])
        for i in range(size)
        for direction, rate, j in jumps[i]
    ) / size

def run():
    checks = 0
    for n in range(3, 11):
        for p, a in ((F(1), F(1)), (F(1), F(-1, 2)),
                     (F(2), F(3, 2)), (F(1, 2), F(-1, 4)),
                     (F(3, 2), F(9, 2))):
            exact = independent_mixed_tilt(n, p, a)
            claimed = formula(n, p, a)
            assert exact == claimed, (n, p, a, exact, claimed)
            assert exact > 0
            checks += 1
        assert formula(n, F(1), F(0)) == 0
        checks += 1
    for n in range(3, 6):
        for p, a in ((F(1), F(1)), (F(1), F(-1, 2)), (F(2), F(3, 2))):
            raw = independent_full_two_lane_tilt(n, p, a)
            assert raw == formula(n, p, a), (n, p, a, raw, formula(n, p, a))
            checks += 1
    for n in (100, 1000, 10000):
        # Rational convergence with the required n->infinity order.
        value = formula(n, F(1), F(1))
        assert abs(value - F(1, 6)) < F(1, n)
        checks += 1
    print(f"PASS: {checks} exact rational statements; independent tilted-generator check")


if __name__ == "__main__":
    run()
