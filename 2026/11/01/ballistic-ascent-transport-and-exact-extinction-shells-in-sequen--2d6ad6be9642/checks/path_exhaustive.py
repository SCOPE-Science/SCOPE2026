#!/usr/bin/env python3
"""Reproducibility: enumerates each initial bit word and directly updates the path."""
from collections import Counter


def step(word):
    y = list(word)
    n = len(y)
    for i in range(n):
        a = y[i - 1] if i else 0
        b = y[i]
        c = y[i + 1] if i + 1 < n else 0
        s = a + b + c
        y[i] = int(s >= (3 if b else 1))
    return tuple(y)


def ascents(x):
    return tuple(i + 1 for i in range(len(x) - 1) if x[i] == 0 and x[i + 1] == 1)


def predicted_time(x):
    a = ascents(x)
    return (1 + max(a)) if a else int(any(x))


def check(n):
    hist = Counter()
    for mask in range(1 << n):
        x = tuple((mask >> j) & 1 for j in range(n))
        y = step(x)
        assert ascents(y) == tuple(j - 1 for j in ascents(x) if j > 1), (n, x, y)
        t = 0
        z = x
        while any(z):
            z = step(z)
            t += 1
            assert t <= n, (n, x)
        assert t == predicted_time(x), (n, x, t, predicted_time(x))
        hist[t] += 1
    expected = {0: 1, 1: n}
    expected.update({t: (n - t + 1) * (1 << (t - 2)) for t in range(2, n + 1)})
    assert dict(hist) == expected, (n, hist, expected)
    s = sum(t * c for t, c in hist.items())
    assert s == (n - 2) * (1 << n) + n + 2, (n, s)
    return len(range(1 << n)), hist[n]


def main():
    total = 0
    for n in range(2, 16):
        states, worst = check(n)
        total += states
        print(f'n={n} states={states} maximal_time_states={worst}')
    print(f'PASS: 2<=n<=15; total_states={total}; full orbit/time and ascent-shift checks')


if __name__ == '__main__':
    main()
