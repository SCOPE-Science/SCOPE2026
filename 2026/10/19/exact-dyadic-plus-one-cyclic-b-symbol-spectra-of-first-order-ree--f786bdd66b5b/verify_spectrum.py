"""Direct census of cyclic b-symbol spectra of first-order binary RM codes.

No external dependencies. Each affine coefficient and offset is enumerated once.
The same linear code is generated in binary-index and reflected-Gray order.
"""
from collections import Counter


def expected(m, s):
    n = 1 << m
    l = 1 << s
    k = 1 << (m-s-1)
    out = Counter({0: 1, n: (1 << (m+1)) - 4*k + 3})
    for r in range(1, k):
        out[n//2 + l*r] = 4
    return out


def cyclic_window_weight(word, b):
    n = len(word)
    if not any(word):
        return 0
    doubled = word + word
    prefix = [0]
    for v in doubled:
        prefix.append(prefix[-1] + v)
    return sum(prefix[i+b] > prefix[i] for i in range(n))


def census(m, gray):
    n = 1 << m
    labels = [i ^ (i >> 1) if gray else i for i in range(n)]
    totals = [Counter() for _ in range(m)]
    for a in range(1 << m):
        base = [(a & i).bit_count() & 1 for i in labels]
        for c in range(2):
            word = [v ^ c for v in base]
            for s in range(m):
                b = (1 << s) + 1
                totals[s][cyclic_window_weight(word, b)] += 1
    return totals


def verify():
    for m in range(2, 10):
        straight = census(m, False)
        gray = census(m, True)
        for s in range(m):
            e = expected(m, s)
            assert straight[s] == e, (m, s, 'binary',straight[s],e)
            assert gray[s] == e, (m, s, 'gray',gray[s],e)
            assert sum(e.values()) == 1 << (m+1)
        print(f'RM_OK m={m} n={1<<m} checked_windows={m} codewords={1<<(m+1)}')
    print('VERIFY_OK all exact b-symbol spectra for m=2..9; natural and Gray order')


if __name__ == '__main__':
    verify()
