"""Exact-arithmetic checks for residual-power Kaczmarz finite-state laws.
Scientific reproducibility only; all substantive general conclusions are proven algebraically.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def check(values, power, eps):
    n = len(values)
    b = list(map(F, values))
    e = F(eps)
    assert e >= 0 and len(set(b)) >= 2 and power > 0 and power % 2 == 0
    W = [[e + (b[i] - b[j]) ** power for j in range(n)] for i in range(n)]
    d = [sum(row) for row in W]
    assert all(t > 0 for t in d)
    total = sum(d)
    pi = [t / total for t in d]
    P = [[W[i][j] / d[i] for j in range(n)] for i in range(n)]
    assert all(sum(row) == 1 for row in P)
    assert all(pi[i]*P[i][j] == pi[j]*P[j][i] for i in range(n) for j in range(n))
    assert all(sum(pi[i]*P[i][j] for i in range(n)) == pi[j] for j in range(n))
    r=power//2
    C = [[(e if a == c == 0 else F(0)) +
          (F((-1)**a * comb(power,a)) if a+c == power else F(0))
          for c in range(power+1)] for a in range(power+1)]
    V = [[b[i] ** k for k in range(power+1)] for i in range(n)]
    assert all(sum(V[i][a]*C[a][c]*V[j][c] for a in range(power+1) for c in range(power+1)) == W[i][j]
               for i in range(n) for j in range(n))
    if power == 2:
        avg = sum(b)/n
        centered = [x-avg for x in b]
        mu2 = sum(x*x for x in centered)/n
        mu3 = sum(x**3 for x in centered)/n
        mu4 = sum(x**4 for x in centered)/n
        stationary_mean = sum(pi[i]*b[i] for i in range(n))
        mse = sum(pi[i]*centered[i]**2 for i in range(n))
        assert stationary_mean == avg + mu3/(e+2*mu2)
        assert mse == mu2 + (mu4-mu2**2)/(e+2*mu2)
        assert mse >= mu2
    return 1


def main():
    count=0
    for n in range(2,8):
        for vals in product((-2,-1,0,1,3),repeat=n):
            if len(set(vals)) < 2: continue
            # Limit count by a deterministic prefix, maintaining exact reproducibility.
            if count >= 12000: break
            for power in (2,4,6):
                for eps in (F(0),F(1,7),F(2)):
                    check(vals,power,eps)
                    count+=1
        if count >= 12000:break
    for n in range(2,20):
        for eps in (F(0),F(1,7),F(2)):
            b=[F(0)]*(n-1)+[F(1)]
            d0=n*eps+1
            d1=(n-1)*(eps+1)+eps
            total=(n-1)*d0+d1
            pi1=d1/total
            assert pi1 == (n*eps+n-1)/(n*n*eps+2*(n-1))
            if eps == 0: assert pi1 == F(1,2)
            m=F(1,n)
            variance=F(n-1,n*n)
            mu3=F((n-1)*(n-2),n**3)
            assert pi1-m == mu3/(eps+2*variance)
    print(f'PASS: {count} exact transition/polynomial/stationary-law cases; '
          '54 exact two-level outlier checks. General statements use the proof, not enumeration.')

if __name__ == '__main__':main()
