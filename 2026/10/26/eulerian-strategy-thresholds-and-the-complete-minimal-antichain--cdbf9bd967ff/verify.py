"""Check the uniform-preference backward-parking theorem by independent finite enumeration.

Run: python3 verify.py
Only Python standard library is required.
"""
from itertools import permutations, combinations, product
from math import comb, factorial


def park(n, m, quotas):
    """Run the physical 1..n parking process, stopping upon any failure."""
    occupied = set()
    for i in range(n):
        p = m
        if p in occupied:
            p = next((s for s in range(m - 1, max(1, m - quotas[i]) - 1, -1)
                      if s not in occupied), None)
            if p is None:
                p = next((s for s in range(m + 1, n + 1) if s not in occupied), None)
        if p is None:
            return False
        occupied.add(p)
    return len(occupied) == n


def statistic(quotas):
    """Threshold-greedy statistic independent of physical parking."""
    b = 0
    for r in quotas[1:]:
        if r >= b + 1:
            b += 1
    return b


def eulerian(n):
    row = [1]
    for i in range(2, n + 1):
        old = row
        row = [0] * i
        for k, v in enumerate(old):
            row[k] += (k + 1) * v
            row[k + 1] += (i - k - 1) * v
    return row


def permutation_via_insertion(quotas):
    """Statistic-preserving insertion bijection to ordinary permutations."""
    pi = [1]
    for size, r in enumerate(quotas[1:], 2):
        old_des = sum(pi[j] > pi[j+1] for j in range(len(pi)-1))
        preserve, increase = [], []
        for pos in range(size):
            trial = pi[:pos] + [size] + pi[pos:]
            new_des = sum(trial[j] > trial[j+1] for j in range(len(trial)-1))
            (preserve if new_des == old_des else increase).append(pos)
        assert len(preserve) == old_des + 1
        assert len(increase) == size - old_des - 1
        if r <= old_des:
            pos = preserve[r]
        else:
            pos = increase[r - old_des - 1]
        pi.insert(pos, size)
    return tuple(pi)


def all_quotas(n):
    return product(*(range(i) for i in range(1, n + 1)))


def minimal_witnesses(n, m):
    target = set()
    for inds in combinations(range(1, n), m - 1):
        r = [0] * n
        for j, i in enumerate(inds, 1):
            r[i] = j
        target.add(tuple(r))
    return target


def main():
    for n in range(1, 9):
        qs = list(all_quotas(n))
        by_score = [0] * n
        actual_perms = set()
        direct_success = {m: set() for m in range(1, n+1)}
        for q in qs:
            score = statistic(q)
            by_score[score] += 1
            pi = permutation_via_insertion(q)
            assert sum(pi[j] > pi[j+1] for j in range(n-1)) == score
            actual_perms.add(pi)
            for m in range(1, n+1):
                answer = park(n, m, q)
                assert answer == (score >= m-1), (n, m, q, answer, score)
                if answer:
                    direct_success[m].add(q)
        assert len(actual_perms) == factorial(n)
        assert by_score == eulerian(n)
        for m in range(1, n+1):
            successes = direct_success[m]
            assert len(successes) == sum(by_score[m-1:])
            minima = set()
            for q in successes:
                if all((q[:i] + (q[i]-1,) + q[i+1:]) not in successes
                       for i in range(1, n) if q[i] > 0):
                    minima.add(q)
            expected_minima = minimal_witnesses(n, m)
            assert minima == expected_minima
            assert len(minima) == comb(n-1, m-1)
        print('n=%d; %d strategies; Eulerian=%s; success-by-m=%s; minima-by-m=%s; OK' % (
            n, factorial(n), by_score,
            [len(direct_success[m]) for m in range(1,n+1)],
            [comb(n-1,m-1) for m in range(1,n+1)]))
    for n in range(9, 101):
        row = eulerian(n)
        assert sum(row) == factorial(n)
        assert row == list(reversed(row))
    print('Eulerian recurrence and symmetry tested through n=100')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
