"""Standalone finite checks for exact sink-allocation spectral identities.

Requires Python 3 and NumPy. Run: python check.py
"""
import math
from fractions import Fraction
import numpy as np


def eig_formula(n, m, s):
    u, v = n - s, n - 2 * m + s
    assert u >= 0 and v >= 0 and (u + v) >= 1
    return n - math.sqrt(u * v)


def eig_direct(n, m, s):
    u, v = n - s, n - 2 * m + s
    L = np.eye(u + v) * n
    L[:u, u:] = -1
    L[u:, :u] = -1
    return np.linalg.eigvalsh(L)[0]


def pmf(n, m, j):
    q = n - m
    if abs(j) > min(m, q):
        return Fraction(0)
    return Fraction(math.comb(n, m + j) * math.comb(n, m - j),
                    math.comb(2 * n, 2 * m))


def probability_survival(n, m, c):
    # The strict ecological persistence inequality is eigenvalue < m+c.
    q = n - m
    def lc(x):
        return math.lgamma(n + 1) - math.lgamma(x + 1) - math.lgamma(n - x + 1)
    denom = math.lgamma(2 * n + 1) - math.lgamma(2 * m + 1) - math.lgamma(2 * n - 2 * m + 1)
    return sum(math.exp(lc(m + j) + lc(m - j) - denom)
               for j in range(-min(m, q), min(m, q) + 1)
               if eig_formula(n, m, m + j) < m + c)


def main():
    cases = 0
    distributions = 0
    for n in range(2, 17):
        for m in range(1, n):
            js = range(-min(m, n-m), min(m, n-m)+1)
            probs = [pmf(n, m, j) for j in js]
            assert sum(probs) == 1
            assert sum(Fraction(j) * p for j, p in zip(js, probs)) == 0
            assert sum(Fraction(j*j) * p for j, p in zip(js, probs)) == Fraction(m*(n-m), 2*n-1)
            distributions += 1
            vals = []
            for j in js:
                s = m + j
                val = eig_formula(n,m,s)
                eig = eig_direct(n,m,s)
                assert abs(val - eig) < 3e-11, (n,m,s,val,eig)
                vals.append(val)
                cases += 1
            assert abs(min(vals)-m)<1e-10
            extreme = n-math.sqrt((n-m)**2-min(m,n-m)**2)
            assert abs(max(vals)-extreme)<3e-11
    print(f"PASS: {cases} direct eigensystem comparisons and {distributions} exact hypergeometric distributions")
    rho, c = 0.4, 0.2
    target = math.erf(math.sqrt(2*c/rho))  # 2*Phi(2*sqrt(c/rho))-1
    print(f"Predicted critical-window survival probability: {target:.9f}")
    for n in (100,400,1600):
        m=int(round(rho*n))
        estimate=probability_survival(n,m,c)
        print(f"  n={n:4d}, m={m:4d}: exact finite probability {estimate:.9f}")
    print("The asymptotic theorem is proved analytically, not by these finite computations.")

if __name__ == '__main__':
    main()
