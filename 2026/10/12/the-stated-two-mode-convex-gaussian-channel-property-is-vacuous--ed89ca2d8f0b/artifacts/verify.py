import cmath
import math

TOL = 1e-10


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def maxabs(a):
    return max(abs(x) for row in a for x in row)


def kron(a, b):
    return [[a[i][j] * b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def block(m, idx):
    return [[m[i][j] for j in idx] for i in idx]


def ident(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def check_su2_block(a, b):
    u = [[a, -b.conjugate()], [b, a.conjugate()]]
    assert abs(det2(u) - 1) < TOL
    assert maxabs(sub(matmul(dagger(u), u), ident(2))) < TOL


def main():
    I = [[1, 0], [0, 1]]
    X = [[0, 1], [1, 0]]
    Y = [[0, -1j], [1j, 0]]
    Z = [[1, 0], [0, -1]]
    paulis = [I, X, Y, Z]

    P = kron(Z, Z)
    SWAP = [[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]]
    assert maxabs(sub(matmul(P, SWAP), matmul(SWAP, P))) < TOL

    A = block(SWAP, [0, 3])
    B = block(SWAP, [1, 2])
    eta = 0.5 * abs(det2(A) - det2(B))
    assert abs(eta - 1) < TOL

    def cplus(p):
        inside = 0.5 * eta * (1-p) * (2-p) + p*p/8 - p/2
        return max(0.0, inside)

    assert abs(cplus(0.0) - 1.0) < TOL
    pstar = (8 - 2 * math.sqrt(6)) / 5
    inside_star = 0.5 * (1-pstar) * (2-pstar) + pstar*pstar/8 - pstar/2
    assert abs(inside_star) < 1e-9

    # Every Pauli-string branch either commutes or anticommutes with total parity.
    for a in paulis:
        for b in paulis:
            k = kron(a, b)
            comm = sub(matmul(P, k), matmul(k, P))
            anti = add(matmul(P, k), matmul(k, P))
            assert maxabs(comm) < TOL or maxabs(anti) < TOL

    # Representative arbitrary-sector SU(2) blocks used in the analytic proof.
    a = (2 + 1j) / math.sqrt(6)
    b = 1 / math.sqrt(6)
    check_su2_block(a, b)
    c = (1 - 1j) / math.sqrt(3)
    d = 1 / math.sqrt(3)
    check_su2_block(c, d)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
