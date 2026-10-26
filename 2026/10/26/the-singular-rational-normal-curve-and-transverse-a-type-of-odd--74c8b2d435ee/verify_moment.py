"""Exact rational checks for odd binary-form moment-map sections.

This verifies selected finite degrees. The all-degree theorem uses a separate
representation-theoretic and local normal-form argument.

Requires Python 3.9+ and only its standard library.
"""
from fractions import Fraction
from math import comb


def linear_solve(A, b):
    n = len(b)
    R = [[Fraction(z) for z in row] + [Fraction(b[i])]
         for i, row in enumerate(A)]
    for col in range(n):
        piv = next((i for i in range(col, n) if R[i][col]), None)
        if piv is None:
            raise ValueError('singular Hessian')
        R[col], R[piv] = R[piv], R[col]
        d = R[col][col]
        R[col] = [z / d for z in R[col]]
        for i in range(n):
            if i != col:
                d = R[i][col]
                R[i] = [R[i][j] - d * R[col][j] for j in range(n+1)]
    return [R[i][-1] for i in range(n)]


def coefficients(r):
    """Terms in F=(r-1)*a2*P0 + Q, with a0=1, a1=0 and q0=q1=0."""
    d = {}
    def add(indices, coeff):
        key = tuple(sorted(indices))
        d[key] = d.get(key, 0) + coeff
    for i in range(2, r - 2):
        add([2, i, r-1-i], (r-1) * (-1)**i * comb(r-1, i))
    for i in range(3, r - 1):
        add([i, r+1-i], (-1)**(i+1) * comb(r-1, i-1))
    return {idx: c for idx, c in d.items() if c}


def quadratic_data(r, t):
    U = list(range(3, r-1))
    pos = {index:j for j,index in enumerate(U)}
    n = len(U)
    H = [[Fraction(0) for _ in U] for _ in U]
    b = [Fraction(0) for _ in U]
    const = Fraction(0)
    terms = coefficients(r)
    for monomial, c in terms.items():
        assert sum(monomial) == r+1, 'incorrect weight'
        others = [i for i in monomial if i != 2]
        value = Fraction(c)*Fraction(t)**(len(monomial)-len(others))
        if len(others)==0:
            const += value
        elif len(others)==1:
            b[pos[others[0]]] += value
        elif len(others)==2:
            i,j=map(pos.get, others)
            if i==j: H[i][i] += 2*value
            else: H[i][j] += value; H[j][i] += value
        else:
            raise AssertionError('not quadratic in transverse variables')
    return H,b,const


def check(r):
    assert r >= 7 and r % 2 == 1
    H0,b0,c0=quadratic_data(r, 0)
    assert not any(b0) and c0 == 0
    linear_solve(H0, [0]*len(H0))
    H,b,c=quadratic_data(r, 1)
    u = linear_solve(H, [-z for z in b])
    critical = c + sum(x*y for x,y in zip(b,u))/2
    assert critical != 0
    print('r=%d, transverse A_%d, quadratic rank=%d, critical coefficient=%s'
          % (r,(r-1)//2,r-4,critical))
    return critical

if __name__ == '__main__':
    sample={7:Fraction(405), 9:Fraction(8960), 11:Fraction(984375,4)}
    for r in (7,9,11,13,15,17,19):
        c=check(r)
        if r in sample: assert c==sample[r]
    print('All exact finite tests passed; no finite test substitutes for the theorem.')
