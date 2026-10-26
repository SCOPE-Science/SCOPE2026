"""Independent finite checks for the alternating-word scattered-palindrome spectrum.

All steps use Python's standard library. Finite checks illustrate, rather than
replace, the separate all-length combinatorial proof.
"""
from itertools import product
from math import comb


def predicted(n, k):
    """Closed binomial formula for distinct length-k scattered palindromes."""
    if k <= 0 or k > n:
        return 0
    if k % 2:
        h = (k - 1) // 2
        return sum(comb(h, j) for b in (0, 1) for j in range(h + 1)
                   if k + 2*j + b <= n)
    h = k // 2
    return sum(comb(h - 1, j) for b in (0, 1) for j in range(h)
               if k + 1 + 2*j + b <= n)


def contains_subsequence(word, sub):
    j = 0
    for ch in word:
        if ch == sub[j]:
            j += 1
            if j == len(sub):
                return True
    return False


def brute_palindromes(n, k):
    w = tuple(j % 2 for j in range(n))
    result = 0
    for half in product((0, 1), repeat=(k+1)//2):
        p = half + (half[-2::-1] if k % 2 else half[::-1])
        if contains_subsequence(w, p):
            result += 1
    return result


def direct_palindrome_dp(n):
    """Standard distinct-palindromic-subsequence interval recurrence."""
    w = [j % 2 for j in range(n)]
    if n == 0:
        return 0
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if w[i] != w[j]:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            else:
                inside = dp[i+1][j-1] if length >= 3 else 0
                lo = i+1
                hi = j-1
                while lo <= hi and w[lo] != w[i]:
                    lo += 1
                while hi >= lo and w[hi] != w[j]:
                    hi -= 1
                if lo > hi:
                    dp[i][j] = 2*inside + 2
                elif lo == hi:
                    dp[i][j] = 2*inside + 1
                else:
                    overlap = dp[lo+1][hi-1] if lo+1 <= hi-1 else 0
                    dp[i][j] = 2*inside - overlap
    return dp[0][n-1]


def recurrence_coefficients(N):
    # H = (1+x)(xy+x^3 y^2)/(1-x^2 y^2-x^4 y^2).
    # C[e,k] counts palindromes first present at prefix length e and length k.
    c = [[0]*(N+1) for _ in range(N+1)]
    for e in range(1, N+1):
        for k in range(1, e+1):
            v = int((e,k) in {(1,1),(2,1),(3,2),(4,2)})
            if e >= 2 and k >= 2:
                v += c[e-2][k-2]
            if e >= 4 and k >= 2:
                v += c[e-4][k-2]
            c[e][k] = v
    return c


def run():
    N = 150
    c = recurrence_coefficients(N)
    cumulative = [0]*(N+1)
    for n in range(N+1):
        if n:
            cumulative[n] = cumulative[n-1] + sum(c[n])
        assert cumulative[n] == sum(predicted(n,k) for k in range(1,n+1)), n
        if n <= 21:
            for k in range(1,n+1):
                assert brute_palindromes(n,k) == predicted(n,k), (n,k)
        assert cumulative[n] == direct_palindrome_dp(n), (n,cumulative[n])
    for n, expected in enumerate((0,1,2,4,6,9,12,17,22,30,38)):
        assert cumulative[n] == expected, n
    print('ALTERNATING_SCATTERED_PALINDROME_PASS brute_n=1..21 exact_spectrum_n=0..150 independent_interval_dp_n=0..150 rational_2d_coefficients_n=0..150')


if __name__ == '__main__':
    run()
