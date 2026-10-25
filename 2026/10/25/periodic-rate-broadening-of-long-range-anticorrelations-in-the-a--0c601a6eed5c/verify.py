#!/usr/bin/env python3
"""Reproduce finite-site stationary second-moment and periodic-boundary-layer checks."""
from fractions import Fraction
from math import comb, erfc, sqrt


def collision_kernel(rates):
    # rates is a 1-indexed array: rates[0] ignored.
    n = len(rates) - 1
    U = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(1, n + 1):
        U[j][j] = Fraction(1)
    # Compute by increasing j, then increasing i, preserving U[i-1][j].
    for j in range(1, n + 1):
        for i in range(1, j):
            U[i][j] = (rates[i] * U[i-1][j] + rates[j] * U[i][j-1]) / (rates[i] + rates[j])
    return U


def rational_tests():
    count = 0
    for rates_tuple in ((1, 1, 1, 1), (1, 3, 2, 5, 1, 4), (2, 1, 4, 2, 6, 3, 5), (1, 2, 3, 4, 5, 6, 7, 8)):
        rates = [Fraction(0)] + [Fraction(t) for t in rates_tuple]
        n = len(rates) - 1
        U = collision_kernel(rates)
        lam = Fraction(7, 5)
        means = [Fraction(0)] + [lam / rates[k] for k in range(1, n+1)]
        moments = [[Fraction(0) for _ in range(n + 1)] for _ in range(n+1)]
        for j in range(2,n+1):
            for i in range(1,j):
                # Evaluate the moments from the collision representation, then
                # separately test the exact generator balance equation.
                moments[i][j] = means[i] * means[j] * (1 - U[i][j])
                lhs = (rates[i]+rates[j])*moments[i][j]
                rhs = lam*means[j] if i == 1 else rates[i-1]*moments[i-1][j]
                if j > i + 1:
                    rhs += rates[j-1]*moments[i][j-1]
                assert lhs == rhs, (i,j,lhs,rhs)
                assert -means[i]*means[j] < -means[i]*means[j]*U[i][j] < 0
                count += 1
    # Independent exact homogeneous collision probability via ballot path census:
    # to close gap d, j must step d+w times and i must step w times, w<i.
    for i in range(1, 15):
        for d in range(1, 12):
            n = i+d
            U = collision_kernel([Fraction(0)]+[Fraction(1)]*n)
            ballot = sum(Fraction(d*comb(d+2*w,w), (d+2*w)*2**(d+2*w)) for w in range(i))
            assert U[i][n] == ballot, (i,d,U[i][n],ballot)
            count += 1
    return count


def periodic_kernel(period, n, ds):
    # Float dynamic programming, testing a distinct numerical regime to the
    # rational exhaustive finite-state identities above.
    mu = [0.0] + [float(period[(k-1) % len(period)]) for k in range(1,n+max(ds)+1)]
    prev = [0.0]*(len(mu)); current = [0.0]*(len(mu)); answer = {}
    targets = set(n+d for d in ds)
    for j in range(1,len(mu)):
        for i in range(1,j):
            current[i] = (mu[i]*current[i-1] + mu[j]*prev[i])/(mu[i]+mu[j])
        current[j]=1.0
        if j in targets:
            answer[j-n]=current[n]
        prev,current=current,prev
    return answer


def periodic_tests():
    checks=0
    n=900
    ds=[int(round(s*sqrt(n))) for s in (0.5,1.0,2.0,3.0)]
    for period in ((1,), (1,3), (1,2,4)):
        m=sum(1/t for t in period)/len(period)
        v=sum(1/(t*t) for t in period)/len(period)
        vals=periodic_kernel(period,n,ds)
        for d in ds:
            pred=erfc(m*d/(2*sqrt(v*n)))
            assert abs(vals[d]-pred)<0.023, (period,d,vals[d],pred)
            checks+=1
        print('period=',period,'inverse-rate means=',round(m,6),'mean-square=',round(v,6),
              'comparison=',[(d,round(vals[d],6),round(erfc(m*d/(2*sqrt(v*n))),6)) for d in ds])
    return checks


if __name__ == '__main__':
    c=rational_tests()
    t=periodic_tests()
    print(f'PASS {c} exact rational stationary and ballot checks; {t} periodic boundary-layer comparisons')
