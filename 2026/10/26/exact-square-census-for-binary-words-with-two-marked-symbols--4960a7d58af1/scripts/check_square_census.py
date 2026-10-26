"""Independent finite checks for the two-marker square-spectrum theorem.
No third-party packages. Run: python3 square_two_marker_checker.py
"""
from collections import Counter
from math import comb


def direct(w):
    """Distinct actual square strings, without using the structural formula."""
    s = set()
    for start in range(len(w)):
        for half in range(1, (len(w) - start) // 2 + 1):
            if w[start:start + half] == w[start + half:start + 2 * half]:
                s.add(w[start:start + 2 * half])
    return len(s)


def formula(a, b, c):
    return max(a, b, c) // 2 + max(0, 1 + min(a, b, c, a+c-b))


def max_count(m):
    if m % 2 == 0:
        return 2 * (m // 3 + 1) - (m % 3 == 0)
    return (2 * (m // 3 + 1) - (m % 3 == 0)
            + 4 * ((m - 2) // 3 + 1) - (m % 3 == 2))


def coefficient_aggregate(m):
    # The all-zero squares contribution counts triples whose maximum >= 2*j.
    pure = 0
    for j in range(1, m // 2 + 1):
        r = 2 * j
        # By inclusion-exclusion, number of triples with some gap >= r.
        def ways(s):
            return comb(s + 2, 2) if s >= 0 else 0
        pure += 3 * ways(m - r) - 3 * ways(m - 2*r) + ways(m - 3*r)
    # Count square roots with one 1 via (a,b,c,u,v) =
    # (u+x, u+v, v+y), with x,y,u,v nonnegative.
    mixed = sum((j + 1) * (m - 2*j + 1) for j in range(m // 2 + 1))
    return pure + mixed


def main():
    n_direct = 0
    for m in range(0, 24):
        for a in range(m + 1):
            for b in range(m - a + 1):
                c = m - a - b
                w = '0'*a+'1'+'0'*b+'1'+'0'*c
                assert direct(w) == formula(a,b,c), (a,b,c)
                n_direct += 1
    n_compositions = 0
    for m in range(0, 121):
        values = [formula(a,b,m-a-b) for a in range(m+1)
                  for b in range(m-a+1)]
        n_compositions += len(values)
        assert sum(values) == coefficient_aggregate(m), m
        assert max(values) == m//2 + 1, m
        assert sum(v == max(values) for v in values) == max_count(m), m
        assert min(values) == (1 if m == 0 else (m+2)//4), m
        assert len(values) == comb(m + 2, 2)
    # Directly confirm the two tightness constructions for a larger range.
    for m in range(1, 501):
        b = m // 2 + 1
        assert formula(m-b,b,0) == (m+2)//4
        assert formula(m,0,0) == m//2 + 1
    print('PASS: direct square-set checks:',n_direct)
    print('PASS: formula/GF/extrema/equality count compositions:',n_compositions)
    print('PASS: explicit sharpness witnesses: 500 lengths')
    print('initial aggregate coefficients:',[coefficient_aggregate(m) for m in range(11)])

if __name__ == '__main__':
    main()
