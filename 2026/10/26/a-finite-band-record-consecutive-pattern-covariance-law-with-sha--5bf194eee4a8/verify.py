"""Finite checks for record/consecutive-pattern covariance identities.

Run: python verify_record_patterns.py
Uses only the Python standard library.
"""
from itertools import permutations
from collections import defaultdict
from fractions import Fraction
from math import factorial


def f(k, b, j):
    """Conditional record probability, if b is a prefix maximum."""
    v = Fraction(factorial(k), factorial(b - 1))
    for t in range(b-1, k):
        v /= j + t
    return v


def kernel(k, pattern, j, r):
    return (Fraction(int(pattern[r] == max(pattern[:r+1])), 1)
            * f(k, pattern[r], j) - Fraction(1, j+r)) / factorial(k)


def limit(k, pat):
    mx = 0
    s = Fraction(-(k-1), factorial(k))
    for b in pat:
        if b > mx:
            mx = b
            if b < k:
                s += Fraction(k, (k-b)*factorial(k))
    return s


def run():
    count = 0
    for n in range(2, 9):
        for k in range(2, min(5,n) + 1):
            windows = n-k+1
            nd = factorial(n)
            totalR = 0
            pattern_count = defaultdict(int)
            pattern_R = defaultdict(int)
            local_R = defaultdict(int)
            local_joint = defaultdict(int)
            for perm in permutations(range(1,n+1)):
                records = tuple(int(perm[i]==max(perm[:i+1])) for i in range(n))
                nr = sum(records)
                totalR += nr
                for j0 in range(windows):
                    w = perm[j0:j0+k]
                    pat = tuple(1 + sum(x < a for x in w) for a in w)
                    pattern_count[pat] += 1
                    pattern_R[pat] += nr
                    if n<=7:
                        for i in range(n):
                            local_joint[(pat,j0,i)] += records[i]
            assert totalR == nd*sum((Fraction(1,i) for i in range(1,n+1)),Fraction(0))
            pats = list(permutations(range(1,k+1)))
            for pat in pats:
                observed = Fraction(pattern_R[pat],nd) - Fraction(totalR,nd)*Fraction(windows,factorial(k))
                expected = sum((kernel(k,pat,j0+1,r) for j0 in range(windows)
                                for r in range(k)),Fraction(0))
                assert observed == expected,(n,k,pat,observed,expected)
                count += 1
                if n<=7:
                    for j0 in range(windows):
                        assert pattern_count[pat]==nd*Fraction(windows,factorial(k))
                        for i in range(n):
                            expected = (kernel(k,pat,j0+1,i-j0) if j0<=i<j0+k else Fraction(0))
                            # Only patterns of this window, so count selected at j0 separately.
                            # Recover observed from per-window sum recorded in local_joint.
                            actual = Fraction(local_joint[(pat,j0,i)],nd) - Fraction(1,i+1)/factorial(k)
                            assert actual == expected,(n,k,pat,j0,i,actual,expected)
                            count += 1
            # The limiting formula has unique max at ascending, and min at all patterns starting with k.
            vals = {p:limit(k,p) for p in pats}
            mn, mx = min(vals.values()), max(vals.values())
            assert mn == -Fraction(k-1,factorial(k))
            assert mx == Fraction(k*sum((Fraction(1,t) for t in range(1,k)),Fraction(0))-(k-1),factorial(k))
            assert [p for p,v in vals.items() if v==mx] == [tuple(range(1,k+1))]
            assert set(p for p,v in vals.items() if v==mn)==set(p for p in pats if p[0]==k)
            count += 4
    print('VERIFY_OK',count,'exact finite covariance and extremal assertions, exhaustive permutations through n=8')


if __name__ == '__main__':
    run()
