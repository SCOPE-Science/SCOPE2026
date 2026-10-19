"""Exact-rational checks for an adaptive-confidence averaging model.

Independent of nonstandard libraries; run with Python 3: python verify.py.
Finite checks complement, and do not replace, the all-n proof.
"""
from fractions import Fraction as F
from random import Random


def update(x, c, gamma, delta):
    n = len(x)
    linked = {(i, j): abs(x[i] - x[j]) < c[i, j]
              for i in range(n) for j in range(i + 1, n)}
    neighbors = [[i] for i in range(n)]
    for (i, j), yes in linked.items():
        if yes:
            neighbors[i].append(j)
            neighbors[j].append(i)
    newx = [sum((x[j] for j in js), F(0)) / len(js) for js in neighbors]
    newc = {(i, j): (v + gamma * (1 - v) if linked[i, j] else delta * v)
            for (i, j), v in c.items()}
    return newx, newc, linked


def predict_first(n, delta, gap, c0, steps=120):
    # A returned integer is the first receptive time; None means no time
    # within the supplied exact-rational horizon (or no recovery possible).
    if delta <= F(1, n - 1):
        return None
    q = (n - 1) * delta
    val = F(1)
    for t in range(steps):
        if c0 * val > gap:
            return t
        val *= q
    raise AssertionError('bound for chosen test parameters exceeded')


def check_case(n, x0, delta, gamma):
    c0 = F(1, 2)
    gap = abs(x0[0] - x0[-1])
    assert gap >= c0
    assert all(abs(x0[i] - x0[j]) < c0
               for i in range(n) for j in range(i + 1, n)
               if (i, j) != (0, n - 1))
    c = {(i, j): c0 for i in range(n) for j in range(i + 1, n)}
    x = list(x0)
    first = predict_first(n, delta, gap, c0)
    horizon = max(14, (first + 3) if first is not None else 14)
    weighted = ((n - 1) * (x0[0] + x0[-1]) +
                n * sum(x0[1:-1], F(0))) / (n*n - 2)
    e0 = (x0[0] + x0[-1]) / 2
    m0 = sum(x0[1:-1], F(0)) / (n - 2)
    symmetric_eigen = F(-(n - 2), n * (n - 1))
    for t in range(horizon):
        observed = {(i, j) for i in range(n) for j in range(i + 1, n)
                    if abs(x[i] - x[j]) < c[i, j]}
        missing = (0, n - 1)
        if first is None or t < first:
            assert len(observed) == n*(n-1)//2 - 1 and missing not in observed
            assert x[-1] - x[0] == (x0[-1]-x0[0]) / ((n-1)**t)
            assert c[missing] == c0 * delta**t
            assert sum(x, F(0))/n == (weighted +
                F(2*(n-2), n*(n*n-2)) * symmetric_eigen**t * (e0-m0))
        else:
            assert len(observed) == n*(n-1)//2
            if t >= first + 1:
                assert len(set(x)) == 1
        x, c, _ = update(x, c, gamma, delta)
    if first is None:
        assert weighted >= 0 and weighted <= 1
    return first


def main():
    rng = Random(4021)
    cases = 0
    permanent = 0
    recovered = 0
    for n in range(3, 13):
        cutoff = F(1, n-1)
        deltas = [F(0), cutoff/2, cutoff, (cutoff+1)/2,
                  F(9,10), cutoff+F(1,1000)]
        for _ in range(4):
            xs = [F(0)] + [F(rng.randint(5,15), 40) for _ in range(n-2)] + [F(3,5)]
            for delta in deltas:
                for gamma in (F(0), F(1,4), F(1)):
                    first = check_case(n, xs, delta, gamma)
                    permanent += first is None
                    recovered += first is not None
                    cases += 1
    assert cases == 720 and permanent == 360 and recovered == 360
    n = 4
    x = [F(0), F(1,4), F(1,3), F(3,5)]
    assert check_case(n,x,F(1,3),F(1,4)) is None
    assert check_case(n,x,F(1,2),F(1,4)) == 1
    print('PASS:', cases, 'exact-rational trajectories;', permanent,
          'permanently missing-edge cases;', recovered, 'finite-recovery cases')
    print('PASS: n=4 sharp boundary 1/3, recovery at t=1 for delta=1/2')

if __name__ == '__main__':
    main()
