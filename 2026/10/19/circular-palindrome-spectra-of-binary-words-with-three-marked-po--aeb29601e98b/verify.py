#!/usr/bin/env python3
"""Standalone independent enumeration for circular binary words with three ones.

Usage: python3 verify.py
No third-party packages required.
"""

def direct_count(a, b, c):
    word = '1' + '0'*a + '1' + '0'*b + '1' + '0'*c
    n = len(word)
    doubled = word + word
    factors = set()
    for start in range(n):
        for length in range(1, n+1):
            f = doubled[start:start+length]
            if f == f[::-1]:
                factors.add(f)
    return len(factors)


def closed_count(a, b, c):
    g = sorted((a, b, c))
    n = a+b+c+3
    if g[0] < g[1] < g[2]:
        return 2*n-2-g[2]
    if g[0] == g[2]:
        return n+g[0]//2
    return n+1+(n-3)//2


def predicted_maximizer_triples(n):
    assert n >= 14
    m, r = divmod(n, 3)
    if r == 0:
        return {(m-2, m-1, m)}
    if r == 1:
        return {(m-3, m, m+1), (m-2, m-1, m+1)}
    return {(m-2, m, m+1)}


def main():
    direct_cases = 0
    for n in range(3, 26):
        for a in range(n-2):
            for b in range(n-2-a):
                c = n-3-a-b
                got = direct_count(a, b, c)
                expected = closed_count(a, b, c)
                assert got == expected, (n, a, b, c, got, expected)
                direct_cases += 1

    extremal_cases = 0
    for n in range(14, 241):
        maximum = -1
        winners = set()
        for a in range(n-2):
            for b in range(n-2-a):
                c = n-3-a-b
                val = closed_count(a, b, c)
                triple = tuple(sorted((a, b, c)))
                if val > maximum:
                    maximum = val
                    winners = {triple}
                elif val == maximum:
                    winners.add(triple)
                extremal_cases += 1
        assert maximum == 2*n-2-((n+2)//3), (n, maximum)
        assert winners == predicted_maximizer_triples(n), (n, winners)

    # Contrast the three class formulas at all possible lengths tested.
    for n in range(3, 241):
        s = n-3
        repeats = n+1+s//2
        if s%3 == 0:
            equal = n+(s//3)//2
            assert equal <= repeats

    print(f'VERIFY_OK direct_gap_triples={direct_cases} extremal_gap_triples={extremal_cases} lengths=3..240')


if __name__ == '__main__':
    main()
