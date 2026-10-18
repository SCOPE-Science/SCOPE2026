"""Exact finite-state tests of leaf-child regression in uniform recursive trees.

Run with Python 3: python verify.py
No dependencies beyond the standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, comb


def enumerate_counts(n):
    """Return counts (root-leaf children, total leaves) over all recursive trees."""
    counts = defaultdict(int)
    if n < 2:
        raise ValueError('n >= 2')
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        outdegree = [0] * (n + 1)
        for parent in parents:
            outdegree[parent] += 1
        z = sum(1 for j, parent in enumerate(parents, 2)
                if parent == 1 and outdegree[j] == 0)
        ell = sum(1 for j in range(2, n + 1) if outdegree[j] == 0)
        counts[(z, ell)] += 1
    return counts


def rencontres_pmf(n, z):
    # n-1 objects, exactly z fixed points.
    m = n - 1
    return Fraction(1, factorial(z)) * sum(((-1) ** k) * Fraction(1, factorial(k))
                for k in range(m-z+1))


def main():
    checks = 0
    for n in range(2, 10):
        counts = enumerate_counts(n)
        total = factorial(n - 1)
        assert sum(counts.values()) == total
        checks += 1
        for z in range(n):
            count_z = sum(v for (k, ell), v in counts.items() if k == z)
            assert Fraction(count_z, total) == rencontres_pmf(n, z), (n, z)
            checks += 1
            if count_z:
                observed = Fraction(sum(ell * v for (k, ell), v in counts.items() if k == z), count_z)
                assert observed == Fraction(n - 1 + z, 2), (n, z, observed)
                checks += 1
        ell_mean = Fraction(sum(ell*v for (z,ell),v in counts.items()),total)
        assert ell_mean == Fraction(n,2)
        checks += 1
        if n >= 3:
            var_ell = Fraction(sum((ell-ell_mean)**2 * v for (z,ell),v in counts.items()),total)
            assert var_ell == Fraction(n,12), (n,var_ell)
            cov = Fraction(sum((z-1)*(ell-ell_mean)*v for (z,ell),v in counts.items()),total)
            assert cov == Fraction(1,2), (n,cov)
            checks += 2

    # Confirm polynomial recurrence and the mixed transform identity by
    # coefficientwise rational arithmetic for an additional parameter range.
    from fractions import Fraction as F
    def add(a,b):
        c = [F(0)]*max(len(a),len(b))
        for i,x in enumerate(a): c[i]+=x
        for i,x in enumerate(b): c[i]+=x
        return c
    def scale(a,f): return [f*x for x in a]
    def mult_u(a): return [F(0)]+a
    def diff(a): return [F(i)*a[i] for i in range(1,len(a))]
    def aop(a,n):
        derivative = diff(a)
        return add(add(mult_u(a),scale(a,n-1)), add(derivative,scale(mult_u(derivative),-1)))
    g=[F(0),F(1)]
    h=[F(0),F(1)]
    for n in range(2, 26):
        predicted=add(scale(g,F(n-1,2)),scale(mult_u(diff(g)),F(1,2)))
        assert h==predicted,(n,h,predicted)
        checks+=1
        if n<25:
            gnext=scale(aop(g,n),F(1,n))
            hnext=scale(add(aop(h,n-1),add(mult_u(g),scale(g,n-1))),F(1,n))
            # Pad polynomials to the same degree before equality.
            hnext=add(hnext,[])
            expected=[sum(F((-1)**(r-j),factorial(j)*factorial(r-j))
                          for r in range(j,n+1)) for j in range(n+1)]
            assert gnext==expected,(n,gnext,expected)
            g,h=gnext,hnext
            checks+=1
    print('PASS:',checks,'exact rational / exhaustive assertions for n=2..9, n<=25 transform recurrences.')

if __name__=='__main__':
    main()
