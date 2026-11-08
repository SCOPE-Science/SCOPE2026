#!/usr/bin/env python3
"""Independently checks finite instances of a Fibonacci-shift comparison theorem."""

def fibonacci_numbers(high):
    F = [0, 1]
    for _ in range(2, high + 1):
        F.append(F[-1] + F[-2])
    return F


def word_by_morphism(min_length):
    w = '0'
    while len(w) < min_length:
        w = ''.join('01' if c == '0' else '0' for c in w)
    return w


def zeckendorf(n, F):
    if n == 0:
        return '0'
    top = max(i for i in range(2, len(F)) if F[i] <= n)
    digits = []
    for i in range(top, 1, -1):
        if F[i] <= n:
            digits.append('1')
            n -= F[i]
        else:
            digits.append('0')
    assert n == 0
    s = ''.join(digits)
    assert s[0] == '1' and '11' not in s
    return s


def check():
    K = 20
    F = fibonacci_numbers(K+3)
    w = word_by_morphism(F[K+2] + 50)
    comparisons = 0
    for k in range(4, K+1):
        c = F[k]
        N = F[k+1] - 2
        u = w[:F[k+1]]
        v = w[c:c+F[k+1]]
        assert u[:N] == v[:N], (k, 'prefix')
        assert u[N] != v[N], (k, 'first mismatch')
        comparisons += N+1
        assert len(zeckendorf(N,F)) == k-1
        assert c <= N < F[k+1]
    # Cross-check two independent descriptions of the unshifted sequence.
    for i in range(25000):
        assert int(w[i]) == int(zeckendorf(i,F)[-1])
    for k in range(3,K+1):
        # Independent finite-word recurrence and near-commutation.
        a,b = '0','01'  # W_2 and W_3
        for j in range(4,k+1):
            a,b = b,b+a
        if k == 3:
            wk,wprev = '01','0'
        else:
            wk,wprev = b,a
        x,y = wk+wprev,wprev+wk
        assert x[:-2] == y[:-2] and x[-2:] != y[-2:]
        assert len(wk) == F[k]
    print(f'VERIFY_OK k=4..{K}; {comparisons} shift comparisons; 25000 independent digit checks; almost-commutation checks')

if __name__ == '__main__':
    check()
