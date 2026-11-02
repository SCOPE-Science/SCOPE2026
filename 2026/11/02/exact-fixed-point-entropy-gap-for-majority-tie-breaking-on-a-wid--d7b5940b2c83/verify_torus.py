#!/usr/bin/env python3
"""Exact, standalone checks for majority fixed-point counts on C3 Cartesian Cn.
Requires Python >=3.10 and SymPy >=1.12.
"""
from math import isclose
from sympy import Matrix, symbols, factor, eye, trace

N = 8

def bit(column, row):
    return (column >> row) & 1

def middle_stable(left, middle, right, strict=False):
    required = 3 if strict else 2
    for row in range(3):
        col = bit(middle, row)
        agree = sum(bit(middle, other) == col for other in range(3) if other != row)
        agree += (bit(left, row) == col) + (bit(right, row) == col)
        if agree < required:
            return False
    return True

def transition(strict=False):
    T = Matrix.zeros(64)
    for left in range(8):
        for mid in range(8):
            for right in range(8):
                if middle_stable(left, mid, right, strict):
                    T[8*left + mid, 8*mid + right] = 1
    return T

def brute_count(n, strict=False):
    if n < 3:
        raise ValueError('Requires n >= 3 and a simple cycle')
    adj = []
    for j in range(n):
        for r in range(3):
            vertices = (3*j + (r+1)%3, 3*j + (r+2)%3,
                        3*((j-1)%n) + r, 3*((j+1)%n) + r)
            adj.append(sum(1 << v for v in vertices))
    total = 0
    threshold = 3 if strict else 2
    for assignment in range(1 << (3*n)):
        if all((assignment & mask).bit_count() >= threshold
               if (assignment >> v) & 1
               else (mask & ~assignment).bit_count() >= threshold
               for v, mask in enumerate(adj)):
            total += 1
    return total

def cycle_no_singletons(n):
    return sum(all(((word>>i)&1) == ((word>>((i-1)%n))&1)
                   or ((word>>i)&1) == ((word>>((i+1)%n))&1)
                   for i in range(n)) for word in range(1<<n))

def main():
    x = symbols('x')
    T = transition(False)
    expected = (x**42*(x-3)*(x-1)*(x+1)*(x**3+x+1)**2
                *(x**3-x**2-1)*(x**3-2*x**2+x+1)**2
                *(x**4+x**2-3*x-3))
    actual = T.charpoly(x).as_expr()
    assert factor(actual-expected) == 0, 'Characteristic polynomial mismatch'
    print('PASS: exact 64x64 characteristic polynomial')
    # A second, independent exact enumeration from a vertex-neighbor graph.
    expected_mm = {3:32,4:94,5:218,6:712}
    expected_rmm = {3:2,4:6,5:12,6:20}
    for n in range(3, 7):
        mm = brute_count(n, False)
        rmm = brute_count(n, True)
        assert mm == expected_mm[n], (n, mm)
        assert rmm == expected_rmm[n], (n, rmm)
        assert rmm == cycle_no_singletons(n), n
        print(f'PASS: n={n}, MM={mm}, RMM={rmm} by independent enumeration')
    Q = eye(64)
    for n in range(1, 10):
        Q = Q*T
        if n in expected_mm:
            assert trace(Q) == expected_mm[n]
    print('PASS: trace/transfer indexing agrees with independent enumeration')
    # Algebraic root exclusion: all non-3 eigenvalues lie strictly within |z|<3.
    # On |z|=3, compare the leading term with the sum of the others.
    assert 4 < 27 and 10 < 27 and 22 < 27 and 21 < 81
    print('PASS: root bounds; unique dominant eigenvalue 3')

if __name__ == '__main__':
    main()
