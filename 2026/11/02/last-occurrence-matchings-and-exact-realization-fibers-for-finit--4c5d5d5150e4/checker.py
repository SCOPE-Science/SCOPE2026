"""Independent exhaustive check of finite-chain flat strict implication operations.

Uses direct set-inclusion semantics, not the last-occurrence formula, for
full operation signatures. Standard-library only.
"""
from itertools import product, combinations, permutations
from collections import Counter
from math import factorial, comb


def last_vector(rows, n):
    last = [-1] * n
    for j, mask in enumerate(rows):
        if mask:
            t = (mask & -mask).bit_length() - 1
            last[t] = j
    return tuple(last)


def signature_direct(rows, n):
    out = []
    for a in range(n + 1):
        A = sum(1 << t for t in range(a, n))
        for b in range(n + 1):
            B = sum(1 << t for t in range(b, n))
            outmask = 0
            for w in range(n):
                ok = all((row & ~A) != 0 or (row & ~B) == 0
                         for row in rows[w:])
                if ok:
                    outmask |= 1 << w
            out.append(outmask)
    return tuple(out)


def signature_last(last, n):
    out = []
    for a in range(n + 1):
        for b in range(n + 1):
            greatest = max((last[t] for t in range(a, b)), default=-1)
            out.append(sum(1 << w for w in range(greatest + 1, n)))
    return tuple(out)


def predicted_fiber(last, n):
    forced = {j: t for t, j in enumerate(last) if j >= 0}
    result = 1
    for j in range(n):
        if j in forced:
            t = forced[j]
            result *= 1 << (n - t - 1)
        else:
            result *= 1 + sum((1 << (n - t - 1)) for t in range(n) if last[t] > j)
    return result


def rook_count(n):
    return sum(comb(n, k)**2 * factorial(k) for k in range(n + 1))


def all_partials(n):
    for k in range(n + 1):
        for domain in combinations(range(n), k):
            for image in permutations(range(n), k):
                last = [-1]*n
                for t, j in zip(domain, image):
                    last[t] = j
                yield tuple(last)


def check(n):
    observed = Counter()
    signatures = {}
    total = 0
    for rows in product(range(1 << n), repeat=n):
        last = last_vector(rows, n)
        direct = signature_direct(rows, n)
        via_last = signature_last(last, n)
        assert direct == via_last, (n, rows, last)
        prior = signatures.setdefault(last, direct)
        assert prior == direct
        observed[last] += 1
        total += 1
    expected = list(all_partials(n))
    assert set(observed) == set(expected)
    assert len(set(signatures.values())) == len(expected)
    for last in expected:
        assert observed[last] == predicted_fiber(last, n), (n, last, observed[last])
    assert len(observed) == rook_count(n)
    assert total == (1 << (n*n))
    assert sum(predicted_fiber(last, n) for last in expected) == total
    print(f'n={n}: relations={total}, operations={len(observed)}, exact_fibers={len(observed)}')

if __name__ == '__main__':
    for n in range(1,5):
        check(n)
    print('ALL_CHECKS_OK')
