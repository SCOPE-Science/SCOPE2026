"""Exact absorbing-chain comparisons and high-precision asymptotic checks.

Run: python verify.py  (Python 3, standard library only).
"""
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext


def gaussian(A, b):
    n = len(b)
    M = [list(A[k]) + [b[k]] for k in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if M[i][k])
        M[k], M[p] = M[p], M[k]
        pivot = M[k][k]
        M[k] = [v / pivot for v in M[k]]
        for i in range(n):
            if i != k:
                a = M[i][k]
                M[i] = [M[i][j] - a * M[k][j] for j in range(n + 1)]
    return [M[k][-1] for k in range(n)]


def green(N, t, y, z, theta, i):
    """Exact expected reward cost at i, with odds y funded, z otherwise."""
    R = [type(y)(1)]
    for k in range(1, N):
        R.append(R[-1] * (y if k <= t else z))
    S = sum(R)
    total = type(y)(0)
    for j in range(1, t + 1):
        u = (Q(j * (N - j), N * N) if isinstance(y, Q)
             else D(j * (N - j)) / D(N * N))
        first = sum(R[:min(i, j)])
        second = sum(R[max(i, j):])
        total += theta * j * first * second * (1 + y) / (S * u * R[j])
    return total


def test_rational():
    checked = 0
    for N in range(4, 9):
        for t in range(2, N - 1):
            for y in [Q(1, 3), Q(1), Q(4)]:
                for z in [Q(2), Q(5)]:
                    A = [[Q(0) for _ in range(N - 1)] for _ in range(N - 1)]
                    rhs = []
                    for i in range(1, N):
                        u = Q(i * (N - i), N * N)
                        p = 1 / (1 + (y if i <= t else z))
                        A[i - 1][i - 1] = u
                        if i > 1:
                            A[i - 1][i - 2] = -u * (1 - p)
                        if i < N - 1:
                            A[i - 1][i] = -u * p
                        rhs.append(Q(i if i <= t else 0))
                    values = gaussian(A, rhs)
                    for i in range(1, N):
                        assert green(N, t, y, z, Q(1), i) == values[i - 1]
                        checked += 1
    return checked


def high_precision():
    checked = 0
    with localcontext() as ctx:
        ctx.prec = 105
        exp = lambda x: x.exp()
        N, t, d, beta = 7, 3, D(1), D(42)
        B = D((N - 1 - t)) * d
        # Both competing barriers, and their exactly equal point.
        for theta in [D('1.5'), D('2'), D('2.5')]:
            h = theta - d
            A = D(t) * h
            y, z = exp(-beta * h), exp(beta * d)
            lead = theta * D(N*N) / D(N-t)
            lead *= exp(beta * min(A, B)) * (D('0.5') if A == B else D(1))
            for i in range(1, N):
                ratio = green(N, t, y, z, theta, i) / lead
                assert abs(ratio - 1) < D('0.000001'), (theta, i, ratio)
                checked += 1
        # At and below the incentive's direction-reversal boundary.
        for theta in [D('0.5'), d]:
            y, z = exp(beta * (d-theta)), exp(beta * d)
            for i in range(1, N):
                if theta < d:
                    lim = theta * D(N*N) * sum(
                        D(1) / D(N-j) for j in range(1, min(i,t)+1))
                else:
                    lim = D(2)*d*D(N*N)*sum(
                        D(min(i,j))/D(N-j) for j in range(1,t+1))
                ratio = green(N,t,y,z,theta,i)/lim
                assert abs(ratio-1)<D('0.000001'),(theta,i,ratio)
                checked += 1
        # Width 1/beta logistic competition between extinction routes.
        theta_c = d * D(N-1) / D(t)
        for s in [D(-3), D(0), D(3)]:
            theta = theta_c + s/(beta*D(t))
            y,z = exp(-beta*(theta-d)),exp(beta*d)
            logistic = 1/(1+exp(-s))
            lead = theta*D(N*N)/D(N-t)*exp(beta*B)
            for i in range(1,N):
                ratio = green(N,t,y,z,theta,i)/lead
                assert abs(ratio-logistic)<D('0.000001'),(s,i,ratio)
                checked += 1
        # A full-invest control has no exponentially persistent interface.
        theta = D('1.5')
        y = exp(-beta*(theta-d))
        for i in range(1,N):
            value=green(N,N-1,y,y,theta,i)
            lim=theta*D(N*N)*sum(D(1)/D(N-j) for j in range(i,N))
            assert abs(value/lim-1)<D('0.000001'),(i,value/lim)
            checked+=1
    return checked

if __name__ == '__main__':
    exact=test_rational()
    asymptotic=high_precision()
    print(f'PASS: {exact} independent exact Markov/Green identities; '
          f'{asymptotic} high-precision limit and crossover comparisons.')
