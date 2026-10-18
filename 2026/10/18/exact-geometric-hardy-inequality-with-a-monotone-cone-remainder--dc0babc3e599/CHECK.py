"""Exact rational checks of a weighted discrete Hardy remainder identity."""
from fractions import Fraction
from random import Random


def expectation_and_remainder(rho, c, drops):
    q = Fraction(rho)
    mu = 1 / (1 - q)
    lam = (1 + q) / (1 - q) ** 2
    size = len(drops)
    def value(n):
        return c + sum(drops[n - 1 :], Fraction(0)) if n <= size else c
    def partial(n):
        return c * n + sum(k * d if k < n else n * d for k, d in enumerate(drops, 1))
    mean_square_f = sum((1 - q) * q ** (n - 1) * value(n) ** 2 for n in range(1, size + 1)) + q ** size * c * c
    mean_square_H = sum((1 - q) * q ** (n - 1) * partial(n) ** 2 for n in range(1, size + 1))
    bump = sum(k * d for k, d in enumerate(drops, 1))
    tail = q ** size * (c * c * (size * size + 2 * size * mu + lam) + 2 * c * bump * (size + mu) + bump * bump)
    mean_square_H += tail
    cross = sum(min(k, l) * (q ** min(k, l) + q ** max(k, l)) * drops[k - 1] * drops[l - 1]
                for k in range(1, size + 1) for l in range(1, size + 1))
    remainder = (2 * c * sum(k * q ** k * d for k, d in enumerate(drops, 1)) + cross) / (1 - q)
    return lam * mean_square_f - mean_square_H, remainder


def main():
    gen = Random(20261011)
    for run in range(600):
        rho = Fraction(gen.randint(1, 9), 10)
        c = Fraction(gen.randint(0, 14), gen.randint(1, 18))
        drops = [Fraction(gen.randint(0, 20), gen.randint(1, 25)) for _ in range(gen.randint(1, 15))]
        lhs, rhs = expectation_and_remainder(rho, c, drops)
        assert lhs == rhs, (run, lhs, rhs)
        assert rhs >= 0
        if any(d > 0 for d in drops):
            assert rhs > 0
        else:
            assert rhs == 0
        constant_lhs, constant_rhs = expectation_and_remainder(rho, c, [])
        assert constant_lhs == constant_rhs == 0
    print("PASS: 600 exact rational remainder and equality tests")


if __name__ == "__main__":
    main()
