"""Independent finite-extension checks for an exact two-type formula.

Run with Python 3.9+ using the standard library: python verify.py.
The support enumeration is algorithmic; it does not store the formula's proof.
"""
from itertools import product
from math import comb

STATES = (-1, 0, 1)


def admissible(order_xy, state_a, state_b=None, relation_ab=0):
    """Check an explicitly specified 3- or 4-point *induced* strict poset.

    -1 encodes less-than, 0 incomparable, +1 greater-than.
    The first two vertices are x,y; the others are labelled parameters.
    """
    n = 3 if state_b is None else 4
    e = [[False] * n for _ in range(n)]

    def add(i, j, sign):
        if sign == -1:
            e[i][j] = True
        elif sign == 1:
            e[j][i] = True

    add(0, 1, order_xy)
    add(2, 0, state_a[0])
    add(2, 1, state_a[1])
    if state_b is not None:
        add(3, 0, state_b[0])
        add(3, 1, state_b[1])
        add(2, 3, relation_ab)
    return not any(e[i][j] and e[j][k] and not e[i][k]
                   for i in range(n) for j in range(n) for k in range(n))


def supports_matrix(order_xy):
    # S is the list of local 3-point types for a single parameter.
    S = [s for s in product(STATES, repeat=2) if admissible(order_xy, s)]
    n = len(S)
    within = [[admissible(order_xy, S[i], S[j], 0)
               for j in range(n)] for i in range(n)]
    cross = [[admissible(order_xy, S[i], S[j], -1)
              for j in range(n)] for i in range(n)]
    assert all(within[i][i] for i in range(n))
    assert all(within[i][j] == within[j][i]
               for i in range(n) for j in range(n))
    good = []
    for mask in range(1 << n):
        active = [i for i in range(n) if (mask >> i) & 1]
        if all(within[i][j] for i in active for j in active):
            good.append((active, len(active)))
    c = [[0] * 5 for _ in range(5)]
    for A, i in good:
        for B, j in good:
            if all(cross[s][t] for s in A for t in B):
                c[i][j] += 1
    return len(S), len(good), c


def shift_to_power_basis(c):
    # In the exponential generating function X = exp(s)-1, Y = exp(t)-1.
    m = len(c)
    d = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for p in range(i + 1):
                for q in range(j + 1):
                    d[p][q] += c[i][j] * comb(i, p) * comb(j, q) * (-1)**(i+j-p-q)
    return d


C_LESS = [
    [1, 6, 10, 6, 1],
    [6, 20, 24, 12, 2],
    [10, 24, 20, 7, 1],
    [6, 12, 7, 1, 0],
    [1, 2, 1, 0, 0],
]
C_INCOMP = [
    [1, 7, 14, 10, 2],
    [7, 26, 38, 24, 5],
    [14, 38, 44, 26, 6],
    [10, 24, 26, 16, 4],
    [2, 5, 6, 4, 1],
]


def formula_less(a, b):
    return (4**a*2**b + 2**a*4**b + 3**(a+b) + 3**a + 3**b
            - 2**(a+b) - 2*2**a - 2*2**b + 1)


def formula_incomp(a, b):
    return (4**(a+b) + 4**a + 4**b + 2*(3**a*2**b + 2**a*3**b)
            - 4*2**(a+b) - 2*(2**a + 2**b) + 2)


def direct_count(a, b):
    # This approach does not use support matrices or the EGF.
    n = 2 + a + b
    count = {-1: 0, 0: 0, 1: 0}
    for order_xy in STATES:
        fixed = [[False] * n for _ in range(n)]
        if order_xy == -1:
            fixed[0][1] = True
        if order_xy == 1:
            fixed[1][0] = True
        for p in range(a):
            for q in range(b):
                fixed[p+2][q+a+2] = True
        for choices in product(STATES, repeat=2*(a+b)):
            e = [row[:] for row in fixed]
            for p in range(a+b):
                z = p+2
                for v in (0, 1):
                    s = choices[2*p+v]
                    if s == -1:
                        e[z][v] = True
                    elif s == 1:
                        e[v][z] = True
            valid = not any(e[i][j] and e[j][k] and not e[i][k]
                            for i in range(n) for j in range(n) for k in range(n))
            count[order_xy] += valid
    return count


def main():
    for order, count_states, count_cliques, target in (
        (-1, 6, 24, C_LESS), (0, 7, 34, C_INCOMP), (1, 6, 24, C_LESS)
    ):
        n, cliques, c = supports_matrix(order)
        assert (n, cliques, c) == (count_states, count_cliques, target)
        transformed = shift_to_power_basis(c)
        for a in range(8):
            for b in range(8):
                val = sum(transformed[i][j] * i**a * j**b
                          for i in range(5) for j in range(5))
                target_val = formula_incomp(a, b) if order == 0 else formula_less(a, b)
                assert val == target_val, (order, a, b, val, target_val)
    print('SUPPORT_MATRICES_AND_POWER_TRANSFORM_PASS: 3 orientations, 192 polynomial tests')
    direct_tests = 0
    for a in range(5):
        for b in range(5-a):
            got = direct_count(a, b)
            assert got[-1] == got[1] == formula_less(a, b), (a, b, got)
            assert got[0] == formula_incomp(a, b), (a, b, got)
            direct_tests += 1
    print('DIRECT_TRANSITIVITY_PASS: %d labelled configurations (a+b<=4)' % direct_tests)
    for n in range(1, 10):
        total = 2*formula_less(n,n) + formula_incomp(n,n)
        assert total >= formula_incomp(n,n) > 0
    print('ASYMPTOTIC_LEADING_TERMS_PASS: comparable=2*9^n+O(8^n), total=16^n+O(9^n)')
    print('SAMPLE: (a,b)=(1,1):',2*formula_less(1,1)+formula_incomp(1,1))
    print('SAMPLE: (a,b)=(2,2):',2*formula_less(2,2)+formula_incomp(2,2))
    print('ALL_TESTS_PASS')

if __name__ == '__main__':
    main()
