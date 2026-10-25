"""Direct finite diagnostics for Fibonacci enumeration of PQN chains.

Python 3.10+; run: python checker.py. No external packages.
"""
from collections import Counter
from itertools import combinations_with_replacement, product


def all_weak_negations(n):
    # Enumerate every antitone n with n(0)=top and n(top)=0.
    for asc in combinations_with_replacement(range(n), n - 2):
        d = (n - 1,) + tuple(reversed(asc)) + (0,)
        if all(d[d[x]] >= x for x in range(n)):
            yield d


def operations(n, d):
    mult = [[min(x, y) if x > d[y] else 0 for y in range(n)]
            for x in range(n)]
    imp = [[max(z for z in range(n) if mult[x][z] <= y)
            for y in range(n)] for x in range(n)]
    return mult, imp


def original_nelson(n, d, mult, imp):
    return all(
        imp[min(imp[mult[x][x]][y], imp[mult[d[y]][d[y]]][d[x]])]
        [imp[x][y]] == n - 1
        for x, y in product(range(n), repeat=2)
    )


def strict_active_condition(n, d):
    return all(d[x-1] > d[x] for x in range(1, n - 1)
               if x <= d[x])


def recoveries(n, d):
    # Unique chain maximum-consistency and minimum-undeterminedness maps.
    circ = [int(min(x, d[x]) == 0) * (n-1) for x in range(n)]
    bullet = [0 if x == 0 or x == n-1 else n-1 for x in range(n)]
    mismatch = sum(bullet[x] != d[circ[x]] for x in range(n))
    return circ, bullet, mismatch


def check():
    fib = [0, 1]
    for j in range(2, 18):
        fib.append(fib[-1] + fib[-2])
    reports = []
    for n in range(2, 12):
        candidates = list(all_weak_negations(n))
        valid = []
        for d in candidates:
            mul, imp = operations(n, d)
            assert all(mul[x][y] == mul[y][x] for x,y in product(range(n), repeat=2))
            assert all(mul[mul[x][y]][z] == mul[x][mul[y][z]]
                       for x,y,z in product(range(n), repeat=3))
            assert all(imp[x][0] == d[x] for x in range(n))
            assert all((mul[x][z] <= y) == (z <= imp[x][y])
                       for x,y,z in product(range(n), repeat=3))
            criterion = strict_active_condition(n, d)
            original = original_nelson(n, d, mul, imp)
            assert original == criterion, (n, d)
            if original:
                valid.append(d)
        assert len(valid) == fib[n], (n, len(valid), fib[n])
        counts = Counter()
        for d in valid:
            _, _, mismatches = recoveries(n, d)
            counts[mismatches] += 1
            assert mismatches == n - 2 - d[1]
        if n >= 3:
            for j in range(n-1):
                r = n - 2 - j
                expected = 1 if r == 0 else fib[r]
                assert counts[j] == expected, (n,j,counts[j],expected)
            assert counts[0] == fib[n-2] if n >= 4 else counts[0] == 1
        else:
            assert counts == Counter({0:1})
        reports.append((n, len(candidates), len(valid), dict(sorted(counts.items()))))
    for n, weak, pqn, counts in reports:
        print('n=', n, 'WNM=', weak, 'PQN=', pqn, 'mismatch_spectrum=', counts)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    check()
