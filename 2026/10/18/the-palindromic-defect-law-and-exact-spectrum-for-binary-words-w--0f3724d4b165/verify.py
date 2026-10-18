"""Independent finite checks for weight-three palindromic defect formulas.

Python 3 standard library only. Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def defect_by_palindrome_centres(word):
    """Discover distinct palindromes by expanding each odd/even centre."""
    seen = set()
    n = len(word)
    for twice_centre in range(2*n-1):
        left = twice_centre // 2
        right = left + (twice_centre % 2)
        while left >= 0 and right < n and word[left] == word[right]:
            seen.add(word[left:right+1])
            left -= 1
            right += 1
    return n - len(seen)


def predicted_defect(a, b, c, d):
    return 0 if b == c else max(0, min(a, d) - max(b, c))


def rational_coefficients(N):
    """Coefficient arrays of H_r via product of geometric series."""
    prod = [0] * (N + 1)
    prod[0] = 1
    for step in (1, 3, 4):
        for k in range(step, N+1):
            prod[k] += prod[k-step]
    coeff = {}
    for r in range(1, (N-6)//2 + 1):
        shift = 2*r + 6
        coeff[r] = [0 if n < shift else 2*(prod[n-shift] + (prod[n-shift-1] if n > shift else 0)) for n in range(N+1)]
    return coeff


def run():
    N = 34
    coeff = rational_coefficients(N)
    direct = [Counter() for _ in range(N+1)]
    for n in range(3,N+1):
        for i,j,k in combinations(range(n),3):
            a,b,c,d = i,j-i-1,k-j-1,n-k-1
            word = '0'*a + '1' + '0'*b + '1' + '0'*c + '1' + '0'*d
            observed = defect_by_palindrome_centres(word)
            formula = predicted_defect(a,b,c,d)
            assert observed == formula, (n,(a,b,c,d),observed,formula)
            direct[n][observed] += 1
        assert sum(direct[n].values()) == comb(n,3)
        for r in range(1,(n-6)//2 + 1):
            assert direct[n][r] == coeff[r][n], (n,r,direct[n][r],coeff[r][n])
        predicted_nonrich = sum(coeff[r][n] for r in coeff)
        assert direct[n][0] == comb(n,3) - predicted_nonrich
    for n in range(35,501):
        # Independent summation of all positive-defect classes via coefficient arrays
        # is replaced by exact counting of the forbidden zero-run configurations.
        bound=0
        for m in range(1,(n-5)//3 + 1):
            for j in range(m):
                leftover = n - (3 + m + j) - 2*(m+1)
                if leftover>=0:
                    bound += 2*(leftover+1)
        # coefficient in 2z^8/((1-z)^2(1-z^3)(1-z^4))
        other=2*sum(n-7-3*i-4*j for i in range((n-8)//3+1)
                    for j in range((n-8-3*i)//4+1))
        assert bound==other,(n,bound,other)
    print('ALL_CHECKS_PASS', 'direct_lengths=3..34', 'rational_lengths=3..500')
    print('positive_defect_counts_n8_to16', [sum(v for r,v in direct[n].items() if r>0) for n in range(8,17)])
    print('defect_spectrum_n20', sorted(direct[20].items()))


if __name__ == '__main__':
    run()
