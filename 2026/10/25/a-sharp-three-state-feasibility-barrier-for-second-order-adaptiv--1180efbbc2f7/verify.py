"""Exact rational checks for the adaptive SSPRK(3,3) positivity theorem.

These checks are finite algebraic tests; the accompanying analytical proof
establishes the universal quantifiers.
"""
from fractions import Fraction as F


def identity(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rk(q, z, v):
    n = len(q)
    q2 = mul(q, q)
    q3 = mul(q2, q)
    eye = identity(n)
    return [[eye[i][j] + z*q[i][j] + z*z*q2[i][j]/2 + v*z*z*z*q3[i][j]/4
             for j in range(n)] for i in range(n)]


def nonnegative_stochastic(matrix):
    return all(x >= 0 for row in matrix for x in row) and all(
        sum((matrix[i][j] for i in range(len(matrix))), F(0)) == 1
        for j in range(len(matrix)))


def check_three():
    q = [[F(-1), F(0), F(0)], [F(1), F(-1), F(0)], [F(0), F(1), F(0)]]
    for z in [F(0), F(1, 3), F(1), F(3, 2), F(2), F(11, 4), F(3), F(4)]:
        v = F(0) if z <= 1 else 4 * (z - 1) / (3*z*z)
        assert F(0) <= v <= F(1)
        mat = rk(q, z, v)
        a = 1 - z + z*z/2 - v*z*z*z/4
        b = z - z*z + 3*v*z*z*z/4
        c = z*z/2 - v*z*z*z/2
        assert mat == [[a, F(0), F(0)], [b, a, F(0)], [c, 1-a, F(1)]]
        assert nonnegative_stochastic(mat)
        if z == 4:
            assert v == F(1, 4) and mat == identity(3)
    for z in [F(17, 4), F(5), F(7), F(100)]:
        lower = 4*(z-1)/(3*z*z)
        upper = 1/z
        assert lower > upper
        # Illustrate why no v satisfies two necessary positivity inequalities.
        for v in [F(-3), F(0), lower, (lower+upper)/2, upper, F(1), F(4)]:
            mat = rk(q,z,v)
            assert mat[1][0] < 0 or mat[2][0] < 0


def check_two():
    for a,b in [(F(0),F(0)),(F(1),F(0)),(F(0),F(3)),
                (F(1),F(2)),(F(7,2),F(1,3))]:
        q = [[-a,b],[a,-b]]
        for h in [F(0),F(1,10),F(1,2),F(1),F(2),F(5),F(100)]:
            z = h*(a+b)
            v = F(0) if z < 2 or z == 0 else 4*(1-z+z*z/2)/(z*z*z)
            assert F(0) <= v <= F(1)
            m = rk(q,h,v)  # Directly use physical generator q and physical h.
            assert nonnegative_stochastic(m)
            if z >= 2 and z > 0:
                pi = [[b/(a+b), b/(a+b)], [a/(a+b),a/(a+b)]]
                assert m == pi


if __name__ == '__main__':
    check_three()
    check_two()
    print('VERIFY_OK')
