#!/usr/bin/env python3
"""Direct finite checks for Cantor-word Abelian factor class multiplicities.
This is a finite corroboration, not a proof for arbitrary substitution depth.
"""
from collections import Counter
from fractions import Fraction


def cantor(k):
    w = '1'
    for _ in range(k):
        w = ''.join('101' if a == '1' else '000' for a in w)
    return w


def v2(n):
    assert n > 0
    r = 0
    while n % 2 == 0:
        r += 1
        n //= 2
    return r


def formula(k):
    assert k >= 1
    n, m = 3**k, 2**k
    d = {0: 1, m: 1}
    for j in range(1, m):
        d[j] = 2 * (3 ** v2(j) + 1) - (j == m // 2)
    return d


def main():
    for k in range(1, 8):
        b = cantor(k)
        n = 3**k
        w = cantor(k + 2)
        # Literal overlapping windows of a substitution prefix; not a two-family shortcut.
        factors = {w[i:i+n] for i in range(len(w) - n + 1)}
        observed = dict(Counter(x.count('1') for x in factors))
        expected = formula(k)
        assert observed == expected, (k, observed, expected)
        assert len(factors) == 2*n - 1
        assert sum(expected.values()) == 2*n - 1

        # A separate construction of all possible macro-block joins.
        p = [b[-t:]+'0'*(n-t) for t in range(1, n+1)]
        s = ['0'*(n-t)+b[:t] for t in range(1, n+1)]
        assert factors == set(p+s+['0'*n])
        assert len(set(p)) == len(set(s)) == n
        intersects = [(t, u) for t in range(1,n+1)
                      for u in range(1,n+1) if p[t-1]==s[u-1]]
        assert intersects == [(2*n//3,2*n//3),(n,n)], (k,intersects)

        # Exact gaps between consecutive ones of B.
        one_positions = [i for i,c in enumerate(b) if c == '1']
        assert len(one_positions)==2**k
        for j, (a, c) in enumerate(zip(one_positions,one_positions[1:]), 1):
            assert c-a == 3**v2(j)+1

        total = 2*n - 1
        mean = sum(Fraction(j,2**k)*count for j,count in observed.items())/total
        variance = sum((Fraction(j,2**k)-mean)**2 *count for j,count in observed.items())/total
        assert mean == Fraction(1,2)
        print(f'k={k}, length={n}, factors={total}, abelian_classes={len(observed)}, '
              f'midpoint_class={observed[2**(k-1)]}, '
              f'normalized_variance={float(variance):.8f}')

    # Limiting masses and moment arithmetic are symbolic finite-ratio checks.
    # At level r the total mass is 2^(r-1)/3^r, and these sum to one.
    for r in range(1, 11):
        assert Fraction(2**(r-1),3**r) == Fraction(1,3)*Fraction(2,3)**(r-1)
    assert Fraction(1,12)*(1-Fraction(1,3)/(1-Fraction(1,6))) == Fraction(1,20)
    print('PASS: finite checks and limiting-moment identity')


if __name__ == '__main__':
    main()
