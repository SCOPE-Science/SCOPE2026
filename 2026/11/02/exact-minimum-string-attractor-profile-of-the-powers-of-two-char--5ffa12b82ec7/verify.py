"""Finite checks accompanying the exact string-attractor profile theorem.

Only the mathematical argument establishes the infinite assertion.
Run with Python 3, using only the standard library.
"""

from itertools import combinations


def word(n):
    return ''.join('1' if (i + 1) & i == 0 else '0' for i in range(n))


def formula(n):
    if n <= 2:
        return 1
    if n <= 5:
        return 2
    j = 0
    while 24 * (4 ** j) <= n:
        j += 1
    return j + 3 if n >= 6 else 2


def proposed(n):
    if n <= 2:
        return {0}
    if n == 3:
        return {0, 2}
    m = n.bit_length() - 1
    h = n - (1 << m)
    t = lambda j: (1 << j) - 1
    if h < (1 << (m - 1)):
        return {t(j) for j in range(1, m - 1, 2)} | {t(m - 1), t(m) - 1}
    return {t(j) for j in range(1, m, 2)} | {t(m) - 1, t(m) + 1}


def contains_all_factors(n, chosen):
    s = word(n)
    seen = set()
    hit = set()
    for start in range(n):
        for end in range(start, n):
            f = s[start:end+1]
            seen.add(f)
            if any(start <= p <= end for p in chosen):
                hit.add(f)
    return seen == hit


def all_occurrences(s, f):
    out = []
    offset = 0
    while True:
        p = s.find(f, offset)
        if p < 0:
            return out
        out.append((p, p + len(f) - 1))
        offset = p + 1


def disjoint_witnesses(n):
    m = n.bit_length() - 1
    # For odd depth, lower witnesses apply to the dyadic prefix;
    # appended zero-only suffixes are handled by the projection lemma.
    h = n - (1 << m)
    if m % 2 == 1:
        n = 1 << m
    s = word(n)
    if m < 2:
        return
    h = n - (1 << m)
    t = lambda j: (1 << j) - 1
    witnesses = []
    if m == 2:
        if h >= 2:
            witnesses = [('11', (0, 1)), ('01', (2, 3)), ('00', (4, n - 1))]
        else:
            witnesses = [('11', (0, 1)), ('01', (2, 3))]
    elif m % 2 == 0 and h >= (1 << (m - 1)):
        witnesses = [('1'+'0'*((1 << i)-1)+'1', (t(i), t(i+1)))
                     for i in range(0, m-2, 2)]
        witnesses += [('1'+'0'*((1 << (m-2))-1)+'10', (t(m-2), t(m-1)+1)),
                      ('0'*((1 << (m-1))-2)+'1', (t(m-1)+2, t(m))),
                      ('0'*(1 << (m-1)), (t(m)+1, n-1))]
    elif m % 2 == 0:
        witnesses = [('1'+'0'*((1 << i)-1)+'1', (t(i), t(i+1)))
                     for i in range(0, m, 2)]
        witnesses += [('0'*((1 << (m-1))-2)+'1', (t(m-1)+2, t(m)))]
    else:
        witnesses = [('1'+'0'*((1 << i)-1)+'1', (t(i), t(i+1)))
                     for i in range(0, m-2, 2)]
        witnesses += [('0'*((1 << (m-2))-1)+'10', (t(m-2)+1, t(m-1)+1)),
                      ('0'*((1 << (m-1))-2)+'1', (t(m-1)+2, t(m)))]
    assert len(witnesses) == formula(n), (n, len(witnesses), formula(n))
    used = set()
    for f, (low, high) in witnesses:
        positions = all_occurrences(s, f)
        assert positions, (n, f)
        assert all(low <= a and b <= high for a,b in positions), (n, f, positions, low, high)
        assert not any(x in used for x in range(low, high+1)), (n, f)
        used.update(range(low, high+1))


def exhaustive_minimum(n):
    s = word(n)
    restrictions = set()
    for a in range(n):
        for b in range(a, n):
            f = s[a:b+1]
            locations = tuple((i, i+len(f)-1) for i in range(n-len(f)+1)
                              if s[i:i+len(f)] == f)
            restrictions.add(locations)
    for k in range(1,n+1):
        for q in combinations(range(n),k):
            if all(any(any(i <= p <= j for p in q) for i,j in occ) for occ in restrictions):
                return k
    return n


def run():
    for n in range(1, 185):
        chosen = proposed(n)
        assert len(chosen) == formula(n) and all(0 <= v < n for v in chosen), (n, chosen)
        assert contains_all_factors(n, chosen), ('upper', n, chosen)
        disjoint_witnesses(n)
    for n in (191,192,223,256,383,384,512):
        chosen = proposed(n)
        assert len(chosen) == formula(n), (n, chosen)
        assert contains_all_factors(n, chosen), ('upper', n, chosen)
        disjoint_witnesses(n)
    for n in range(1, 15):
        assert exhaustive_minimum(n) == formula(n), ('small exact', n)
    print('VERIFY_OK: factor coverage, disjoint-occurrence witnesses, and exhaustive small-prefix minima')


if __name__ == '__main__':
    run()
