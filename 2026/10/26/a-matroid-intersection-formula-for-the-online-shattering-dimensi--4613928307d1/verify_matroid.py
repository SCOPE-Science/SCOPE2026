"""Independent exhaustive finite checks of a matroid-basis learning identity.
No external files, services, or nonstandard packages are required.
Run: python3 verify_matroid.py
"""
from itertools import combinations
from functools import lru_cache
import random


def bits(m, k):
    return [sum(1 << i for i in C) for C in combinations(range(m), k)]


def is_matroid_bases(B, m):
    if not B or len({b.bit_count() for b in B}) != 1:
        return False
    SS = set(B)
    for b in B:
        for c in B:
            x = b & ~c
            y = c & ~b
            while x:
                e = x & -x; x ^= e
                if not any(((b ^ e) | f) in SS for f in powers_of_one_bits(y)):
                    return False
    return True


def powers_of_one_bits(x):
    while x:
        b = x & -x; x -= b
        yield b


def vc_dimension(B, m):
    result = 0
    for mask in range(1 << m):
        F = [i for i in range(m) if (mask >> i) & 1]
        n = len(F)
        patterns = {sum(((b >> i) & 1) << k for k, i in enumerate(F)) for b in B}
        if len(patterns) == 1 << n:
            result = max(result, n)
    return result


def ld_dimension(B, m):
    if len(B) <= 1:
        return 0
    # Version space represented by bits in an integer; no repeated queries are needed.
    one = [sum(1 << j for j, b in enumerate(B) if (b >> i) & 1) for i in range(m)]
    full = (1 << len(B)) - 1
    @lru_cache(None)
    def rec(S):
        best = 0
        if S.bit_count() <= 1:
            return best
        for test in one:
            a = S & test
            b = S & (full ^ test)
            if a and b:
                best = max(best, 1 + min(rec(a), rec(b)))
        return best
    return rec(full)


def rank_from_bases(B, A):
    return max((b & A).bit_count() for b in B)


def nu_rank(B, m):
    r = B[0].bit_count()
    return min(2 * rank_from_bases(B, A) + m - A.bit_count() - r for A in range(1 << m))


def nu_common(B, m):
    # Common independence of M and M*: F is independent iff F subsets a base,
    # and F is independent in M* iff some base is disjoint from F.
    return max((F.bit_count() for F in range(1 << m) if
                any((F & b) == F for b in B) and any((F & b) == 0 for b in B)), default=0)


def check_minor_split(B, m):
    nu = nu_common(B, m)
    for i in range(m):
        be = [b for b in B if (b >> i) & 1]
        bn = [b for b in B if not ((b >> i) & 1)]
        if not (be and bn):
            continue
        compact = lambda b: (b & ((1 << i) - 1)) | ((b >> (i + 1)) << i)
        be = [compact(b) for b in be]
        bn = [compact(b) for b in bn]
        nbe = nu_common(be, m - 1)
        nbn = nu_common(bn, m - 1)
        assert min(nbe, nbn) == nu - 1, (B, m, i, nu, nbe, nbn)


def examine(B, m):
    a = vc_dimension(B, m)
    b = ld_dimension(B, m)
    c = nu_rank(B, m)
    d = nu_common(B, m)
    assert a == b == c == d, (m, B, a, b, c, d)
    check_minor_split(B, m)
    return a


def all_small_matroids():
    counts = []
    for m in range(6):
        cnt = 0
        hist = {}
        for r in range(m + 1):
            candidates = bits(m, r)
            for family_code in range(1, 1 << len(candidates)):
                B = [b for k, b in enumerate(candidates) if (family_code >> k) & 1]
                if is_matroid_bases(B, m):
                    d = examine(B, m)
                    hist[d] = hist.get(d, 0) + 1
                    cnt += 1
        counts.append((m, cnt, hist))
        print('ALL_MATROIDS m=%s count=%s dims=%s' % (m, cnt, hist), flush=True)
    return counts


def is_independent_linear(column_vectors):
    basis = {}
    for x in column_vectors:
        while x:
            highest = x.bit_length() - 1
            if highest in basis:
                x ^= basis[highest]
            else:
                basis[highest] = x
                break
        if not x:
            return False
    return True


def linear_matroids():
    rng = random.Random(21102026)
    cnt = 0
    for m in range(4, 11):
        for _ in range(48):
            dimension = rng.randrange(1, m)
            cols = [rng.randrange(0, 1 << dimension) for _ in range(m)]
            rank = max((len(C) for k in range(m + 1) for C in combinations(range(m), k)
                        if is_independent_linear([cols[i] for i in C])), default=0)
            B = [sum(1 << i for i in C) for C in combinations(range(m), rank)
                 if is_independent_linear([cols[i] for i in C])]
            examine(B, m)
            cnt += 1
    print('RANDOM_GF2_LINEAR_MATROIDS', cnt)
    return cnt


if __name__ == '__main__':
    counts = all_small_matroids()
    random_count = linear_matroids()
    print('ALL_MATROID_IDENTITY_CHECKS_PASS', counts[-1][1], random_count)
