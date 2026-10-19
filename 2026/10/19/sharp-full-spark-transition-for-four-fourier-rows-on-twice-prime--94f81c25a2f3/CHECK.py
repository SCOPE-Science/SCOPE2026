"""Exact verification of a four-frequency cyclic Fourier full-spark classification.

Usage: python3 CHECK.py
Requires sympy; every calculation is over integer polynomial rings.
"""
from itertools import combinations, product
from functools import lru_cache
from sympy import Poly, cyclotomic_poly, symbols, expand
from sympy.matrices import Matrix

x = symbols('x')
@lru_cache(None)
def residues(n):
    phi = Poly(cyclotomic_poly(n, x), x)
    return [tuple(int(Poly(x**j, x).rem(phi).nth(k)) for k in range(phi.degree())) for j in range(n)]

def h2_is_zero(n, cols):
    v = residues(n)
    d = len(v[0])
    out = [0]*d
    for i in range(4):
        for j in range(i,4):
            term = v[(cols[i]+cols[j])%n]
            for k in range(d):
                out[k] += term[k]
    return not any(out)

def inspect(n):
    examples = []
    count = 0
    for c in combinations(range(n),4):
        count += 1
        if h2_is_zero(n,c): examples.append(c)
    return count, examples

def main():
    z = symbols('z0:4')
    A = Matrix([[zj**r for zj in z] for r in (0,1,2,5)])
    vandermonde = 1
    for i in range(4):
        for j in range(i+1,4):
            vandermonde *= (z[j]-z[i])
    h2 = sum(z[i]*z[j] for i in range(4) for j in range(i,4))
    assert expand(A.det(method='domain-ge')-vandermonde*h2)==0
    for signs in product((-1,1), repeat=4):
        val = int(h2.subs(dict(zip(z,signs))))
        assert val in (2,4,10)
    print('Exact Vandermonde times h_2 factorization and 16 signs: PASS')
    for n in (6, 10, 14, 18, 22):
        count, bad = inspect(n)
        if n == 10:
            assert len(bad)>0 and h2_is_zero(10,(0,2,4,6))
        else:
            assert bad==[], (n,bad[:5])
        print('N={}, four-column sets={}, singular={}: PASS'.format(n,count,len(bad)))
    print('All exact finite corroboration checks passed; infinite proof is cyclotomic.')

if __name__ == '__main__':
    main()
