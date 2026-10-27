"""Exact checks for sparse density-dependent self-limitation in obligate mutualism."""
from fractions import Fraction as F
from itertools import product


def det(matrix):
    a = [row[:] for row in matrix]
    size = len(a)
    sign = 1
    output = F(1)
    for i in range(size):
        pivot = next((j for j in range(i, size) if a[j][i] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign = -sign
        d = a[i][i]
        output *= d
        for j in range(i + 1, size):
            c = a[j][i] / d
            for l in range(i + 1, size):
                a[j][l] -= c * a[i][l]
    return sign * output


def negative_definite(m):
    return all((-1) ** k * det([row[:k] for row in m[:k]]) > 0
               for k in range(1, len(m) + 1))


def check(n, a, b, d, m):
    k = n - m
    B = (n-1)*b-d
    if B <= 0 or m < 1:
        return False
    D = d - b*(k-1)
    if D <= 0:
        return False
    C = B*(d+b)/D
    E = a*(d+b)/D
    critical = C*C/(4*E)
    h = F(8,9)*critical
    xp, xm = 3*a/B, 3*a/(2*B)
    for x,should_stabilize in [(xp, True),(xm, False)]:
        y = (b*m*x-a)/D if k else None
        assert x > 0 and (not k or y > 0)
        abund = [x]*m + ([y]*k if k else [])
        for i in range(n):
            growth = -a-d*abund[i]+b*sum(abund[j] for j in range(n) if j!=i)
            if i < m:
                growth-= h*abund[i]**2
            assert growth == 0, (n,a,b,d,m,i,growth)
        mat = [[b if i!=j else -d-(2*h*x if i<m else 0)
                for j in range(n)] for i in range(n)]
        assert negative_definite(mat) is should_stabilize, (n,a,b,d,m,x)
        assert (h*x > C/2) is should_stabilize
    assert critical==B*B*(d+b)/(4*a*D)
    return True


def main():
    count = 0
    for n in range(2,9):
        for a,b,d in product([F(1),F(2)], [F(1),F(2),F(3)], [F(1,2),F(1),F(2),F(3),F(4)]):
            if (n-1)*b<=d:
                continue
            for m in range(1,n+1):
                k=n-m
                predicted = d>b*(k-1)
                got = check(n,a,b,d,m)
                assert got==predicted,(n,a,b,d,m)
                count += 1
    print('PASS:',count,'exact parameter/group configurations; 2 equilibria each in feasible cases; exact determinants.')

if __name__=='__main__':
    main()
