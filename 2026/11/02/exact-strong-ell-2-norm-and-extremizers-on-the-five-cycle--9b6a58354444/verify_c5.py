"""Exact, stdlib-only certificate for the five-cycle maximal averaging norm.

Run: python3 verify_c5.py
No floating-point comparisons and no external software required.
"""
from fractions import Fraction as Q
from itertools import product

N = 5
T = Q(1463, 1000)
PATTERN = (2, 2, 0, 1, 0)
WINNERS = {tuple(PATTERN[(i + j) % N] for i in range(N)) for j in range(N)}


def distances(origin):
    # Breadth-first graph distances; independently generates metric balls.
    d = {origin: 0}
    queue = [origin]
    for x in queue:
        for y in ((x - 1) % N, (x + 1) % N):
            if y not in d:
                d[y] = d[x] + 1
                queue.append(y)
    assert len(d) == N
    return d


ROWS = []
for vertex in range(N):
    d = distances(vertex)
    choices = []
    for radius in range(3):
        ball = [j for j in range(N) if d[j] <= radius]
        choices.append(tuple(Q(1, len(ball)) if j in ball else Q(0) for j in range(N)))
    assert list(map(lambda z: sum(z), choices)) == [1, 1, 1]
    assert [sum(x != 0 for x in row) for row in choices] == [1, 3, 5]
    ROWS.append(choices)


def gram(pattern):
    rows = [ROWS[i][pattern[i]] for i in range(N)]
    return [[sum((rows[i][j] * rows[i][k] for i in range(N)), Q(0))
             for k in range(N)] for j in range(N)]


def positive_definite_ldlt(matrix):
    n = len(matrix)
    lower = [[Q(0)] * n for _ in range(n)]
    diagonal = []
    for i in range(n):
        lower[i][i] = Q(1)
        pivot = matrix[i][i] - sum(
            (lower[i][j]**2 * diagonal[j] for j in range(i)), Q(0))
        if pivot <= 0:
            return False
        diagonal.append(pivot)
        for k in range(i + 1, n):
            lower[k][i] = (
                matrix[k][i] - sum((lower[k][j] * lower[i][j] * diagonal[j]
                                     for j in range(i)), Q(0))) / pivot
    return True


def determinant3(m):
    a, b, c = m
    return a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0])


def poly(t):
    return 225*t**3 - 390*t**2 + 91*t - 4


def main():
    checked = 0
    for pattern in product(range(3), repeat=N):
        matrix = gram(pattern)
        assert all(matrix[i][j] == matrix[j][i] for i in range(N) for j in range(N))
        if pattern not in WINNERS:
            assert positive_definite_ldlt([
                [((T if i == j else Q(0)) - matrix[i][j]) for j in range(N)]
                for i in range(N)])
            checked += 1
    assert checked == 238 and len(WINNERS) == 5

    # The five winners are conjugate by cyclic rotation.
    for shift in range(N):
        pat = tuple(PATTERN[(i + shift) % N] for i in range(N))
        assert pat in WINNERS
        for i in range(N):
            for j in range(N):
                assert gram(pat)[i][j] == gram(PATTERN)[(i + shift) % N][(j + shift) % N]

    # The restriction to f=(a,a,b,c,b) has energy numerator x^T B x
    # and denominator x^T D x. Its characteristic determinant is -4/225 poly(t).
    B = [[Q(8,25), Q(8,25), Q(4,25)],
         [Q(8,25), Q(622,225), Q(86,225)],
         [Q(4,25), Q(86,225), Q(43,225)]]
    D = [Q(2), Q(2), Q(1)]
    for k in range(4):
        t = Q(k)
        mat = [[B[i][j] - (t*D[i] if i == j else Q(0))
                for j in range(3)] for i in range(3)]
        assert determinant3(mat) == -Q(4,225)*poly(t)
    # Four evaluations suffice because both sides are cubic polynomials.
    lower, upper = Q(293,200), Q(733,500)
    assert lower > T and poly(lower) < 0 < poly(upper)
    # poly'(t)=675 t^2-780 t+91 is positive and increasing above lower.
    assert 675*lower**2 - 780*lower + 91 > 0
    assert 1350*lower - 780 > 0

    # The top eigendirection f=(a,a,1,c,1) has these exact expressions.
    # With the root between lower and upper, obtain simple rational bounds.
    c_lo, c_hi = (lower - 1)/lower, (upper - 1)/upper
    a_lo = (4 + 2*c_lo)/(25*upper - 4)
    a_hi = (4 + 2*c_hi)/(25*lower - 4)
    assert Q(31,100) < c_lo < c_hi < Q(33,100)
    assert Q(7,50) < a_lo < a_hi < Q(3,20)
    # These intervals ensure the selected rows really are maximizers:
    # 2/5 global rows, 2 singleton rows, 1 nearest-neighbor row.
    assert (2*Q(7,50)+2+Q(31,100))/5 > (2*Q(3,20)+1)/3
    assert (2*Q(3,20)+2+Q(33,100))/5 < 1
    assert (2+Q(31,100))/3 > (2*Q(3,20)+2+Q(33,100))/5

    print('CERTIFICATE_OK: 243 choices; 238 strict LDL bounds; 5 rotational maximizers;')
    print('               cubic identity, root isolation, positive extremizer and activation.')


if __name__ == '__main__':
    main()
