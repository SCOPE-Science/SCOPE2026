"""Exact rational finite checks for the complete-bipartite Hilbert distance."""
from fractions import Fraction as F
from itertools import product


def potential(m, n, left, right):
    x = [F(t) for t in left]
    y = [F(t) for t in right]
    xb = sum(x, F(0)) / m
    yb = sum(y, F(0)) / n
    h = xb - yb
    u = [t - xb for t in x]
    v = [t - yb for t in y]
    q = h*h + sum((t*t for t in u), F(0)) / m + sum((t*t for t in v), F(0)) / n
    lip = max(abs(a-b) for a in x for b in y)
    return q, lip


def run():
    count = 0
    for m, n in product(range(3, 9), repeat=2):
        d = m+n-1
        # Exactly all active-edge-spanning sign-pattern vertices.
        for signs in product((-1, 1), repeat=m):
            q, lip = potential(m, n, signs, [0]*n)
            assert q == 1 and lip == 1
            count += 1
        for signs in product((-1, 1), repeat=n):
            q, lip = potential(m, n, [0]*m, signs)
            assert q == 1 and lip == 1
            count += 1
        x = [m-1] + [-1]*(m-1)
        y = [-(n-1)] + [1]*(n-1)
        # The difference in means is +1, while both sets of fluctuations sum to 0.
        x = [t+1 for t in x]
        q, lip = potential(m, n, x, y)
        assert q == d and lip == d
        assert lip*lip == d*q
        count += 1
        # The symmetry-minimax lower certificate at representative rational values.
        for gamma in (F(1, 4), F(1, 2), F(3, 4), F(1)):
            dm = F(0) if m % 2 == 0 else F(1, m*m)
            dn = F(0) if n % 2 == 0 else F(1, n*n)
            a = (1 - gamma*dm) / (m*(1-dm))
            b = (1 - gamma*dn) / (n*(1-dn))
            dual = 1/gamma + F(m-1,m)/a + F(n-1,n)/b
            assert dual >= d
            count += 1
    print('COMPLETE_BIPARTITE_HILBERT_EXACT_OK', count)

if __name__ == '__main__':
    run()
