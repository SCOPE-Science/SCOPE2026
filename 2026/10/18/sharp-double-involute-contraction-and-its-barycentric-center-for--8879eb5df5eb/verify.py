"""Exact rational spot checks for the hexagonal involute theorem.

Run: python3 verify.py
The all-parameter proof is algebraic and is given in RESULT.md.
"""
from fractions import Fraction as F


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def neg(a): return (-a[0], -a[1])
def sub(a, b): return add(a, neg(b))
def mul(t, a): return (t * a[0], t * a[1])
def det(a, b): return a[0] * b[1] - a[1] * b[0]


def coefficient(v, basis):
    if basis[0]:
        t = v[0] / basis[0]
    else:
        t = v[1] / basis[1]
    assert v == mul(t, basis)
    return t


def involute(X, U):
    """(3.14),(4.1) from Craizer--Martini; double vertices are 3-periodic."""
    out = []
    V = []
    alpha = []
    c = []
    for i in range(6):
        j = (i + 1) % 6
        d = sub(U[j], U[i])
        c.append(det(U[i], U[j]))
        V.append(mul(1 / c[-1], d))
        alpha.append(coefficient(sub(X[j], X[i]), d))
    for i in range(6):
        b = sum((alpha[(i + j) % 6] * c[(i + j) % 6]
                 for j in range(3)), F(0)) / 2
        out.append(add(X[i], mul(b, V[i])))
    assert all(out[i + 3] == out[i] for i in range(3))
    return out, V


def full_step(M, U):
    N, V = involute(M, U)
    Z, W = involute(N, V)
    assert all(W[i] == neg(U[(i + 1) % 6]) for i in range(6))
    return [Z[(i - 1) % 6] for i in range(6)], N


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), F(0))
             for j in range(3)] for i in range(3)]


def test(p, q):
    U = [(F(1), F(0)), (F(0), F(1)), (-p, q),
         (F(-1), F(0)), (F(0), F(-1)), (p, -q)]
    a, b, c = F(1), p, q
    x, y, z = b + c - a, c + a - b, a + b - c
    assert min(x, y, z) > 0
    cs = [det(U[i], U[i + 1]) for i in range(3)]
    assert cs == [a, b, c]
    lam = x*y*z / (4*a*b*c)
    Q = b*y*y + c*z*z + a*x*x
    assert Q + x*y*z == 4*a*b*c
    w = [b*y*y/Q, c*z*z/Q, a*x*x/Q]
    assert sum(w) == 1
    t = [z/(2*a), x/(2*b), y/(2*c)]
    r = [x/(2*c), y/(2*a), z/(2*b)]
    Nmatrix = [[F(0)]*3 for _ in range(3)]
    Rmatrix = [[F(0)]*3 for _ in range(3)]
    for i in range(3):
        Nmatrix[i][i] = 1-t[i]
        Nmatrix[i][(i+1)%3] = t[i]
        Rmatrix[(i+1)%3][i] = 1-r[i]
        Rmatrix[(i+1)%3][(i+1)%3] = r[i]
    A = matmul(Rmatrix, Nmatrix)
    assert A == [[(lam if i == j else F(0))+(1-lam)*w[j]
                  for j in range(3)] for i in range(3)]

    # Arbitrarily shifted nondegenerate central triangle, scaled small
    d = [sub(U[(i+1)%6],U[i]) for i in range(3)]
    alphas = [x, -y, z]
    assert add(add(mul(alphas[0],d[0]),mul(alphas[1],d[1])),mul(alphas[2],d[2])) == (F(0),F(0))
    m0=(F(2,7),F(-1,5))
    eps=F(1,100)
    M3=[m0,add(m0,mul(eps*alphas[0],d[0]))]
    M3.append(add(M3[-1],mul(eps*alphas[1],d[1])))
    M=M3+M3
    # P_{i+3}=M_i-U_i
    P=[add(M[i],U[i]) for i in range(3)]+[sub(M[i],U[i]) for i in range(3)]
    assert all(add(mul(F(1,2),P[i]),mul(F(1,2),P[i+3]))==M[i] for i in range(3))
    for i in range(6):
        e1=sub(P[(i+1)%6],P[i]);e2=sub(P[(i+2)%6],P[(i+1)%6]);assert det(e1,e2)>0
    O=add(add(mul(w[0],M[0]),mul(w[1],M[1])),mul(w[2],M[2]))
    for k in range(5):
        for i in range(3):
            assert M[i]==add(O,mul(lam**k,sub(M3[i],O)))
        MN,N=full_step(M,U)
        assert MN[:3]==[add(O,mul(lam,sub(M[i],O))) for i in range(3)]
        assert N[3:]==N[:3]
        M=MN
    print('verified',p,q,'lambda',lam,'weight',w)


if __name__ == '__main__':
    for p,q in [(F(1),F(1)),(F(6,5),F(9,10)),(F(2,3),F(5,6)),
                (F(5,2),F(2)),(F(3,4),F(3,2)),(F(3,10),F(4,5))]:
        test(p,q)
    print('All exact-rational checks passed.')
