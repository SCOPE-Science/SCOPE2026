"""Exact checks of character-deletion measurement ranks on finite abelian groups.

The matrices are in the Fourier-coefficient representation of the observations.
Fourier orthogonality equates their rank with the physical intensity/projector
measurement rank. No floating point and no external packages are used.
"""
from itertools import product
from fractions import Fraction
import random


def group(shape):
    return list(product(*(range(t) for t in shape)))


def add(a, b, shape):
    return tuple((x+y) % t for x, y, t in zip(a, b, shape))


def sub(a, b, shape):
    return tuple((x-y) % t for x, y, t in zip(a, b, shape))


def order(d, shape):
    zero = (0,)*len(shape)
    v = zero
    for j in range(1, len(group(shape))+1):
        v = add(v, d, shape)
        if v == zero:
            return j
    raise AssertionError('failed to find element order')


def rank_integer_matrix(matrix):
    if not matrix:
        return 0
    a = [[Fraction(int(v)) for v in row] for row in matrix]
    row_count, col_count = len(a), len(a[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = next((r for r in range(pivot_row, row_count) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        den = a[pivot_row][col]
        for c in range(col, col_count):
            a[pivot_row][c] /= den
        for r in range(pivot_row+1, row_count):
            factor = a[r][col]
            if factor:
                for c in range(col, col_count):
                    a[r][c] -= factor*a[pivot_row][c]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def fiber_matrix(shape, d):
    g = group(shape)
    zero = (0,)*len(shape)
    nz = [a for a in g if a != zero]
    columns = [(a, b) for a in nz for b in nz if sub(a,b,shape) == d]
    matrix = [[int(a != j and b != j) for a,b in columns] for j in nz]
    return columns, matrix


def kernel_construction(shape, d, coset):
    zero = (0,)*len(shape)
    assert d != zero and order(d,shape)%2 == 0
    r = order(d,shape)
    x = {}
    for t in range(r):
        j = add(coset,tuple((t*v)%m for v,m in zip(d,shape)),shape)
        assert j != zero and j != d
        x[j] = (-1)**t
    return x


def verify_group(shape):
    g = group(shape)
    n = len(g)
    if n < 4:
        return None
    zero = (0,)*len(shape)
    nz = [a for a in g if a != zero]
    defect = 0
    for d in g:
        cols,mat = fiber_matrix(shape,d)
        observed = rank_integer_matrix(mat)
        if d == zero:
            assert observed == n-1 and len(cols) == n-1
            continue
        r = order(d,shape)
        expected_defect = n//r-1 if r%2 == 0 else 0
        assert len(cols) == n-2
        assert observed == len(cols)-expected_defect, (shape,d,observed,expected_defect)
        defect += expected_defect
        if r%2 == 0:
            subgroup = set()
            v = zero
            for _ in range(r):
                subgroup.add(v)
                v = add(v,d,shape)
            cosets = set()
            for a in g:
                if a in subgroup: continue
                orbit = frozenset(add(a,b,shape) for b in subgroup)
                if orbit in cosets: continue
                cosets.add(orbit)
                x = kernel_construction(shape,d,a)
                vector = [x.get(j,0) for j,k in cols]
                assert all(sum(t*v for t,v in zip(row,vector)) == 0 for row in mat)
            assert len(cosets) == n//r-1
    expected = (n-1)**2-defect
    assert expected == sum(rank_integer_matrix(fiber_matrix(shape,d)[1]) for d in g)
    return expected,defect


def verify_odd_reconstruction(shape):
    g=group(shape)
    n=len(g)
    assert n>=5 and n%2==1
    zero=(0,)*len(shape)
    nz=[a for a in g if a!=zero]
    rng=random.Random(240517+n+sum(shape))
    for trial in range(20):
        a={t:0 if t==zero else rng.randrange(-3,4) for t in g}
        # The projected intensity Fourier coefficients T[d][j] for deletion j.
        T={(d,j):sum(a[u]*a[v] for u in nz for v in nz
                         if sub(u,v,shape)==d and u!=j and v!=j)
           for d in g for j in nz}
        for d in g:
            if d==zero:
                sd=Fraction(sum(T[(d,j)] for j in nz),n-2)
                for j in nz:
                    assert sd-T[(d,j)] == a[j]*a[j]
            else:
                sd=Fraction(sum(T[(d,j)] for j in nz),n-3)
                b={j:(sd-T[(d,j)]) if j!=zero else 0 for j in g}
                r=order(d,shape)
                assert r%2 == 1
                for j in g:
                    val = sum(((-1)**t)*b[add(j,tuple((t*v)%m for v,m in zip(d,shape)),shape)]
                              for t in range(r))
                    assert val == 2*a[j]*a[sub(j,d,shape)], (shape,d,j,val)
    return 20


def main():
    shapes = [(4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,), (12,),
              (15,), (16,), (18,), (2,2), (2,3), (2,4), (2,2,2),
              (3,3), (3,5), (2,2,3), (2,2,2,2)]
    count = 0
    for shape in shapes:
        rank,defect=verify_group(shape)
        count += 1
        if len(group(shape))%2:
            verify_odd_reconstruction(shape)
        print('shape',shape,'order',len(group(shape)),'rank',rank,'nullity',defect)
    assert verify_group((8,)) == (44,5)
    assert verify_group((4,2)) == (36,13)
    assert verify_group((2,2,2)) == (28,21)
    print('VERIFY_OK groups=',count)

if __name__=='__main__':
    main()
