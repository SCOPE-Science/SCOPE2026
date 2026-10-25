"""Reproducible finite tests for the square fixed-cardinality assignment width loss.

Requirements: Python 3, NumPy, SciPy. No external files or network needed.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linear_sum_assignment
from scipy.stats import norm


def maximum_assignment(a, k):
    n = a.shape[0]
    assert a.shape == (n, n) and 1 <= k <= n
    premium = 3 * n * (1 + np.max(np.abs(a)))
    # Each dummy column is forced into a maximizing assignment. The remaining
    # k choices are a maximum-weight matching of cardinality exactly k.
    extended = np.column_stack((a, np.full((n, n - k), premium)))
    rows, columns = linear_sum_assignment(extended, maximize=True)
    mask = columns < n
    assert int(np.count_nonzero(mask)) == k
    return float(a[rows[mask], columns[mask]].sum())


def brute_force(a, k):
    n = a.shape[0]
    return max(sum(a[i, j] for i, j in zip(rr, cc))
               for rr in itertools.combinations(range(n), k)
               for c0 in itertools.combinations(range(n), k)
               for cc in itertools.permutations(c0))


def support_loss(a, k):
    upper = float(np.partition(a.ravel(), -k)[-k:].sum())
    return upper - maximum_assignment(a, k)


def one_sided_agreement(n, k):
    return math.exp(sum(2 * math.log1p(-j/n) - math.log1p(-j/(n*n))
                        for j in range(k)))


def main():
    rng = np.random.default_rng(314159)
    checked = 0
    for n in range(2, 5):
        for k in range(1, n+1):
            for _ in range(25):
                a = rng.normal(size=(n, n))
                assert abs(maximum_assignment(a, k)-brute_force(a, k)) < 1e-9
                checked += 1
    print('brute-force optimizer comparisons passed:', checked)

    rng2 = np.random.default_rng(123)
    repaired = 0
    for n in (10, 20, 50):
        for _ in range(500):
            k = max(2, round(n**.5))
            a = rng2.normal(size=(n,n))
            indices = np.argsort(a.ravel())[::-1]
            positions = [divmod(int(i), n) for i in indices[:k+10]]
            pairs = [(i,j) for i in range(k) for j in range(i+1,k)
                     if positions[i][0] == positions[j][0]
                     or positions[i][1] == positions[j][1]]
            endpoints = [v for e in pairs for v in e]
            if len(set(endpoints)) < len(endpoints):
                continue
            count = len(pairs)
            kept = set(range(k)) - {j for i,j in pairs}
            chosen = list(kept) + list(range(k,k+count))
            rows = [positions[i][0] for i in chosen]
            cols = [positions[i][1] for i in chosen]
            if len(set(rows)) < len(rows) or len(set(cols)) < len(cols):
                continue
            descending = a.ravel()[indices]
            defect = descending[:k].sum() - maximum_assignment(a, k)
            lower = sum(descending[j]-descending[k-1] for i,j in pairs)
            upper = sum(descending[j]-descending[k+count-1] for i,j in pairs)
            assert lower-1e-8 <= defect <= upper+1e-8
            repaired += 1
    print('collision-repair sandwiches passed:', repaired)

    rng3 = np.random.default_rng(271828)
    for n, reps in ((40,350),(100,350),(180,180)):
        k = round(n**.5)
        t = norm.isf(k/(n*n))
        samples = []
        zeros = 0
        for _ in range(reps):
            a = rng3.normal(size=(n,n))
            dp = support_loss(a,k)
            dn = support_loss(-a,k)
            samples.append(t*(dp+dn))
            zeros += dp < 1e-9 and dn < 1e-9
        print('n={} k={} reps={} zero_fraction={:.6f} scaled_mean={:.6f}'.format(
            n,k,reps,zeros/reps,float(np.mean(samples))))
    print('exact one-sided equality probability n=100 k=10:',
          '{:.10f}'.format(one_sided_agreement(100,10)))

if __name__ == '__main__':
    main()
