#!/usr/bin/env python3
"""Independent finite checks for the characteristic-three nine-variable quartic.

Uses only the Python standard library. Finite checks support, but do not replace,
the characteristic-three algebraic-closure proof in RESULT.md.
"""
from itertools import combinations, product
from math import comb

P = 3
N = 9


def e(values, degree):
    coeff = [1] + [0] * degree
    for value in values:
        for j in range(degree, 0, -1):
            coeff[j] = (coeff[j] + value * coeff[j - 1]) % P
    return coeff[degree]


def grad(values):
    return tuple(e(values[:i] + values[i+1:], 3) for i in range(N))


def normalize(v):
    for z in v:
        if z:
            multiplier = pow(z, -1, P)
            return tuple((multiplier * x) % P for x in v)
    return None


def rref(rows):
    matrix = [list(r) for r in rows]
    pivot_row = 0
    for j in range(N):
        found = next((r for r in range(pivot_row, len(matrix)) if matrix[r][j] % P), None)
        if found is None:
            continue
        matrix[pivot_row], matrix[found] = matrix[found], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][j] % P, -1, P)
        matrix[pivot_row] = [(inverse * z) % P for z in matrix[pivot_row]]
        for r in range(len(matrix)):
            if r != pivot_row:
                multiple = matrix[r][j] % P
                matrix[r] = [(x - multiple * y) % P for x,y in zip(matrix[r],matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix)


def line_bases():
    for i,j in combinations(range(N),2):
        first = tuple(int(k == i) for k in range(N))
        second = tuple(int(k == j) for k in range(N))
        yield 'coordinate',first,second
    for i in range(N):
        remaining = [k for k in range(N) if k != i]
        for block in combinations(remaining,4):
            block = set(block)
            complement = set(remaining)-block
            if min(block) > min(complement):
                continue
            first = tuple(int(k == i) for k in range(N))
            second = tuple(1 if k in block else 2 if k in complement else 0 for k in range(N))
            yield 'balanced',first,second


def restricted_gradient_coefficients(a,b,i):
    """Coefficients of s^(3-j)*t^j in derivative restricted to span(a,b)."""
    ans=[0]*4
    pool=[k for k in range(N) if k!=i]
    for inds in combinations(pool,3):
        poly=[1,0,0,0]
        for k in inds:
            nxt=[0,0,0,0]
            for j in range(4):
                nxt[j]=(nxt[j]+poly[j]*a[k])%P
                if j+1<=3: nxt[j+1]=(nxt[j+1]+poly[j]*b[k])%P
            poly=nxt
        ans=[(x+y)%P for x,y in zip(ans,poly)]
    return ans


def two_value_derivative_coeffs(count_a):
    """Each derivative is a cubic in a,b; returns coefficient vector a^j b^(3-j)."""
    def c(a,b):
        return tuple(sum(comb(a,j)*comb(b,3-j) for j in (m,) if j<=a and 3-j<=b)%P for m in range(4))
    return c(count_a-1,N-count_a),c(count_a,N-count_a-1)


def main():
    lines=list(line_bases())
    assert len(lines)==351
    assert sum(typ=='coordinate' for typ,*_ in lines)==36
    assert sum(typ=='balanced' for typ,*_ in lines)==315
    assert len({rref((a,b)) for typ,a,b in lines})==351
    for typ,a,b in lines:
        for k in range(N):
            assert restricted_gradient_coefficients(a,b,k)==[0,0,0,0],(typ,k)
    # An independent brute-force enumeration of all F_3 projective points.
    predicted=set()
    for typ,a,b in lines:
        for s,t in product(range(P),repeat=2):
            if s or t:
                predicted.add(normalize(tuple((s*x+t*y)%P for x,y in zip(a,b))))
    actual={v for v in product(range(P),repeat=N) if normalize(v)==v and not any(grad(v))}
    assert len(actual)==len(predicted)==522
    assert actual==predicted
    # Independently reconstruct the eight two-block derivative coefficient pairs.
    expected=[
        ((2,0,0,0),(2,0,0,0)),
        ((2,0,0,0),(2,0,0,0)),
        ((2,0,0,0),(1,0,0,1)),
        ((1,0,0,1),(1,0,0,1)),
        ((1,0,0,1),(1,0,0,1)),
        ((1,0,0,1),(0,0,0,2)),
        ((0,0,0,2),(0,0,0,2)),
        ((0,0,0,2),(0,0,0,2))
    ]
    assert [two_value_derivative_coeffs(r) for r in range(1,9)]==expected
    print('VERIFY_OK: 36 coordinate + 315 balanced distinct singular lines; 522/522 projective F3 points; 8 two-value coefficient cases.')

if __name__=='__main__':
    main()
