#!/usr/bin/env python3
"""Independent small-field checks for zero products in truncated cycle path algebras.

Usage: python3 checker.py. No non-stdlib dependencies.
"""
from itertools import product


def arcs(word):
    n = len(word)
    return [((i, (i + 1) % n) if ch == '+' else ((i + 1) % n, i))
            for i, ch in enumerate(word)]


def direct_counts(q, word):
    n = len(word)
    edges = arcs(word)
    elems = list(product(range(q), repeat=2*n))
    zero = (0,) * (2*n)
    out = [0, 0]
    # Direct multiplication in the vertex-and-arrow basis of kQ/J^2.
    for x in elems:
        for y in elems:
            xy = [x[i]*y[i] % q for i in range(n)]
            yx = [y[i]*x[i] % q for i in range(n)]
            for a,(tail,head) in enumerate(edges):
                xy.append((x[tail]*y[n+a]+x[n+a]*y[head]) % q)
                yx.append((y[tail]*x[n+a]+y[n+a]*x[head]) % q)
            if tuple(xy) == zero:
                out[0] += 1
                if tuple(yx) == zero:
                    out[1] += 1
    return tuple(out)


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def transfer_counts(q, word):
    n = len(word)
    # State 0: (d,h)=(0,0); L: (d!=0,h=0); R: (d=0,h!=0).
    multiplicity = (1,q-1,q-1)
    d = (0,1,0)
    h = (0,0,1)
    W = [[q**(2-int(bool(d[i] or h[j]))) for j in range(3)] for i in range(3)]
    M = [[W[i][j]*multiplicity[j] for j in range(3)] for i in range(3)]
    MT = [[W[j][i]*multiplicity[j] for j in range(3)] for i in range(3)]
    # Both equations have 0, 1, or 2 independent arrow coefficients.
    rank = lambda i,j: int(bool(d[i] or d[j] or h[i] or h[j]))
    B = [[q**(2-rank(i,j))*multiplicity[j] for j in range(3)] for i in range(3)]
    I = [[int(i==j) for j in range(3)] for i in range(3)]
    P=I
    for ch in word:
        P = matmul(P, M if ch=='+' else MT)
    Q=I
    for _ in word:
        Q=matmul(Q,B)
    return sum(P[i][i] for i in range(3)),sum(Q[i][i] for i in range(3))


def verify_symbolic_matrix_identities():
    # Every entry of each transfer matrix has polynomial degree <= 3 in q.
    # Both sides of the four-edge identity have degree at most 12. Equality at
    # 13 distinct integer q proves a polynomial identity over the rationals.
    def charpoly3(A):
        a11,a12,a13=A[0];a21,a22,a23=A[1];a31,a32,a33=A[2]
        tr=a11+a22+a33
        minor=(a11*a22-a12*a21)+(a11*a33-a13*a31)+(a22*a33-a23*a32)
        det=(a11*(a22*a33-a23*a32)-a12*(a21*a33-a23*a31)
             +a13*(a21*a32-a22*a31))
        return (-tr, minor, -det) # coefficients of t^2,t,constant

    for q in range(13):
        g = (1,q-1,q-1)
        W = [[q*q,q*q,q],[q,q,q],[q*q,q*q,q]]
        M = [[W[i][j]*g[j] for j in range(3)] for i in range(3)]
        B = [[q*q,q*(q-1),q*(q-1)],
             [q,q*(q-1),q*(q-1)],
             [q,q*(q-1),q*(q-1)]]
        a=q*(3*q-2)
        b=q*q*(q-1)**3
        c=2*q*q*(q-1)**2
        assert charpoly3(M)==(-a,-b,0)
        assert charpoly3(B)==(-a,c,0)
        delta=(transfer_counts(q, '+-+-')[0]-transfer_counts(q,'++++')[0])
        factor=q**4*(q-1)**3*(q**5+3*q**4+8*q**3-8*q**2-q+1)
        assert delta==factor, (q,delta,factor)
    print('symbolic polynomial identities: 13 exact interpolation points, degree <=12')


def test():
    verify_symbolic_matrix_identities()
    cases = [(2,'+++'),(2,'++-'),(3,'+++'),(3,'++-'),
             (2,'++++'),(2,'+++-'),(2,'++--'),(2,'+-+-'),
             (2,'+++++'),(2,'++-+-')]
    for q,word in cases:
        direct = direct_counts(q,word)
        formula=transfer_counts(q,word)
        assert direct==formula, (q,word,direct,formula)
        print('checked',q,word,direct)
    assert transfer_counts(2,'++++')[0] == 5152
    assert transfer_counts(2,'+-+-')[0] == 6928
    assert transfer_counts(2,'+++')[0] == 608
    print('VERIFY_OK')


if __name__ == '__main__': test()
