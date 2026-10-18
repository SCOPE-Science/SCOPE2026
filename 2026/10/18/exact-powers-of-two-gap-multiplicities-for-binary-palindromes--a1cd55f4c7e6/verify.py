"""Finite independent checks of the binary-palindrome gap classification.

Use: python3 verify.py
This enumerates all binary palindromes through length 2*k+2, which
contains every possible pair for the tested k by the theorem's proof.
"""
from math import isqrt


def palindrome(x):
    s = format(x, "b")
    return s == s[::-1]


def palindromes_of_length(L):
    half = (L + 1) // 2
    for left in range(1 << (half - 1), 1 << half):
        s = format(left, "0%db" % half)
        yield int(s + (s[::-1] if L % 2 == 0 else s[-2::-1]), 2)


def explicit_pairs(k):
    out = set()
    for a in range(1, k + 1):
        if k % a == 0:
            n = sum(1 << (j * a) for j in range(k // a))
            m = n + (1 << k)
            out.add((n, m))
    out.add(((1 << k) + 1, (1 << (k + 1)) + 1))
    for free in range(1 << (k - 1)):
        n = (1 << (2 * k)) | 1
        for j in range(1, k):
            if free & (1 << (j - 1)):
                n |= (1 << j) | (1 << (2 * k - j))
        out.add((n, n + (1 << k)))
    return out


def check():
    allpals = []
    checked = 0
    for k in range(2, 15):
        for L in (2 * k + 1, 2 * k + 2):
            # Add new palindrome lengths since preceding k.
            previous_max = 2 * (k - 1) + 2 if k > 2 else 0
            for ell in range(max(previous_max + 1, 1), L + 1):
                allpals.extend(palindromes_of_length(ell))
            break
        # Generate the remaining length 2*k+2 separately.
        allpals.extend(palindromes_of_length(2 * k + 2))
        palset = set(allpals)
        found = {(n, n + (1 << k)) for n in allpals if n + (1 << k) in palset}
        described = explicit_pairs(k)
        tau = sum(k % a == 0 for a in range(1, k + 1))
        expect = (1 << (k - 1)) + tau + 1
        assert found == described, (k, sorted(found ^ described)[:10])
        assert len(found) == expect, (k, len(found), expect)
        assert all(palindrome(n) and palindrome(m) and m - n == (1 << k)
                   for n, m in described)
        checked += len(found)
        print("k=%d: %d pairs, divisor branches=%d, centre branches=%d, boundary=1; PASS"
              % (k, len(found), tau, 1 << (k - 1)))
    print("PASS: k=2..14, %d classified pairs; all shorter palindromes exhaustively checked."
          % checked)


if __name__ == "__main__":
    check()
