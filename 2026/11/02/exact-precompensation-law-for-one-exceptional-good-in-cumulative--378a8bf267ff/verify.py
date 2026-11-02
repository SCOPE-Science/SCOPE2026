"""Independent exact-arithmetic checks for the one-exceptional-item theorem.

Requires only Python 3's standard library. All tested finite domains are
reported explicitly; the theorem for arbitrary parameters uses a proof.
"""
from fractions import Fraction
from itertools import product


def brute_opt(a, b, h):
    """Exact shortest-path DP over ALL reachable signed bundle gaps."""
    paths = {Fraction(0): Fraction(0)}
    for weight in [Fraction(1)] * a + [h] + [Fraction(1)] * b:
        next_paths = {}
        for gap, cost in paths.items():
            for successor in (gap + weight, gap - weight):
                candidate = cost + abs(successor)
                if successor not in next_paths or candidate < next_paths[successor]:
                    next_paths[successor] = candidate
        paths = next_paths
    return min(paths.values())


def lattice_distance(x, t):
    q = (x + t) / 2
    k0 = min(t, max(0, q.numerator // q.denominator))
    k1 = min(t, k0 + 1)
    return min(abs(x + t - 2 * k0), abs(x + t - 2 * k1))


def formula_opt(a, b, h):
    """Exact structural formula, computed independently of brute_opt."""
    return min(
        Fraction(a + j * j, 2) + abs(h - j)
        + sum((lattice_distance(abs(h - j), t) for t in range(1, b + 1)), Fraction(0))
        for j in range(-a, a + 1, 2)
    )


def long_horizon_formula(a, b, h):
    assert isinstance(h, int) and h >= 1 and a >= h and b >= h
    parity = (a + b - h) % 2
    nearest_square = min((Fraction(h, 2) - j) ** 2 for j in range(a % 2, h + 1, 2))
    return Fraction(a + b + parity, 2) + Fraction(h * h, 4) + nearest_square


def symmetric_family(h):
    # Exceptional value H=2h, a=b=2h. Greedy balances all unit prefixes.
    exceptional = 2 * h
    optimum = 2 * h + 2 * ((h * h + 1) // 2)
    greedy = 2 * h + 2 * h * h
    return Fraction(optimum), Fraction(greedy)



def constructive_witness(a, b, h):
    """Produce a full indivisible allocation using the proof's path pattern."""
    choices = []
    for j in range(-a, a + 1, 2):
        score = Fraction(a + j * j, 2) + abs(h - j)
        score += sum((lattice_distance(abs(h - j), t) for t in range(1, b + 1)), Fraction(0))
        choices.append((score, j))
    optimum, j = min(choices)
    signs = []
    for _ in range((a - abs(j)) // 2):
        signs.extend((+1, -1))
    signs.extend([-1 if j > 0 else +1] * abs(j))
    signs.append(+1)
    gap = -j + h
    for _ in range(b):
        direction = -1 if gap > 0 else +1
        gap += direction
        signs.append(direction)
    assert len(signs) == a + b + 1
    gap = Fraction(0)
    cost = Fraction(0)
    for sign, weight in zip(signs, [Fraction(1)] * a + [h] + [Fraction(1)] * b):
        gap += sign * weight
        cost += abs(gap)
    assert cost == optimum, (a, b, h, j, cost, optimum)
    return cost

def run():
    rat_values = [Fraction(n, d) for n, d in
                  [(1, 1), (6, 5), (3, 2), (2, 1), (7, 3), (3, 1),
                   (7, 2), (4, 1), (11, 2), (8, 1), (13, 1)]]
    direct = 0
    for a, b, h in product(range(9), range(9), rat_values):
        observed = brute_opt(a, b, h)
        predicted = formula_opt(a, b, h)
        assert observed == predicted, (a, b, h, observed, predicted)
        assert constructive_witness(a, b, h) == observed
        direct += 1

    long_cases = 0
    for h in range(1, 31):
        for a in range(h, h + 4):
            for b in range(h, h + 4):
                exact = formula_opt(a, b, Fraction(h))
                midpoint = long_horizon_formula(a, b, h)
                assert exact == midpoint, (a, b, h, exact, midpoint)
                long_cases += 1

    symmetric = 0
    for h in range(1, 61):
        exact = formula_opt(2 * h, 2 * h, Fraction(2 * h))
        optimum, greedy = symmetric_family(h)
        assert exact == optimum, (h, exact, optimum)
        assert greedy >= optimum
        symmetric += 1

    for h in range(1, 7):
        optimum, greedy = symmetric_family(h)
        assert brute_opt(2 * h, 2 * h, Fraction(2 * h)) == optimum

    print('VERIFY_OK direct_dynamic_checks=%d integer_midpoint_checks=%d '
          'symmetric_witnesses=%d' % (direct, long_cases, symmetric))


if __name__ == '__main__':
    run()
