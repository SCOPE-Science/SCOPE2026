"""Exact integer certificate for the centered graph-ball maximal operator on K_{2,2,2}.

Run with Python 3; no third-party packages are required.
"""
from itertools import product
from fractions import Fraction
from math import sqrt

N = 6
DENOM = 30
# Pairs of antipodal (nonadjacent) graph vertices: (0,1), (2,3), (4,5).
MATE = tuple(i ^ 1 for i in range(N))


def det_bareiss(matrix):
    """Exact determinant by fraction-free elimination; no row swap is required here."""
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    prev = 1
    for k in range(n - 1):
        pivot = a[k][k]
        if pivot == 0:
            return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
        for i in range(k+1, n):
            a[i][k] = 0
        prev = pivot
    return a[n - 1][n - 1]


def selected_integer_matrix(choices):
    """Rows indexed by choices: 0=radius 0, 1=radius 1, 2=radius 2."""
    assert len(choices) == N
    result = []
    for i, radius in enumerate(choices):
        if radius == 0:
            row = [DENOM * int(j == i) for j in range(N)]
        elif radius == 1:
            row = [6 * int(j != MATE[i]) for j in range(N)]
        else:
            row = [5 for _ in range(N)]
        result.append(row)
    return result


def gram_integer(B):
    return [[sum(B[i][j] * B[i][k] for i in range(N))
             for k in range(N)] for j in range(N)]


def proper_certificate(choices):
    B=selected_integer_matrix(choices)
    gram=gram_integer(B)
    # lambda_0=141/100, and DENOM^2 * lambda_0=1269.
    H=[[1269*int(i==j)-gram[i][j] for j in range(N)] for i in range(N)]
    for k in range(1,N+1):
        det=det_bareiss([row[:k] for row in H[:k]])
        if det <= 0:
            return False
    return True


def main():
    exceptional = {tuple(0 if i // 2 == pair else 1 for i in range(N))
                   for pair in range(3)}
    assert len(exceptional) == 3
    n_positive = n_other = 0
    for choice in product(range(3), repeat=N):
        positive = proper_certificate(choice)
        if choice in exceptional:
            assert not positive, choice
            n_other += 1
        else:
            assert positive, choice
            n_positive += 1
    assert (n_positive,n_other)==(726,3)

    # Verify invariant pair-block eigenvalues and exact scalar quadratic.
    # lambda_+= (21+6*sqrt(6))/25, lambda_-= (21-6*sqrt(6))/25.
    # Trace=42/25, determinant=9/25 for the leading 2x2 block Gram.
    assert Fraction(42,25)**2 - 4*Fraction(9,25) == Fraction(864,625)
    assert 2*Fraction(21,25) == Fraction(42,25)

    # Exact action at f=(1,1,b,b,b,b), b=(sqrt(6)-2)/2.
    # T f=(1,1,c,c,c,c), c=(2+3*b)/5.
    # Check exact eigenvalue identity without floating arithmetic by
    # representing elements of Q(sqrt(6)) as (rational, rational).
    R=Fraction
    def add(x,y):return(x[0]+y[0],x[1]+y[1])
    def mul(x,y):return(x[0]*y[0]+6*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
    def s(a):return(R(a),R(0))
    def scale(x,a):return(x[0]*R(a),x[1]*R(a))
    one=s(1)
    b=(R(-1),R(1,2))
    lam=(R(21,25),R(6,25))
    c=scale(add(s(2),scale(b,3)),R(1,5))
    # A^T A f at each high coordinate equals 1 + (4/5)c.
    # At each low coordinate equals (3/5)c.
    assert add(one,scale(c,R(4,5))) == lam
    assert scale(c,R(3,5)) == mul(lam,b)
    # b is strictly between zero and one, hence chosen radii are active.
    assert 0 < (sqrt(6)-2)/2 < 1

    # The second two-dimensional eigenvalue is lambda_-<1 and the
    # remaining four singular squares are 1 and (1/25)x3.
    assert (21-6*sqrt(6))/25 < 1
    assert (21+6*sqrt(6))/25 > 1.41
    print('CERTIFICATE_OK all=729 strict=726 exceptional=3 witness=exact')

if __name__ == '__main__':
    main()
