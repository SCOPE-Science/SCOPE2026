"""Exact rational checks for the alternating variable-step BDF3 Floquet law.

Python 3 standard library only. Finite tests supplement the symbolic proof.
"""
from fractions import Fraction as F


def mul(X, Y):
    return [[sum((X[i][k] * Y[k][j] for k in range(3)), F(0))
             for j in range(3)] for i in range(3)]


def det(X):
    a, b, c = X
    return a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0])


def step_pair(r, q):
    r, q = F(r), F(q)
    E1, E2 = 5*r*r+5*r+1, r*r+5*r+5
    d1 = 1/r + 1/(r+1) + 1/(2*r+1)
    d2 = 1 + 1/(r+1) + 1/(r+2)
    A = [[(r+1)*(2*r+1)**2/E1, -r*(2*r+1)**2/E1, r*(r+1)/E1],
         [F(1), F(0), F(0)], [F(0), F(1), F(0)]]
    B = [[(r+1)*(r+2)**2/(r*E2), -(r+2)**2/(r*E2), (r+1)/E2],
         [F(1), F(0), F(0)], [F(0), F(1), F(0)]]
    A[0] = [z*d1/(d1+q) for z in A[0]]
    B[0] = [z*d2/(d2+q) for z in B[0]]
    return A, B, mul(B, A)


def check():
    trials = [F(1, 1000), F(1, 20), F(1, 3), F(1), F(2), F(3), F(10), F(100), F(1000)]
    for r in trials:
        A, B, P = step_pair(r, F(0))
        assert all(sum(row) == 1 for row in (A[0], B[0]))
        E = (r*r+5*r+5)*(5*r*r+5*r+1)
        S = -(r**4-r**3-5*r*r-r+1)/E
        D = r*(r+1)**2/E
        assert det(P) == D
        assert P[0][0]+P[1][1]+P[2][2] == 1+S
        assert (1-S+D) > 0 and (1+S+D) > 0 and (1-D) > 0
    for r in trials:
        for q in [F(1, 100), F(1, 10), F(1), F(2), F(10)]:
            A, B, P = step_pair(r, q)
            assert all(z.denominator > 0 for row in P for z in row)
            assert det(P) > 0
            # Right-hand-side damping and subdiagonal structure.
            assert all(A[1][i] == [1,0,0][i] for i in range(3))
            assert all(B[2][i] == [0,1,0][i] for i in range(3))
    _, _, W = step_pair(F(100), F(1, 10))
    witness = det([[W[i][j]+int(i==j) for j in range(3)] for i in range(3)])
    assert witness == F(-4621393451, 14621500436), witness
    print("VERIFY_OK: nine exact zero-ODE monodromies, 45 damped two-period maps, exact negative-real-axis instability certificate")


if __name__ == '__main__':
    check()
