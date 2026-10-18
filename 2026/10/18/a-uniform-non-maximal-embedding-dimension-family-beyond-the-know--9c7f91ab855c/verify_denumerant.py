"""Reproducible finite tests for a family of three-consecutive coin systems.

The printed finite tests do not replace the universal symbolic argument.
Python 3, standard library only.
"""

def exact_by_length(a, n):
    total = 0
    for t in range(n // a + 1):
        u = n - a * t
        lo = max(0, u - t)
        hi = u // 2
        if hi >= lo:
            total += hi - lo + 1
    return total


def dynamic_counts(a, max_n):
    out = [0] * (max_n + 1)
    out[0] = 1
    for coin in (a, a + 1, a + 2):
        for n in range(coin, max_n + 1):
            out[n] += out[n - coin]
    return out


def check():
    checks = 0
    for a in range(7, 101):
        k = a // 2
        p = k + 5
        mu = (a + 2)**2 - 2
        n0 = mu - a
        max_n = mu + 2*a + 4
        counts = dynamic_counts(a, max_n)
        assert counts[mu] == p + 1
        assert all(counts[n] <= p for n in range(mu))
        for n in range(n0, mu + 5):
            assert counts[n] == exact_by_length(a, n)
            checks += 1
        if a % 2 == 0:
            x = y = (a + 2)**2
        else:
            x = (a + 2)**2 - 1
            y = (a + 2)**2
        hole = x + y - mu
        assert counts[x] == counts[y] == p + 1
        assert counts[hole] == p
        checks += 4
        # Full-window conductor and generator check, independent of the theorem's proof.
        N = mu + 2 * a + 4
        members = {0} | {n for n in range(1, N + 1) if counts[n] > p}
        minimal = []
        for n in range(1, mu + a + 7):
            if n in members and not any((n - g) in members for g in minimal):
                minimal.append(n)
        assert len(minimal) < mu
        checks += 1
    print('PASS', checks, 'formula-and-DP comparisons and invariant checks, a=7..100')


if __name__ == '__main__':
    check()
