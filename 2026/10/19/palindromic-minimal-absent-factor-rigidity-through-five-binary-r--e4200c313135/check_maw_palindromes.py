#!/usr/bin/env python3
"""Independent finite verification of the five-run palindrome MAW theorem."""
from itertools import product


def observed_maws(w):
    factors = {""}
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            factors.add(w[i:j])
    out = {x for x in "01" if x not in factors}
    for s in factors:
        for x in "01":
            for y in "01":
                t = x + s + y
                if t not in factors and t[:-1] in factors and t[1:] in factors:
                    out.add(t)
    return out


def predicted_maws(a, b, c):
    assert a >= 1 and b >= 1 and c >= 1
    m = max(a, c)
    s = {"0" * (m + 1), "1" * (b + 1)}
    s |= {"0" + "1" * i + "0" for i in range(1, b)}
    s |= {"1" + "0" * i + "1" for i in range(1, m + 1) if i != c}
    if a != c:
        j = min(a, c) + 1
        s.add("0" * j + "1" * b + "0" * j)
    if a >= c:
        s.add("1" + "0" * c + "1" * b + "0" * c + "1")
    return s


def main():
    tests = 0
    for a, b, c in product(range(1, 13), repeat=3):
        w = "0" * a + "1" * b + "0" * c + "1" * b + "0" * a
        direct = observed_maws(w)
        predicted = predicted_maws(a, b, c)
        assert direct == predicted, (a, b, c, sorted(direct ^ predicted))
        assert len(direct) == b + max(a, c) + 1 + (a > c)
        assert all(t == t[::-1] for t in direct)
        tests += 1
    small_palindromes = 0
    for a in range(1, 19):
        w = "0" * a
        assert observed_maws(w) == {"1", "0" * (a + 1)}
        small_palindromes += 1
        for b in range(1, 19):
            w = "0" * a + "1" * b + "0" * a
            expect = {"0" * (a + 1), "1" * (b + 1)}
            expect |= {"0" + "1" * i + "0" for i in range(1, b)}
            expect |= {"1" + "0" * i + "1" for i in range(1, a + 1)}
            assert observed_maws(w) == expect
            small_palindromes += 1
    nonpal_source = '0010110100'
    assert nonpal_source == nonpal_source[::-1]
    bad = {t for t in observed_maws(nonpal_source) if t != t[::-1]}
    assert bad == {'0011','1100'}
    print(f'PASS_PALINDROMIC_FIVE_RUN_MAW parameter_triples={tests} one_three_run_cases={small_palindromes} all_sets_exact=true nonuniversal_palindrome_counterexample={nonpal_source}')


if __name__ == '__main__':
    main()
