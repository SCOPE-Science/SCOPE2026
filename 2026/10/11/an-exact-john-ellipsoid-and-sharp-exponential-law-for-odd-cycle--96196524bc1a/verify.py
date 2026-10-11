"""Numerical reproducibility checks for the cyclic fractional-stable-set John ellipsoid.

Requires Python 3.9+ standard library only. Tests finite instances; the general
claim and the asymptotic constant follow from the analytic proof.
"""
from math import cos, pi, sqrt


def parameter(n):
    if n < 5 or n % 2 != 1:
        raise ValueError('the documented theorem assumes odd n >= 5')
    r = sqrt(5.0) - 2.0
    def f(q):
        return 1.0 - 4.0 * q - q * q - q**n * (1.0 + 4.0 * q - q*q)
    lo, hi = 0.0, r
    assert f(lo) > 0 and f(hi) < 0
    for _ in range(85):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    q = (lo + hi) / 2
    t = 2.0*q/(1.0+q*q)
    a = t/(1.0+t)
    eta = t*(1.0-t)/(2.0*(1.0+t))
    return q,t,a,eta


def inverse(matrix):
    n = len(matrix)
    a = [list(row) + [float(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col,n),key=lambda i:abs(a[i][col]))
        a[col],a[pivot] = a[pivot],a[col]
        divisor = a[col][col]
        assert abs(divisor)>1e-10
        a[col] = [v/divisor for v in a[col]]
        for i in range(n):
            if i != col:
                fac = a[i][col]
                a[i] = [x-fac*y for x,y in zip(a[i],a[col])]
    return [row[n:] for row in a]


def test_one(n):
    q,t,a,eta = parameter(n)
    adjacency = [[int((j-i)%n in (1,n-1)) for j in range(n)]
                 for i in range(n)]
    base = [[float(i==j)+t*adjacency[i][j]/2.0 for j in range(n)]
            for i in range(n)]
    inverted = inverse(base)
    S = [[eta*inverted[i][j] for j in range(n)] for i in range(n)]
    fn = sum(1.0/(1.0+t*cos(2*pi*j/n)) for j in range(n))/n
    assert abs(fn - 2*t/(1-t*t)) < 2e-12
    for i in range(n):
        j=(i+1)%n
        # Both kinds of facet have equality in their ellipsoidal containment test.
        assert abs(S[i][i]-a*a) < 2e-12
        assert abs(S[i][i]+S[j][j]+2*S[i][j]-(1-2*a)**2)<2e-12
    # The positive John weights yield the exact inverse shape matrix.
    for i in range(n):
        for j in range(n):
            target = (2*a/a**2 +2/(1-2*a))*float(i==j) + adjacency[i][j]/(1-2*a)
            actual = (float(i==j)+t*adjacency[i][j]/2)/eta
            assert abs(target-actual)<2e-12
    assert 2*a>0 and 1-2*a>0
    assert abs(sum([2*a]*n+[(1-2*a)]*n)-n)<1e-12
    # Exact determinant product identity after replacing t by 2q/(1+q^2).
    prod=1.0
    for j in range(n):
        prod *= 1+t*cos(2*pi*j/n)
    expected=(1+q**n)**2/(1+q*q)**n
    assert abs(prod/expected-1)<2e-11
    return q,t


def main():
    outcomes = [test_one(n) for n in range(5,32,2)]
    r=sqrt(5)-2
    limit=8*sqrt(5)/25
    for n in (5,7,9,11):
        _,t=outcomes[(n-5)//2]
        scaled=(1/sqrt(5)-t)/r**n
        assert abs(scaled-limit)<0.006
    # The predicted correction is below the numerical floor for large n.
    print('PASS: 14 odd cycle sizes, 5 through 31; center, 2n facet tangencies,')
    print('John-weight inverse-shape identity, volume product, and asymptotic samples.')
    print('n=5: q,t =',*(round(v,12) for v in outcomes[0]))
    print('asymptotic constant:',limit)


if __name__ == '__main__':
    main()
