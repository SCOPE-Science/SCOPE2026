#!/usr/bin/env python3
"""Exact finite checks for a binary repetend sharp-complexity formula.

The infinite theorem relies on the written number-theoretic argument.
"""

def predicted(k):
    Q = 3**k
    N = 2 * 3**(k-1)
    m = N.bit_length() - 1
    M = 1 << m
    deficit = max(0, (M-1)//3 - (Q-M)//3)
    longest = m if deficit == 0 else m-1
    return Q,N,m,M,deficit,longest


def digit_period(Q, N):
    remainder = 1
    bits = []
    seen = set()
    for i in range(N):
        assert remainder not in seen, (Q, i, remainder)
        seen.add(remainder)
        doubled = 2*remainder
        bits.append(doubled//Q)
        remainder = doubled%Q
    assert remainder == 1
    assert len(bits) == N
    return bits


def cyclic_words(bits, j):
    n = len(bits)
    mask = (1 << j) - 1
    window = 0
    for z in range(j):
        window = ((window << 1) | bits[z % n]) & mask
    vals = {window}
    for i in range(1,n):
        window = ((window << 1) | bits[(i+j-1)%n]) & mask
        vals.add(window)
    return vals


def main():
    checks = 0
    for k in range(1,10):
        Q,N,m,M,d,longest = predicted(k)
        bits = digit_period(Q,N)
        for j in range(1,m+2):
            B = 1 << j
            from_digits = cyclic_words(bits,j)
            from_units = {(B*r)//Q for r in range(1,Q) if r%3}
            assert from_digits == from_units, (k,j)
            checks += len(from_units)
            assert (len(from_units) == B) == (j <= longest), (k,j)
        assert M-len(cyclic_words(bits,m)) == d, (k,d)
        if k>=2:
            assert (longest==m)==(Q>=2*M)
        print(f'k={k}, period={N}, critical-length={m}, missing={d}, universal-through={longest}')
    for k in range(2,101):
        Q,N,m,M,d,longest=predicted(k)
        assert (d == 0) == (Q >= 2*M), k
    print(f'PASS: {checks} checked distinct-word memberships; 99 sharp-phase integer comparisons; independent long division and unit-bin enumeration')

if __name__ == '__main__':
    main()
