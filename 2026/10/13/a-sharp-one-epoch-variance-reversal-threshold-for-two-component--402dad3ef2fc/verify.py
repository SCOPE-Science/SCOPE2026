"""Reproduce exact two-step expectation identities with rational arithmetic."""
from fractions import Fraction as F
from random import Random
from itertools import product


def expectation(curvatures, step, offset, start, outcomes):
    def run(indices):
        x = start
        for index in indices:
            sgn = 1 if index == 1 else -1
            x = x - step * (curvatures[index - 1] * x + sgn * offset)
        return x * x
    return sum((run(seq) for seq in outcomes), F(0)) / len(outcomes)


def check():
    rng = Random(340042)
    rr = [(1, 2), (2, 1)]
    iid = list(product((1, 2), repeat=2))
    count_general = 0
    for _ in range(1000):
        a = F(rng.randrange(1, 31), rng.randrange(1, 18))
        b = F(rng.randrange(1, 31), rng.randrange(1, 18))
        step = F(rng.randrange(1, 31), rng.randrange(1, 35))
        c = F(rng.randrange(1, 11), rng.randrange(1, 11))
        e_rr = expectation((a, b), step, c, F(0), rr)
        e_iid = expectation((a, b), step, c, F(0), iid)
        assert e_rr - e_iid == step * step * c * c * (step * (a + b) - 2)
        count_general += 1

    count_all_start = 0
    for _ in range(500):
        lam = F(rng.randrange(1, 50), rng.randrange(1, 30))
        step = F(rng.randrange(1, 50), rng.randrange(1, 30))
        c = F(rng.randrange(1, 20), rng.randrange(1, 20))
        start = F(rng.randrange(-30, 31), rng.randrange(1, 20))
        e_rr = expectation((lam, lam), step, c, start, rr)
        e_iid = expectation((lam, lam), step, c, start, iid)
        assert e_rr - e_iid == 2 * step * step * c * c * (step * lam - 1)
        count_all_start += 1

    a = b = F(3, 2)
    eta = c = F(1)
    assert expectation((a, b), eta, c, F(0), rr) == F(9, 4)
    assert expectation((a, b), eta, c, F(0), iid) == F(5, 4)
    assert abs(1 - eta * a) < 1
    print('VERIFY_OK general=', count_general, 'all_start=', count_all_start, 'exact_witness=1')

if __name__ == '__main__':
    check()
