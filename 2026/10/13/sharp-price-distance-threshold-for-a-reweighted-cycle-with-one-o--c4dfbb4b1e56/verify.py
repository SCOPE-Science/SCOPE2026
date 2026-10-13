"""Exact arithmetic checks for the priced-chord cycle threshold theorem.

Python 3 standard library only. Finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F


def delta(n, d):
    u = [F((n - d) * i, n) if i <= d else F(d * (n - i), n)
         for i in range(n)]
    mu = sum(u) / n
    b = [int(i == d) - int(i == 0) for i in range(n)]
    for i in range(n):
        assert 2*u[i] - u[(i - 1) % n] - u[(i + 1) % n] == b[i]
    v = sum((x - mu)**2 for x in u)
    expected = F(d * (n - d) * (d * (n - d) + 2), 12 * n)
    assert v == expected, (n, d, v, expected)
    return v


def invert(a):
    n = len(a)
    m = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for col in range(n):
        pivot = next(k for k in range(col, n) if m[k][col])
        m[col], m[pivot] = m[pivot], m[col]
        scale = m[col][col]
        m[col] = [x / scale for x in m[col]]
        for i in range(n):
            if i != col:
                v = m[i][col]
                if v:
                    m[i] = [x - v*y for x,y in zip(m[i],m[col])]
    return [row[n:] for row in m]


def index(n, d, price, epsilon):
    # A unit budget: each ring edge has (1-price*epsilon)/n,
    # and the new distance-d chord has epsilon.
    ring = (1 - price * epsilon)/n
    assert ring > 0
    a = [[F(1,n) for j in range(n)] for i in range(n)]
    for i in range(n):
        j = (i + 1) % n
        for p, q, sign in [(i,i,1),(j,j,1),(i,j,-1),(j,i,-1)]:
            a[p][q] += sign * ring
    for p, q, sign in [(0,0,1),(d,d,1),(0,d,-1),(d,0,-1)]:
        a[p][q] += sign * epsilon
    ia = invert(a)
    return n*(sum(ia[i][i] for i in range(n))-1)


def test():
    count = 0
    for n in range(4, 44):
        for d in range(1, n//2 + 1):
            ratio = delta(n, d) / delta(n, 1)
            expected = F(d*(n-d)*(d*(n-d)+2), n*n-1)
            assert ratio == expected
            count += 1
    # Real objective checks, exact rational, on both sides of the threshold.
    signs = 0
    for n in range(4, 11):
        for d in range(2, n//2+1):
            price_star = delta(n,d)/delta(n,1)
            base = index(n,d, F(1), F(0))
            e = F(1,1000000)
            assert index(n,d,price_star-F(1,20),e)<base
            assert index(n,d,price_star+F(1,20),e)>base
            signs += 2
    print(f'VERIFY_OK {count} exact cycle-Poisson/threshold identities; {signs} exact objective-side comparisons')

if __name__ == '__main__':
    test()
