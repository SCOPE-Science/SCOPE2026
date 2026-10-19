"""Independent exhaustive test of a weight-three ternary ghost-pulse classification.

Run: python verify.py
"""
from itertools import combinations, product
from math import comb


def direct_feasible(n, support):
    """Enumerate all signings, and all ordered triples, including repetitions."""
    S = set(support)
    for signs in product((-1, 1), repeat=3):
        x = dict(zip(support, signs))
        if all(not (0 <= i + j - k < n and i + j - k not in S)
               for i in support for j in support for k in support
               if x[i] == x[j] == x[k]):
            return True
    return False


def geometric_feasible(n, a, b, c):
    outer = c > 2*a and 2*c - a >= n
    left = b > 2*a and (c == 2*b - a or 2*b - a >= n)
    right = 2*c - b >= n and (a == 2*b - c or c > 2*b)
    return outer or left or right


def formula(n):
    # P(n): supports with feasible outermost equal-sign pair.
    p = 0
    for a in range((n - 2)//2 + 1):
        lo = max(2*a + 1, (n + a + 1)//2)
        if lo < n:
            p += (n-lo)*(n+lo-2*a-3)//2
    # E(n): each of two disjoint arithmetic-progression exception types.
    e = sum(min(d, n-4*d) for d in range(1, (n-1)//4+1))
    u, v = n//5, (n-1)//4
    assert 2*e == 5*u*(u+1)-4*v*(v+1)+2*n*(v-u)
    return p + 2*e, p, e


def quasi_polynomial_p(n):
    return [
        n*n*(11*n-18),
        (n-1)*(11*n*n-7*n-22),
        (n-2)*(11*n*n+4*n+20),
        11*n**3-18*n*n-27*n+54,
        11*n**3-18*n*n+12*n-32,
        (n-2)*(n+1)*(11*n-7),
    ][n % 6] // 108


def main():
    for n in range(3, 42):
        count = 0
        for a,b,c in combinations(range(n),3):
            d = direct_feasible(n, (a,b,c))
            g = geometric_feasible(n, a,b,c)
            assert d == g, (n, (a,b,c), d, g)
            count += d
        exact, p, e = formula(n)
        assert count == exact, (n, count, exact)
        assert p == quasi_polynomial_p(n)
        if n <= 14 or n in (20,30,40,41):
            print(n, count, comb(n,3), p, e)
    for n in range(42, 1001):
        exact, p, e = formula(n)
        assert p == quasi_polynomial_p(n)
        assert 0 <= exact <= comb(n,3)
    print("ALL_CHECKS_PASS")

if __name__ == '__main__':
    main()
