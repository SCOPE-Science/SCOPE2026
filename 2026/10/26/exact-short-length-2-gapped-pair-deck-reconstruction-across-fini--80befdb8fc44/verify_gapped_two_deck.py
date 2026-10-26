#!/usr/bin/env python3
"""Exact exhaustive certificate for short 2-spaced pair-subsequence reconstruction.

Only Python 3 standard library is required. Input alphabets are {0,...,q-1}.
The observed deck includes singleton counts and ordered pairs from positions
whose index difference is at least two.
"""
from collections import Counter, defaultdict
from itertools import combinations, product


def direct(word, q):
    n = len(word)
    out = [0] * (q + q * q)
    for x in word:
        out[x] += 1
    for i in range(n):
        for j in range(i + 2, n):
            out[q + q * word[i] + word[j]] += 1
    return tuple(out)


def streaming(word, q):
    n = len(word)
    out = [0] * (q + q * q)
    available = [0] * q
    for j, y in enumerate(word):
        if j >= 2:
            available[word[j - 2]] += 1
        out[y] += 1
        for x in range(q):
            out[q + q * x + y] += available[x]
    return tuple(out)


def fibers(q, n):
    data = defaultdict(list)
    for word in product(range(q), repeat=n):
        a = direct(word, q)
        assert a == streaming(word, q), (q, n, word)
        data[a].append(word)
    return data


def collision_pairs(data):
    out = []
    for vals in data.values():
        assert 1 <= len(vals) <= 2
        if len(vals) == 2:
            a, b = vals
            out.append((a, b))
    return out


def support(pair):
    return len(set(pair[0]) | set(pair[1]))


def strings(pair):
    return tuple(''.join(map(str, w)) for w in pair)


SIX_BINARY = {
    ('001101', '010011'),
    ('011001', '100110'),
    ('101100', '110010'),
}
SEVEN_BINARY = {
    ('0001101', '0010011'),
    ('0010100', '0100010'),
    ('0011010', '0100110'),
    ('0011011', '0100111'),
    ('0101100', '0110010'),
    ('1001101', '1010011'),
    ('1011000', '1100100'),
    ('1011001', '1100101'),
    ('1011101', '1101011'),
    ('1101100', '1110010'),
}
SEVEN_TERNARY = {
    ('0011012', '0100112'), ('0022021', '0200221'),
    ('0112212', '0121122'), ('0120210', '0210120'),
    ('0212211', '0221121'), ('1002202', '1020022'),
    ('1011002', '1100102'), ('1021201', '1201021'),
    ('1122120', '1211220'), ('1202200', '1220020'),
    ('2001101', '2010011'), ('2012102', '2102012'),
    ('2022001', '2200201'), ('2101100', '2110010'),
    ('2122110', '2211210'),
}


def main():
    checked = 0
    for q in range(2, 6):
        for n in range(1, 8):
            data = fibers(q, n)
            checked += q ** n
            if n == 1:
                expected = q
                assert len(data) == expected
                assert all(len(v) == 1 for v in data.values())
            elif n == 2:
                expected = q * (q + 1) // 2
                assert len(data) == expected
                assert Counter(map(len, data.values())) == {1:q, 2:q*(q-1)//2}
            elif n <= 5:
                assert len(data) == q ** n
                assert all(len(v) == 1 for v in data.values())
            else:
                coll = collision_pairs(data)
                hist = Counter(support(p) for p in coll)
                if n == 6:
                    assert hist == {2: 3 * (q * (q - 1) // 2)}, (q,n,hist)
                else:
                    expected_hist = {2: 10 * (q * (q - 1) // 2)}
                    if q >= 3:
                        expected_hist[3] = 15 * (q * (q - 1) * (q - 2) // 6)
                    assert hist == expected_hist, (q,n,hist)
                assert len(data) == q**n - len(coll)
                if q == 2 and n == 6:
                    assert {strings(p) for p in coll} == SIX_BINARY
                    for a,b in coll: assert sum(a) == sum(b) == 3
                if q == 2 and n == 7:
                    assert {strings(p) for p in coll} == SEVEN_BINARY
                    for a,b in coll: assert min(sum(a), n-sum(a)) >= 2
                if q == 3 and n == 7:
                    assert {strings(p) for p in coll if support(p) == 3} == SEVEN_TERNARY
        print('ALPHABET_OK q=%d' % q)
    print('GAPPED_TWO_DECK_PASS q=2..5 n=1..7 words=%d binary6=3 binary7=10 ternary7=15 max_fiber=2' % checked)


if __name__ == '__main__':
    main()
