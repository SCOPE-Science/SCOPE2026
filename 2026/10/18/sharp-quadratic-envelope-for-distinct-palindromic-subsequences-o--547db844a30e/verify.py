"""Independent palindrome-subsequence count checks for sparse binary words.

Usage: python verify_pal_sparse.py
"""
from itertools import combinations
from random import Random


def count_by_gaps(a, b, c, d):
    z = a + b + c + d
    locations = (a, a + b, a + b + c)
    one = 1 + max(min(t, z-t) for t in locations)
    if a <= d:
        two = (a + 1) * (b + c + 1) + min(b, d-a) * (c + 1)
    else:
        two = (d + 1) * (b + c + 1) + min(c, a-d) * (b + 1)
    three = (min(a, d) + 1) * (min(b, c) + 1)
    return z + one + two + three


def count_dp(w):
    """Independent all-string dynamic program using distinct-palindrome union rules."""
    n = len(w)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    def v(i,j):
        return 0 if i > j else dp[i][j]
    for i in range(n):
        dp[i][i] = 1
    for span in range(2, n + 1):
        for i in range(n-span+1):
            j = i+span-1
            if w[i] != w[j]:
                dp[i][j] = v(i+1,j) + v(i,j-1) - v(i+1,j-1)
            else:
                left = i+1
                while left < j and w[left] != w[i]:
                    left += 1
                right = j-1
                while right > i and w[right] != w[i]:
                    right -= 1
                inside = v(i+1,j-1)
                if left > right:
                    dp[i][j] = 2*inside + 2
                elif left == right:
                    dp[i][j] = 2*inside + 1
                else:
                    dp[i][j] = 2*inside - v(left+1,right-1)
    return dp[0][n-1]


def count_bruteforce(w):
    s = {''}
    for ch in w:
        s |= {u+ch for u in s}
    return sum(bool(t) and t == t[::-1] for t in s)


def word(a,b,c,d):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d


def main():
    exhaustive = 0
    small_bruteforce = 0
    for z in range(0, 18):
        for a in range(z+1):
            for b in range(z-a+1):
                for c in range(z-a-b+1):
                    d=z-a-b-c
                    w=word(a,b,c,d)
                    predicted=count_by_gaps(a,b,c,d)
                    actual=count_dp(w)
                    assert predicted == actual, (a,b,c,d,predicted,actual)
                    exhaustive += 1
                    if z <= 8:
                        brute=count_bruteforce(w)
                        assert brute == actual, (a,b,c,d,brute,actual)
                        small_bruteforce += 1
    rng=Random(1729)
    for _ in range(300):
        a,b,c,d = (rng.randrange(0, 90) for j in range(4))
        assert count_by_gaps(a,b,c,d) == count_dp(word(a,b,c,d))
    max_count=0
    for z in range(0, 75):
        top = -1
        best = []
        for a in range(z+1):
            for b in range(z-a+1):
                for c in range(z-a-b+1):
                    d=z-a-b-c
                    count = count_by_gaps(a,b,c,d)
                    if count > top:
                        top, best = count,[(a,b,c,d)]
                    elif count == top:
                        best.append((a,b,c,d))
        # Sanity check the analytically asserted sharp quadratic coefficient.
        assert 3*z*z/16 <= top <= 3*z*z/16 + 5*z + 3
        max_count += 1
    print(f'VERIFY_OK exhaustive_gap_tuples={exhaustive} raw_subsequence_cases={small_bruteforce} random_cases=300 envelope_scans={max_count}')

if __name__ == '__main__':
    main()
