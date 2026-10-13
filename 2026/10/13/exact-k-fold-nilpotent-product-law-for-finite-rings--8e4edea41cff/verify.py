"""Exact independent small-ring checks of a nilpotent-product probability law.

All tests count full matrix-product distributions, not sampled tuples.
Only Python standard library is required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def distributions(elements, identity, multiply, kmax):
    counts = {identity: 1}
    for k in range(1, kmax + 1):
        nxt = Counter()
        for a, weight in counts.items():
            for b in elements:
                nxt[multiply(a, b)] += weight
        counts = nxt
        yield k, counts


def matrices(n, q):
    return tuple(product(range(q), repeat=n * n))


def matrix_mult(n, q):
    return lambda a, b: tuple(
        sum(a[n*i+t]*b[n*t+j] for t in range(n)) % q
        for i in range(n) for j in range(n))


def is_nilpotent(a, n, q, multiply):
    p = tuple(int(i == j) for i in range(n) for j in range(n))
    zero = (0,) * (n * n)
    for _ in range(n):
        p = multiply(p, a)
    return p == zero


def main():
    checks = 0
    for n, q, kmax in ((2, 2, 4), (2, 3, 3), (3, 2, 3)):
        elems = matrices(n, q)
        unit = tuple(int(i == j) for i in range(n) for j in range(n))
        mul = matrix_mult(n, q)
        nilset = {a for a in elems if is_nilpotent(a, n, q, mul)}
        assert len(nilset) == q ** (n*n-n), (n, q, len(nilset))
        for k, dist in distributions(elems, unit, mul, kmax):
            numerator = sum(v for a, v in dist.items() if a in nilset)
            lhs = Fraction(numerator, len(elems)**k)
            rhs = 1 - Fraction(q**n-1, q**n)**k
            assert lhs == rhs, (n, q, k, lhs, rhs)
            print(f'MATRIX n={n} q={q} k={k}: {lhs} = {rhs}')
            checks += 1

    # The upper-triangular 2-by-2 ring over F_2 has Jacobson
    # radical consisting of strictly upper-triangular matrices,
    # and semisimple quotient F_2 x F_2.
    tri = tuple(product(range(2), repeat=3))
    def trimul(x, y):
        a,b,c=x; d,e,f=y
        return (a*d % 2, (a*e+b*f) % 2, c*f % 2)
    for k, dist in distributions(tri, (1,0,1), trimul, 4):
        lhs = Fraction(sum(v for (a,b,c), v in dist.items() if a==c==0), len(tri)**k)
        rhs = (1 - Fraction(1,2)**k)**2
        # More simply, (1-(1-1/2)^k)^2.
        assert lhs == rhs, (k, lhs, rhs)
        print(f'TRIANGULAR_F2 k={k}: {lhs} = {rhs}')
        checks += 1

    ring4 = tuple(range(4))
    for k, dist in distributions(ring4, 1, lambda a,b:a*b % 4, 4):
        lhs = Fraction(sum(weight for a,weight in dist.items() if a%2==0), 4**k)
        rhs = 1-Fraction(1,2)**k
        assert lhs==rhs
        print(f'Z_MOD_4 k={k}: {lhs} = {rhs}')
        checks += 1

    # Direct product F_2 x M_2(F_2) has two semisimple components.
    mm = matrices(2,2)
    mmul = matrix_mult(2,2)
    prod = tuple((z,a) for z in range(2) for a in mm)
    product_unit = (1,(1,0,0,1))
    def product_mul(v,w): return (v[0]*w[0]%2,mmul(v[1],w[1]))
    nilset = {a for a in mm if is_nilpotent(a,2,2,mmul)}
    for k,dist in distributions(prod,product_unit,product_mul,3):
        lhs=Fraction(sum(weight for (z,a),weight in dist.items() if z==0 and a in nilset),len(prod)**k)
        rhs=(1-Fraction(1,2)**k)*(1-Fraction(3,4)**k)
        assert lhs==rhs
        print(f'F2_X_M2_F2 k={k}: {lhs} = {rhs}')
        checks+=1
    print(f'EXACT_CHECKS={checks} VERIFY_OK')

if __name__ == '__main__':
    main()
