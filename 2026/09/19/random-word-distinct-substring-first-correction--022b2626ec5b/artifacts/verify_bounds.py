from itertools import product
from math import floor, log


def distinct_substrings(word):
    n = len(word)
    return len({word[i:j] for i in range(n) for j in range(i + 1, n + 1)})


def deficit_bounds(n, d):
    m = floor(log(n, d))
    prefix = m * (n + 1) - m * (m + 1) / 2
    lower = prefix - d * (d**m - 1) / (d - 1)
    tail = sum(
        ((n - k + 1) * (n - k) / 2) * d ** (-k)
        for k in range(m + 1, n + 1)
    )
    upper = prefix + tail
    return m, lower, upper


def exact_expectation(n, d):
    total = 0
    for word in product(range(d), repeat=n):
        total += distinct_substrings(word)
    return total / (d**n)


for d, nmax in [(2, 16), (3, 10)]:
    print(f"alphabet={d}")
    for n in range(2, nmax + 1):
        expected = exact_expectation(n, d)
        positional = n * (n + 1) / 2
        deficit = positional - expected
        m, lower, upper = deficit_bounds(n, d)
        assert lower <= deficit + 1e-12
        assert deficit <= upper + 1e-12
        ratio = deficit / (n * log(n, d))
        print(
            f"n={n:2d} m={m:2d} E[D]={expected:.10f} "
            f"R={deficit:.10f} R/(n log_d n)={ratio:.8f} "
            f"bounds=[{lower:.10f},{upper:.10f}]"
        )
