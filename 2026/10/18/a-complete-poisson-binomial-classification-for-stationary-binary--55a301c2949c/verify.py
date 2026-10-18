"""Exact-arithmetic checks of stationary binary Markov switch counts."""
from fractions import Fraction as F
from itertools import product


def law(a, b, m):
    probabilities = [b / (a + b), a / (a + b)]
    mass = [F(0) for _ in range(m + 1)]
    joints = [[F(0) for _ in range(m)] for _ in range(m)]
    for states in product((0, 1), repeat=m + 1):
        prob = probabilities[states[0]]
        switch = []
        for s, t in zip(states[:-1], states[1:]):
            prob *= ((1 - a) if t == 0 else a) if s == 0 else (b if t == 0 else (1 - b))
            switch.append(int(s != t))
        mass[sum(switch)] += prob
        for i in range(m):
            for j in range(m):
                joints[i][j] += prob * switch[i] * switch[j]
    return mass, joints


def main():
    tested = 0
    for ai, bi in [(1, 2), (1, 3), (2, 3), (4, 5), (3, 7), (7, 9), (2, 2), (1, 1)]:
        for aj, bj in [(1, 2), (2, 3), (3, 4), (4, 5)]:
            a, b = F(ai, bi), F(aj, bj)
            for m in range(1, 8):
                pmf, pair = law(a, b, m)
                mu, lam = 2 * a * b / (a + b), 1 - a - b
                c = a * b * (a - b) ** 2 / (a + b) ** 2
                assert sum(pmf) == 1
                assert sum(k * p for k, p in enumerate(pmf)) == m * mu
                var = sum(k * k * p for k, p in enumerate(pmf)) - (m * mu) ** 2
                ss = sum((m - h) * lam ** (h - 1) for h in range(1, m))
                assert var == m * mu * (1 - mu) + 2 * c * ss
                for i in range(m):
                    for j in range(i + 1, m):
                        assert pair[i][j] - mu**2 == c * lam ** (j - i - 1)
                if m >= 2:
                    assert (var > m * mu * (1 - mu)) == (a != b)
                if a == b:
                    from math import comb
                    assert all(pmf[k] == F(comb(m, k)) * a**k * (1 - a)**(m - k) for k in range(m + 1))
                tested += 1
    print(f'PASS: {tested} exact rational chain/horizon configurations')


if __name__ == '__main__':
    main()
