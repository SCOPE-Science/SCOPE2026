"""Independent finite checks for the five-run prefix-normal enumerator.

Run with Python 3.9 or later: python verify.py
These checks corroborate, but do not replace, the symbolic all-length proof.
"""
from itertools import combinations, product
from math import comb


def prefix_normal(word):
    counts = [0]
    for ch in word:
        counts.append(counts[-1] + (ch == '1'))
    n = len(word)
    return all(
        counts[start + length] - counts[start] <= counts[length]
        for length in range(1, n + 1)
        for start in range(1, n - length + 1)
    )


def criterion(a, b, c, d, e):
    return c <= a and e <= a and (c + e <= a or d >= b)


def mul(lhs, rhs):
    ans = [0] * (len(lhs) + len(rhs) - 1)
    for i, v in enumerate(lhs):
        for j, u in enumerate(rhs):
            ans[i+j] += v*u
    return ans


def power(poly, k):
    ans = [1]
    for _ in range(k):
        ans = mul(ans, poly)
    return ans


def sequence_from_rational(top, bottom, maxn):
    coefficients = []
    for n in range(maxn+1):
        v = top[n] if n < len(top) else 0
        v -= sum(bottom[j]*coefficients[n-j] for j in range(1, min(n,len(bottom)-1)+1))
        assert bottom[0] == 1
        coefficients.append(v)
    return coefficients


def main():
    numerator = [0]*5 + [1,1,2,2,1]
    denominator = mul(mul(power([1,-1], 5),power([1,1],3)),[1,1,1])
    predicted = sequence_from_rational(numerator, denominator, 27)
    tested = 0
    for n in range(5, 28):
        positives = 0
        total = 0
        for cuts in combinations(range(1,n), 4):
            a, b, c, d, e = (cuts[0],cuts[1]-cuts[0],cuts[2]-cuts[1],cuts[3]-cuts[2],n-cuts[3])
            w = '1'*a+'0'*b+'1'*c+'0'*d+'1'*e
            actual = prefix_normal(w)
            assert actual == criterion(a,b,c,d,e),(n,a,b,c,d,e)
            positives += int(actual)
            total += 1
            tested += 1
        assert total == comb(n-1,4), (n,total)
        assert positives == predicted[n], (n,positives,predicted[n])
    assert predicted[5:12] == [1,2,7,13,27,44,75]
    print('VERIFY_OK', 'five_run_words_checked',tested,'coefficient_range','n=5..27')

if __name__ == '__main__':
    main()
