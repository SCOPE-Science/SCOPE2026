#!/usr/bin/env python3
"""Exhaustive small-field checks for commuting upper-triangular idempotents.

Run with Python 3, standard library only. Matrix entries use prime fields
and the polynomial basis for GF(4)=GF(2)[z]/(z*z+z+1).
"""
from collections import Counter
from itertools import product
from math import factorial


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    p = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                p ^= 1 << (i+j)
    if p & 8:
        p ^= 0b1001  # z^3 = 1 in GF(4)
    if p & 4:
        p ^= 0b111  # z^2 = z+1
    return p


def matmul(a, b, n, q):
    out = [0] * (n*n)
    for i in range(n):
        for j in range(i, n):
            v = 0
            for t in range(i, j+1):
                v = add(v, mul(a[i*n+t], b[t*n+j], q), q)
            out[i*n+j] = v
    return tuple(out)


def triangular_matrices(n, q):
    ij = [(i, j) for i in range(n) for j in range(i, n)]
    for vals in product(range(q), repeat=len(ij)):
        mat = [0] * (n*n)
        for (i,j), a in zip(ij, vals):
            mat[i*n+j] = a
        yield tuple(mat)


def calc_predicted(n, k, q):
    m = 1 << k
    counts = Counter()
    for chars in product(range(m), repeat=n):
        changes = sum(chars[i] != chars[j] for i in range(n) for j in range(i+1,n))
        counts[tuple(chars)] = q ** changes
    return counts


def check_configuration(n, q, k):
    ide = [a for a in triangular_matrices(n,q) if matmul(a,a,n,q) == a]
    predicted = calc_predicted(n,k,q)
    observed = Counter()
    selected = 0
    pairs_tested = 0
    for items in product(ide, repeat=k):
        pairs_tested += 1
        if any(matmul(items[i],items[j],n,q) != matmul(items[j],items[i],n,q)
               for i in range(k) for j in range(i+1,k)):
            continue
        chars = tuple(sum(items[h][i*n+i] << h for h in range(k)) for i in range(n))
        observed[chars] += 1
        selected += 1
    assert observed == predicted, (n,q,k,selected,sum(predicted.values()),observed-predicted,predicted-observed)
    # Joint spectrum equals the set of diagonal characters for these families.
    profile = Counter()
    for word,v in observed.items():
        profile[len(set(word))] += v
    assert sum(profile.values()) == selected
    return len(ide), pairs_tested, selected, dict(sorted(profile.items()))


def multinomial_sum(n, m, q):
    fact = [factorial(i) for i in range(n+1)]
    ans = Counter()
    def rec(left, remaining, vec):
        if remaining == 1:
            b = vec + (left,)
            exponent = (n*n - sum(x*x for x in b))//2
            denominator = 1
            for x in b:
                denominator *= fact[x]
            ans[sum(x>0 for x in b)] += fact[n]//denominator * q**exponent
            return
        for x in range(left+1):
            rec(left-x, remaining-1, vec+(x,))
    rec(n,m,())
    return ans


def main():
    configs = [(2,2,1),(3,2,1),(4,2,1),(3,3,1),(3,4,1),
               (2,2,2),(3,2,2),(4,2,2),(3,3,2),(3,4,2),
               (2,2,3),(3,2,3)]
    n_cases = 0
    n_checked = 0
    for n,q,k in configs:
        n_idem, tested, selected, profile = check_configuration(n,q,k)
        formula = multinomial_sum(n,1<<k,q)
        assert profile == dict(sorted(formula.items())), (n,q,k,profile,formula)
        n_cases += 1
        n_checked += tested
        print('CASE', n, q, k, 'idempotents', n_idem, 'tested', tested,
              'commuting', selected, 'profile', profile)
    print('ALL_COMMUTING_IDEMPOTENT_CHECKS_PASSED', n_cases, n_checked)


if __name__ == '__main__':
    main()
