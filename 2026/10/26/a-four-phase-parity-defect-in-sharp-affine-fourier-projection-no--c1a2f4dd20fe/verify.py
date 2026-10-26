"""Exact checks for affine Fourier projection on a binary parity-check code.
Run with Python 3. No external packages are required.
Finite checks supplement, but do not replace, the all-dimensional proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def central(m):
    return Fraction(comb(2*m, m), 4**m)


def formula_code(n):
    assert n >= 3
    m = n // 2
    b = central(m)
    if n % 2:
        return b * (2*m+1+(-1)**m)
    return b * (2*m+1+Fraction((-1)**(m+1),2*m-1))


def formula_cube(n):
    m = n//2
    return (2*m+1)*central(m)


def sum_code(n):
    total=sum(comb(n,j)*abs(n+1-2*j) for j in range(0,n+1,2))
    return Fraction(total,2**(n-1))


def sum_cube(n):
    return Fraction(sum(comb(n,j)*abs(n+1-2*j) for j in range(n+1)),2**n)


def parity_vertices(n):
    for vals in product((-1,1),repeat=n-1):
        z=1
        for v in vals:
            z*=v
        yield vals+(z,)


def checked():
    checks=0
    for n in range(3,201):
        a=sum_code(n)
        b=formula_code(n)
        c=formula_cube(n)
        assert a==b
        checks+=1
        assert sum_cube(n)==c
        checks+=1
        if n%2:
            assert a/c==1+Fraction((-1)**((n-1)//2),n)
        else:
            assert a/c==1+Fraction((-1)**(n//2+1),n*n-1)
        checks+=1
        if n<200:
            if n%2==0:
                m=n//2
                assert formula_code(n+1)-formula_code(n)==(-1)**m*Fraction(2*m,2*m-1)*central(m)
            else:
                m=(n-1)//2
                assert formula_code(n+1)-formula_code(n)==Fraction(2*m+1,2*m+2)*central(m)*(1-(-1)**m)
            checks+=1
    direct_rows=0
    pair_products=0
    for n in range(3,11):
        xs=list(parity_vertices(n))
        N=len(xs)
        assert N==2**(n-1)
        # Independent direct Gram matrix check for 1 and n coordinate characters.
        us=[(1,)+x for x in xs]
        for i in range(n+1):
            for j in range(n+1):
                assert sum(u[i]*u[j] for u in us)==(N if i==j else 0)
                pair_products+=1
        # Matrix rows, their positive/negative contributions, and attained sign data.
        for x in xs:
            ks=[sum(u*v for u,v in zip((1,)+x,(1,)+y)) for y in xs]
            norm=Fraction(sum(abs(k) for k in ks),N)
            assert norm==formula_code(n)
            signs=[1 if k>=0 else -1 for k in ks]
            attained=Fraction(sum(k*f for k,f in zip(ks,signs)),N)
            assert attained==norm
            assert sum(ks)==N   # constants are projected identically.
            direct_rows+=1
    print('VERIFY_OK finite_n=3..200 exact_binomial_checks='+str(checks)+
          ' direct_dimensions=3..10 direct_rows='+str(direct_rows)+
          ' Gram_entries='+str(pair_products))

if __name__ == '__main__':
    checked()
