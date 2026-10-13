#!/usr/bin/env python3
"""Exact Hamming-weight enumerator checks for two integral spike-code families.
Standard library only; all arithmetic is integer arithmetic.
"""
from collections import Counter
from itertools import product
from math import comb, gcd


def predicted(k, q):
    if not (k >= 2 and q >= 2):
        raise ValueError("k,q must be integers at least two")
    T = sum(comb(k, j) * gcd(j - 1, q) for j in range(k + 1))
    E = Counter()
    B = Counter()
    for j in range(k + 1):
        numerator = comb(k, j) * ((q - 1)**j + (q - 1)*(-1)**j)
        assert numerator % q == 0
        E[2*j] += numerator // q
    D = q*T - (2*q-1)*2**k
    for t in range(k + 1):
        numerator = (q-1)*comb(k,t)*2**(k-t)*(q-2)**t + D*comb(k,t)*(-1)**t
        assert numerator % q == 0
        B[t] += numerator // q
    N = Counter(E)
    Z = Counter(E)
    for t, count in B.items():
        N[k+t] += count
        Z[k+t+1] += count
    assert all(n >= 0 for n in N.values())
    assert all(n >= 0 for n in Z.values())
    assert sum(N.values()) == q**k and sum(Z.values()) == q**k
    # Published full-support coefficient identities, tested without floating point.
    numerator = (q-1)*(q-2)**k - ((-2)**k)*(2*q-1) + q*((-1)**k)*T
    assert numerator % q == 0
    published_Z = numerator // q
    published_N = published_Z + ((q-1)**k + (q-1)*(-1)**k)//q
    assert Z[2*k+1] == published_Z and N[2*k] == published_N
    return +N, +Z


def matrix_enumeration(k, q):
    """Directly multiply all q^k messages by the original integral matrices."""
    columns = []
    for i in range(k):
        columns.append(tuple(int(row == i) for row in range(k)))
    for i in range(k):
        columns.append(tuple(int(row != i) for row in range(k)))
    extra = tuple([1]*k)
    N, Z = Counter(), Counter()
    for u in product(range(q), repeat=k):
        v = tuple(sum(a*b for a,b in zip(u,col)) % q for col in columns)
        vn = sum(x != 0 for x in v)
        N[vn] += 1
        Z[vn + (sum(a*b for a,b in zip(u,extra)) % q != 0)] += 1
    return +N, +Z


def residue_dynamic_program(k,q):
    """Independently count zero/nonzero coordinates by residue convolution."""
    N, Z = Counter(), Counter()
    for target in range(q):
        states = {(0,0): 1}
        for _ in range(k):
            new = Counter()
            for (s,w),mult in states.items():
                for x in range(q):
                    paired = (target-x) % q
                    new[((s+x)%q, w+int(x!=0)+int(paired!=0))] += mult
            states = dict(new)
        for (s,w),mult in states.items():
            if s==target:
                N[w] += mult
                Z[w+(target!=0)] += mult
    return +N, +Z


def main():
    exhaustive = dp = 0
    for q in range(2,14):
        for k in range(2,9):
            want = predicted(k,q)
            got = residue_dynamic_program(k,q)
            assert want == got, ("DP mismatch",k,q,want,got)
            dp += 1
            if q**k <= 35000:
                actual = matrix_enumeration(k,q)
                assert want == actual, ("matrix mismatch",k,q,want,actual)
                exhaustive += 1
    assert predicted(4,2)[0] == {0:1,4:14,8:1}
    assert predicted(4,5)[0][4] == 40
    assert predicted(4,6)[0][4] == 56
    assert predicted(5,5)[1][4] == 40
    print(f"VERIFY_OK residue-DP={dp} direct-matrix={exhaustive}; source-table checks N4/Z5 passed")
    for k,q in ((4,6),(5,3),(6,5)):
        print(f"N(k={k},q={q})",dict(sorted(predicted(k,q)[0].items())))

if __name__ == '__main__':
    main()
