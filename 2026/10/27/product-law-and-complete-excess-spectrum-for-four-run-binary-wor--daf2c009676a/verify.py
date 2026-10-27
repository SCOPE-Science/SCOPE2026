"""Exhaustive exact checks for the closed-factor formula of four-run binary words.

Run: python3 verify.py
Standard library only. This finite check complements, but does not replace,
the unrestricted proof in RESULT.md.
"""
from itertools import product


def closed_by_all_borders(s):
    """Use every possible proper nonempty border; no structural formula."""
    if len(s) <= 1:
        return True
    for length in range(1, len(s)):
        border = s[:length]
        if s[-length:] != border:
            continue
        starts = [i for i in range(len(s) - length + 1)
                  if s[i:i+length] == border]
        if starts == [0, len(s) - length]:
            return True
    return False


def actual_factors(s):
    return {s[i:j] for i in range(len(s))
            for j in range(i+1, len(s)+1)
            if closed_by_all_borders(s[i:j])} | {""}


def classified(a, b, c, d):
    p, q = min(a, c), min(b, d)
    family = {""}
    family.update("0"*r for r in range(1, max(a, c)+1))
    family.update("1"*r for r in range(1, max(b, d)+1))
    family.update("0"*i + "1"*b + "0"*i for i in range(1, p+1))
    family.update("1"*j + "0"*c + "1"*j for j in range(1, q+1))
    family.update("0"*i + "1"*b + "0"*c + "1"*j
                  for i in range(1, p+1) for j in range(1, q+1))
    return family


def verify():
    checked = 0
    maximum = 0
    for a, b, c, d in product(range(1, 7), repeat=4):
        w = '0'*a + '1'*b + '0'*c + '1'*d
        got = actual_factors(w)
        expected = classified(a, b, c, d)
        assert got == expected, (a, b, c, d, sorted(got ^ expected))
        assert len(got) == len(w) + 1 + min(a,c)*min(b,d)
        checked += 1
        maximum = max(maximum, len(w))

    for n in range(4, 19):
        actual_spectrum = set()
        for a in range(1, n-2):
            for b in range(1, n-a-1):
                for c in range(1, n-a-b):
                    d = n-a-b-c
                    if d >= 1:
                        actual_spectrum.add(len(actual_factors('0'*a+'1'*b+'0'*c+'1'*d))-n-1)
        expected_spectrum = {p*q for p in range(1,n//2+1)
                             for q in range(1,n//2+1) if 2*(p+q) <= n}
        assert actual_spectrum == expected_spectrum, (n,actual_spectrum,expected_spectrum)
        m = n//2
        assert max(actual_spectrum) == (m*m)//4

    print('CHECK_OK families=1296 run_lengths=1..6 max_length=%d exact_sets=matched' % maximum)
    print('CHECK_OK exact_excess_spectra=lengths_4_through_18 maxima=matched')


if __name__ == '__main__':
    verify()
