"""Exact rational certificate for four-observation isotonic Sobolev stability.

Requires Python 3 standard library only. Polynomial-identity checking uses
exact bivariate interpolation on a 5-by-5 integer grid: each determinant has
polynomial degree at most four in each variable. No floating-point tests are
needed for the claimed formulas.
"""
from fractions import Fraction as F
from itertools import permutations

PARTITIONS = [(1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3),
              (2, 1, 1), (2, 2), (3, 1), (4,)]


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def det(a):
    n = len(a)
    out = F(0)
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = F(-1 if inversions % 2 else 1)
        for i in range(n):
            term *= a[i][p[i]]
        out += term
    return out


def matrices(g, comp):
    n = 4
    q = [[F(i == j) for j in range(n)] for i in range(n)]
    for i in range(n - 1):
        q[i][i] += g
        q[i + 1][i + 1] += g
        q[i][i + 1] -= g
        q[i + 1][i] -= g
    p = [[F(0) for _ in range(n)] for _ in range(n)]
    start = 0
    for length in comp:
        for i in range(start, start + length):
            for j in range(start, start + length):
                p[i][j] = F(1, length)
        start += length
    assert start == n
    return q, p


def predicted_det(g, t, comp):
    d = (2*g + 1) * (2*g*g + 4*g + 1)
    if comp == (1, 1, 1, 1):
        return (1-t)**4 * d
    if comp == (4,):
        return t**3*(t-1)*d
    if comp in ((1, 3), (3, 1)):
        h = ((36*g**3+90*g*g+54*g+9)*t
             - (56*g**3+98*g*g+54*g+9))
        return t*t*(t-1)*h/9
    if comp == (2, 2):
        h = (2*g*g+4*g+1)*t - (3*g*g+4*g+1)
        return t*t*(t-1)*(2*g+1)*h
    if comp == (1, 2, 1):
        h = (2*g*g+4*g+1)*t - (3*g*g+4*g+1)
        return t*(t-1)**2*(2*g+1)*h
    if comp in ((1, 1, 2), (2, 1, 1)):
        h = ((16*g**3+40*g*g+24*g+4)*t
             - (20*g**3+43*g*g+24*g+4))
        return t*(t-1)**2*h/4
    raise ValueError(comp)


def pava(values):
    blocks = [[F(x)] for x in values]
    k = 0
    while k < len(blocks) - 1:
        if sum(blocks[k], F(0))/len(blocks[k]) > sum(blocks[k+1], F(0))/len(blocks[k+1]):
            blocks[k:k+2] = [blocks[k]+blocks[k+1]]
            k = max(0, k-1)
        else:
            k += 1
    return [sum(block, F(0))/len(block) for block in blocks for _ in block]


def qnorm2(v, q):
    return sum((v[i]*q[i][j]*v[j] for i in range(4) for j in range(4)), F(0))


def check():
    count = 0
    # Both sides are polynomials of bidegree <= (4,4) in (g,t).
    # Equality on five distinct rational values of each variable proves
    # polynomial identity over Q, not merely a finite-parameter observation.
    for comp in PARTITIONS:
        for gi in range(5):
            g = F(gi)
            q,p = matrices(g, comp)
            pqp = matmul(matmul(p,q),p)
            for ti in range(5):
                t = F(ti)
                left = det([[pqp[i][j]-t*q[i][j] for j in range(4)]
                            for i in range(4)])
                right = predicted_det(g,t,comp)
                assert left == right, (comp,g,t,left,right)
                count += 1
    # Further noninteger checks, explicitly supplementary.
    for comp in PARTITIONS:
        for g in (F(1,10),F(1,2),F(7,5)):
            q,p = matrices(g,comp)
            pqp = matmul(matmul(p,q),p)
            for t in (F(1,7),F(13,9)):
                assert det([[pqp[i][j]-t*q[i][j] for j in range(4)]
                            for i in range(4)]) == predicted_det(g,t,comp)
                count += 1
    # Actual pairs exactly attain the leading branches on their open PAV cells.
    for g,comp,x,v,target in (
        (F(1), (1,3), [F(-10),F(3),F(2),F(1)],
         [F(-31),F(1),F(13),F(17)], F(31,27)),
        (F(1,10), (2,2), [F(2),F(1),F(5),F(4)],
         [F(-7),F(-6),F(6),F(7)], F(143,142))):
        eps=F(1,100)
        y=[x[i]+eps*v[i] for i in range(4)]
        px=pava(x)
        py=pava(y)
        q,_=matrices(g,comp)
        delta=[py[i]-px[i] for i in range(4)]
        diff=[y[i]-x[i] for i in range(4)]
        assert qnorm2(delta,q) == target*qnorm2(diff,q)
        count += 1
    print('EXACT_FOUR_POINT_ISOTONIC_SOBLEV_CERTIFICATE_OK', count)

if __name__ == '__main__':
    check()
