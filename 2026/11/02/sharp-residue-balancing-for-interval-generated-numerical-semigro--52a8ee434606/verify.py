"""Finite independent checks for residue counts of interval-generated semigroups.

Run with Python 3: python3 verify.py
Finite checks complement, but do not replace, the all-parameter proof.
"""
from math import gcd


def check(n, k):
    if not (2 <= n and 1 <= k < n):
        raise ValueError('invalid parameters')
    length = (n - 2) // k + 1
    intervals = [(t * (n + k) + 1, (t + 1) * n - 1)
                 for t in range(length)]
    upper = max(b for _, b in intervals)
    # Independent semigroup membership by forward reachable-value DP.
    reachable = bytearray(upper + 1)
    reachable[0] = 1
    for x in range(1, upper + 1):
        reachable[x] = any(x >= g and reachable[x-g] for g in range(n, n+k+1))
    direct = [x for x in range(1, upper + 1) if not reachable[x]]
    predicted = [x for a, b in intervals for x in range(a, b+1)]
    assert direct == predicted, (n, k, 'gap intervals')
    for m in range(2, k+1):
        if k % m:
            continue
        c = [0] * m
        for x in direct:
            c[x % m] += 1
        v = [0] * m
        for x in range(1, length * n):
            v[x % m] += 1
        for t in range(1, length):
            v[(t*n) % m] -= 1
        offset = (k // m) * (length*(length-1)//2)
        v = [value - offset for value in v]
        assert c == v, (n, k, m, 'exact counts')
        uniform = len(set(c)) == 1
        criterion = (gcd(n, m) == 1 and (n % m == 1 or length % m == 0))
        assert uniform == criterion, (n, k, m, 'uniformity')
        if gcd(n, m) == 1:
            assert max(c)-min(c) <= 2, (n, k, m, 'discrepancy')
        if n % m == 0:
            assert max(c)-min(c) == length, (n, k, m, 'resonance')
    return sum(1 for m in range(2,k+1) if k%m==0)


def main():
    cases = 0
    mod_cases = 0
    for n in range(3, 66):
        for k in range(1, n):
            mod_cases += check(n, k)
            cases += 1
    for n in range(66, 151):
        for k in sorted(set(k for k in (1,2,3,4,5,n//3,n//2,n-2,n-1) if k < n)):
            mod_cases += check(n, k)
            cases += 1
    for m in range(4, 30):
        n = 2*m-1
        k = m
        L = 2
        c = [0]*m
        for t in range(L):
            for x in range(t*(n+k)+1, (t+1)*n):
                c[x%m] += 1
        assert max(c)-min(c) == 2
    print('PASS: %d semigroups, %d divisor-modulus profiles, 26 sharp examples' % (cases, mod_cases))

if __name__ == '__main__':
    main()
