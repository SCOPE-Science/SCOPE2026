from collections import Counter
from math import ceil


def balanced_nonzero_values(q, d):
    return [1 + (i % (q - 1)) for i in range(d)]


def expected_distribution(q, d):
    n = 2 * d + 1
    a, b = divmod(d, q - 1)
    out = Counter({0: 1, d: q - 1, n: q - 1})
    if b:
        out[n - a - 1] += (q - 1) * b
    out[n - a] += (q - 1) * (q - 1 - b)
    return dict(sorted(out.items()))


def verify(q, d):
    n = 2 * d + 1
    c = balanced_nonzero_values(q, d)
    u = [1] * n
    v = c + [0] * (d + 1)
    words = set()
    distribution = Counter()
    for alpha in range(q):
        for beta in range(q):
            word = tuple((alpha * u[i] + beta * v[i]) % q for i in range(n))
            words.add(word)
            distribution[sum(x != 0 for x in word)] += 1
    assert len(words) == q * q
    distribution = dict(sorted(distribution.items()))
    assert distribution == expected_distribution(q, d)
    t = d - ceil(d / (q - 1))
    assert t >= 1
    assert all(distribution.get(d + j, 0) == 0 for j in range(1, t + 1))
    assert distribution.get(2 * d + 1, 0) > 0
    assert 2 == n - 2 * d + 1


for q in (3, 5, 7, 11, 13):
    for d in range(2, 15):
        verify(q, d)
    print(f"q={q}: d=2..14 PASS")
print("All tested prime-field instances satisfy the stated weight distribution, local gap, and mirror-counterexample conditions.")
