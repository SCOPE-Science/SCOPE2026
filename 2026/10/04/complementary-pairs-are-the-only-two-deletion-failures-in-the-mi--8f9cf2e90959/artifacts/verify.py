from itertools import combinations
from math import comb


def pop(x):
    return x.bit_count()


def dist(a, b, n):
    if a == b:
        return 0
    if a & b == 0:
        return 1
    if (a | b) == (1 << n) - 1:
        return 3
    return 2


def resolves(landmarks, n):
    seen = {}
    for a in range(1, (1 << n) - 1):
        sig = tuple(dist(a, b, n) for b in landmarks)
        if sig in seen:
            return False, (seen[sig], a)
        seen[sig] = a
    return True, None


for n in (6, 8):
    m = n // 2
    full = (1 << n) - 1
    middle = [a for a in range(1, full) if pop(a) == m]

    bad = []
    for i, j in combinations(range(len(middle)), 2):
        landmarks = [middle[k] for k in range(len(middle)) if k not in (i, j)]
        ok, collision = resolves(landmarks, n)
        complementary = middle[j] == (full ^ middle[i])
        assert ok == (not complementary), (n, middle[i], middle[j], collision)
        if not ok:
            bad.append((middle[i], middle[j]))
    assert len(bad) == len(middle) // 2

    for a, b in combinations(range(1, full), 2):
        distinguishers = [s for s in middle if dist(a, s, n) != dist(b, s, n)]
        if len(distinguishers) == 2:
            assert pop(a) == m and pop(b) == m and b == (full ^ a)
            assert set(distinguishers) == {a, b}
        else:
            assert len(distinguishers) >= 3

for m in range(3, 31):
    assert comb(m, m - 1) >= 3
    assert m + 1 >= 4
    assert comb(m + 1, m) - 1 >= 3

print("VERIFY_OK")
