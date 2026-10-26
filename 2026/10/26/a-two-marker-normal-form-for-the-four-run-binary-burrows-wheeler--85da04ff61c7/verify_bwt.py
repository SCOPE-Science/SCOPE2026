#!/usr/bin/env python3
"""Independent suffix-order verification of a four-run binary BWT theorem.

Run with Python 3.9 or later: python verify_bwt.py
The reference construction sorts literal suffixes. The closed-form evaluator
uses only rank arithmetic and is independent of the sorting implementation.
"""
from itertools import product
from math import comb
from random import Random


def direct_bwt(a, b, c, d):
    assert min(a, b, c, d) >= 1
    text = '0' * a + '1' * b + '0' * c + '1' * d + '$'
    order = sorted(range(len(text)), key=lambda i: text[i:])
    return ''.join(text[i - 1] for i in order)


def direct_run_count(word):
    return 1 + sum(word[i] != word[i - 1] for i in range(1, len(word)))


def normal_form(a, b, c, d):
    Z, O = a + c, b + d
    u = 1 + max(c - a, 0) + int(c >= a and b >= d)
    v = 1 + max(a - c, 0) + int(a >= c and b < d)
    p = min(2 * b, O)
    q = min(2 * d - 1, O)
    assert 1 <= u <= Z and 1 <= v <= Z and u != v
    assert 1 <= p <= O and 1 <= q <= O and p != q
    X = ['0'] * Z
    X[u - 1], X[v - 1] = '$', '1'
    Y = ['1'] * O
    Y[p - 1] = Y[q - 1] = '0'
    predicted_text = '1' + ''.join(X) + ''.join(Y)
    internal_X = 3 - int(max(u, v) == Z) - int(abs(u - v) == 1)
    internal_Y = 3 - int(q == 1) - 2 * int(abs(p - q) == 1)
    end_X = '$' if u == Z else ('1' if v == Z else '0')
    start_Y = '0' if q == 1 else '1'
    predicted_runs = (1 + internal_X + internal_Y + int(v != 1)
                      + int(end_X != start_Y))
    return predicted_text, predicted_runs


def is_nine_run(a, b, c, d):
    return (a > c >= 2 and d >= b + 2) or (a >= c + 2 and b > d >= 2)


def nine_count(n):
    m = n - 9
    if m < 0:
        return 0
    return 2 * sum((j + 1) * (m - 2 * j + 1) for j in range(m // 2 + 1))


def compositions4(n):
    for a in range(1, n - 2):
        for b in range(1, n - a - 1):
            for c in range(1, n - a - b):
                yield a, b, c, n - a - b - c


def verify():
    checked = 0
    for a, b, c, d in product(range(1, 9), repeat=4):
        actual = direct_bwt(a, b, c, d)
        text, predicted = normal_form(a, b, c, d)
        assert actual == text, ((a, b, c, d), actual, text)
        runs = direct_run_count(actual)
        assert runs == predicted, ((a, b, c, d), runs, predicted)
        assert (runs == 9) == is_nine_run(a, b, c, d)
        word = '0'*a+'1'*b+'0'*c+'1'*d
        reverse = word[::-1] + '$'
        reverse_bwt = ''.join(reverse[i - 1] for i in sorted(
            range(len(reverse)), key=lambda i: reverse[i:]))
        assert direct_run_count(reverse_bwt) >= 4
        checked += 1

    rng = Random(78139)
    for _ in range(1000):
        a, b, c, d = (rng.randint(1, 150) for _ in range(4))
        text, predicted = normal_form(a, b, c, d)
        assert direct_bwt(a, b, c, d) == text
        assert direct_run_count(text) == predicted

    expected_maxima = {4: 3, 5: 5, 6: 6, 7: 7, 8: 8}
    for n in range(4, 29):
        vals = [(p, direct_run_count(direct_bwt(*p))) for p in compositions4(n)]
        assert len(vals) == comb(n - 1, 3)
        assert sum(r == 9 for _, r in vals) == nine_count(n)
        assert max(r for _, r in vals) == expected_maxima.get(n, 9)
        for (a,b,c,d), r in vals:
            assert (r == 9) == is_nine_run(a,b,c,d)
            if min(a,b,c,d) >= 2 and abs(a-c) >= 2 and abs(b-d) >= 2:
                assert r == (9 if a>c else 8)

    witness = (3, 3, 1, 2)
    w = '0'*witness[0]+'1'*witness[1]+'0'*witness[2]+'1'*witness[3]
    reverse_text = w[::-1]+'$'
    reverse_bwt = ''.join(reverse_text[i-1] for i in sorted(
        range(len(reverse_text)), key=lambda i: reverse_text[i:]))
    assert direct_bwt(*witness) == '1$01011010'
    assert reverse_bwt == '00011111$0'
    assert direct_run_count(direct_bwt(*witness)) == 9
    assert direct_run_count(reverse_bwt) == 4
    print('VERIFY_OK direct_suffix_quadruples=4096 random_large=1000 '
          'complete_length_censuses=4..28 nine_run_generating_function=true '
          'reverse_ratio_witness=9/4')

if __name__ == '__main__':
    verify()
