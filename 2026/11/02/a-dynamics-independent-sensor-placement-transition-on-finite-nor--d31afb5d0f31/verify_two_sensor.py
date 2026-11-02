"""Supplementary finite checks for a paired-sensor normalized-path sampling theorem.

Run with Python 3.10+ and the standard library; infinite assertions are proved
analytically in the accompanying mathematical result, not by this checker.
"""
from math import cos, pi, sqrt, exp, log, isfinite


def eigvec(N, j, vertex):
    L = N - 1
    deg = 1 if vertex in (0, L) else 2
    factor = sqrt(deg / (2 * L)) if j in (0, L) else sqrt(deg / L)
    return factor * cos(pi * j * vertex / L)


def matdet(matrix):
    a = [list(map(float, row)) for row in matrix]
    n = len(a)
    det = 1.0
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[p][k]) < 1e-12:
            return 0.0
        if p != k:
            a[k], a[p] = a[p], a[k]
            det = -det
        pivot = a[k][k]
        det *= pivot
        for i in range(k+1, n):
            c = a[i][k] / pivot
            for h in range(k+1, n):
                a[i][h] -= c * a[k][h]
            a[i][k] = 0
    return det


def gram(N, m, positions, K):
    # An injective spectral evolution on this finite path can interpolate
    # phi(lambda_j) = 0.85 - 1.7*j/(N-1) at each distinct eigenvalue.
    matrix = [
        [eigvec(N, j, v) * ((0.85 - 1.7*j/(N-1)) ** t) for j in range(m)]
        for v in positions for t in range(K)
    ]
    return [[sum(row[i] * row[j] for row in matrix) for j in range(m)]
            for i in range(m)]


def log_ratio(N, m):
    L = N - 1
    if L % 2 == 0 and m > L // 2:
        return float('-inf')
    return m * log(2) + sum(2 * log(abs(cos(pi * j / L)))
                            for j in range(1, m))


def simpson(f, end, steps=8000):
    h = end / steps
    return h / 3 * (f(0) + f(end)
                    + 4*sum(f(h*i) for i in range(1, steps, 2))
                    + 2*sum(f(h*i) for i in range(2, steps, 2)))


def F(a):
    return simpson(lambda t: log(2*cos(pi*t)**2), a)


def run():
    count = 0
    # Full orthonormal spectral basis for normalized path adjacency.
    for N in range(5, 19):
        L = N - 1
        for j in range(N):
            v = [eigvec(N, j, i) for i in range(N)]
            mu = cos(pi*j/L)
            for i in range(N):
                value = sum(v[h]/sqrt((1 if i in (0,L) else 2) *
                                      (1 if h in (0,L) else 2))
                            for h in (i-1, i+1) if 0 <= h < N)
                assert abs(value - mu*v[i]) < 2e-12, (N,j,i)
                count += 1
            for k in range(j+1):
                dot = sum(eigvec(N,j,i)*eigvec(N,k,i) for i in range(N))
                assert abs(dot - (1 if k==j else 0)) < 2e-12
                count += 1
    # Entrywise transfer and Gram congruence; several time horizons and m.
    for N in range(5, 19):
        for m in range(2, N+1):
            d = [sqrt(2)*cos(pi*j/(N-1)) for j in range(m)]
            for j in range(m):
                for left, inward in ((0,1),(N-1,N-2)):
                    assert abs(eigvec(N,j,inward)-d[j]*eigvec(N,j,left)) < 2e-12
                    count += 1
            if m <= 6:
                for K in (int((m+1)//2),m):
                    G0 = gram(N,m,(0,N-1),K)
                    G1 = gram(N,m,(1,N-2),K)
                    for i in range(m):
                        for j in range(m):
                            assert abs(G1[i][j]-d[i]*d[j]*G0[i][j]) <= (1e-10 * max(1,abs(G1[i][j]))), (N,m,K,i,j,G1[i][j],d[i]*d[j]*G0[i][j])
                            count += 1
                    # Restrict determinant checks to stably conditioned small systems.
                    if m <= 4 and N <= 10:
                        det0=matdet(G0)
                        det1=matdet(G1)
                        if det0 > 1e-8:
                            expected=exp(log_ratio(N,m)) if isfinite(log_ratio(N,m)) else 0
                            assert abs(det1/det0 - expected) < 3e-5, (N,m,K,det1/det0,expected)
                            count += 1
    # Exact one-step ratio recurrence and a single strict-win interval.
    for N in range(5, 501):
        prev = log(2)
        changed=False
        for m in range(2,N+1):
            s=log_ratio(N,m)
            assert (not isfinite(s) or abs(s-(prev+log(2)+2*log(abs(cos(pi*(m-1)/(N-1))))))<1e-9) if isfinite(prev) else True
            if s < 1e-10:
                changed=True
            elif changed:
                raise AssertionError(('multiple strict-win intervals',N,m,s))
            prev=s
            count+=1
    assert abs(log_ratio(9,4)) < 1e-12  # An actual finite-size tie.
    # The universal continuous crossover and first Euler-Maclaurin correction.
    a,b=0.25,0.499
    assert F(a)>0 and F(b)<0
    for _ in range(43):
        mid=(a+b)/2
        if F(mid)>0: a=mid
        else: b=mid
    alpha=(a+b)/2
    assert abs(alpha - 0.4095810867492214)<2e-9
    f=lambda t:log(2*cos(pi*t)**2)
    delta=log(cos(pi*alpha))/f(alpha)
    assert abs(delta - 0.6872393090643195)<2e-8
    for N in (501,1001,2001,5001):
        L=N-1
        m=round(alpha*L)
        expected=f(alpha)*(m-alpha*L-delta)
        actual=log_ratio(N,m)
        assert abs(actual-expected) < 4/L, (N,actual,expected)
        count+=1
    return count,alpha,delta


if __name__=='__main__':
    count,alpha,delta=run()
    print('TWO_SENSOR_CHECK_OK',count, 'alpha', f'{alpha:.12f}', 'delta', f'{delta:.12f}')
