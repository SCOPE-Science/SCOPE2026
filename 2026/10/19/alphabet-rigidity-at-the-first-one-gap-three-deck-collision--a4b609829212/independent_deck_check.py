"""Independent dynamic-programming verification of selected full gap-two three-decks."""
from itertools import combinations
from random import Random

def direct(w, q):
    n = len(w)
    result = []
    for ell in (1, 2, 3):
        hist = [0] * (q ** ell)
        for positions in combinations(range(n), ell):
            if all(positions[j+1] - positions[j] >= 2 for j in range(ell - 1)):
                index = 0
                for i in positions:
                    index = q * index + w[i]
                hist[index] += 1
        result.extend(hist)
    return tuple(result)

def dynamic(w, q):
    n = len(w)
    end = {ell: [] for ell in (1, 2, 3)}
    for i, x in enumerate(w):
        a = [0] * q
        a[x] = 1
        end[1].append(a)
        for ell in (2, 3):
            b = [0] * (q ** ell)
            for j in range(i - 1):
                previous = end[ell - 1][j]
                for code, count in enumerate(previous):
                    b[code * q + x] += count
            end[ell].append(b)
    out = []
    for ell in (1, 2, 3):
        for code in range(q ** ell):
            out.append(sum(a[code] for a in end[ell]))
    return tuple(out)

pairs = [
    ('0001010000100', '0010000101000'),
    ('0101111010110', '0110101111010'),
    ('1001010000101', '1010000101001'),
    ('1101111010111', '1110101111011'),
]
checked = 0
for q in (2, 3):
    for a in range(q):
        for b in range(a + 1, q):
            for left, right in pairs:
                x = [a if c == '0' else b for c in left]
                y = [a if c == '0' else b for c in right]
                assert x != y
                assert direct(x, q) == direct(y, q)
                assert dynamic(x, q) == dynamic(y, q)
                assert direct(x, q) == dynamic(x, q)
                checked += 1
    random = Random(20261015 + q)
    for _ in range(250):
        w = [random.randrange(q) for _ in range(13)]
        assert direct(w, q) == dynamic(w, q)
        checked += 1
print('INDEPENDENT_DIRECT_AND_DP_PASSED', checked)
