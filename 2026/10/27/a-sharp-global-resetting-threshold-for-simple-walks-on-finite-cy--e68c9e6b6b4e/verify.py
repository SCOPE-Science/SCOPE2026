"""Exact finite checks for the cyclic-walk resetting threshold theorem.

Run with Python 3: python verify.py. The mathematical result for unrestricted sizes
rests on the analytical positivity argument, not these finite tests.
"""
from fractions import Fraction


def coefficients(j, parity):
    values = [Fraction(1)]
    for k in range(1, j + 1):
        top = j * (j + parity) - (k - 1) * (k - 1 + parity)
        values.append(values[-1] * Fraction(top, k * (2*k-1)))
    return values


def at(values, index):
    return values[index] if 0 <= index < len(values) else Fraction(0)


def data(m, d):
    parity, a = m % 2, m // 2
    b = a - d
    upper = coefficients(a, parity)
    lower = coefficients(b, parity)
    mu = d * (m - d)
    N = [at(upper, j) - at(lower, j) + at(upper, j-1)
         - (1+mu)*at(lower, j-1) for j in range(a+2)]
    return mu, upper, lower, N


def evalpoly(poly, x):
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value*x + coefficient
    return value


def formula_hitting(m, d, r):
    mu, upper, lower, _ = data(m, d)
    if r == 0:
        return Fraction(mu)
    w = r/(1-r)
    return (1+w)*(evalpoly(upper,w)-evalpoly(lower,w))/(w*evalpoly(lower,w))


def direct_hitting(m, d, r):
    # E[target] = 0. For i != target: E[i] = 1 + r E[0]
    # +(1-r)*(E[i-1]+E[i+1])/2. Solve over exact rationals.
    states = [i for i in range(m) if i != d]
    index = {s:j for j,s in enumerate(states)}
    n = len(states)
    mat = [[Fraction(int(i==j)) for j in range(n)] + [Fraction(1)]
           for i in range(n)]
    for i, state in enumerate(states):
        mat[i][index[0]] -= r
        for neighbor in ((state-1)%m,(state+1)%m):
            if neighbor in index:
                mat[i][index[neighbor]] -= (1-r)/2
    for k in range(n):
        pivot = next(j for j in range(k,n) if mat[j][k])
        mat[k], mat[pivot] = mat[pivot], mat[k]
        factor = mat[k][k]
        mat[k] = [x/factor for x in mat[k]]
        for i in range(n):
            if i != k and mat[i][k]:
                factor = mat[i][k]
                mat[i] = [u-factor*v for u,v in zip(mat[i],mat[k])]
    return mat[index[0]][-1]


def main():
    checks = 0
    for m in range(3, 101):
        for d in range(1,m//2+1):
            mu, upper, lower, N = data(m,d)
            assert N[0] == N[1] == 0
            assert N[2] == Fraction(mu*(5*mu+5-m*m),6)
            checks += 2
            if N[2] >= 0:
                assert all(v >= 0 for v in N[2:])
                assert any(v > 0 for v in N[2:])
                checks += 2
            for r in (Fraction(1,3), Fraction(2,3)):
                w = r/(1-r)
                gap = formula_hitting(m,d,r) - mu
                assert gap == evalpoly(N,w)/(w*evalpoly(lower,w))
                if N[2] >= 0:
                    assert gap > 0
                checks += 2 if N[2] >= 0 else 1
    for m in range(3, 12):
        for d in range(1,m//2+1):
            for r in (Fraction(0), Fraction(1,5), Fraction(1,2), Fraction(3,4)):
                assert direct_hitting(m,d,r) == formula_hitting(m,d,r)
                checks += 1
    print('VERIFY_OK', checks, 'exact assertions; direct Markov equations and threshold signs')


if __name__ == '__main__':
    main()
