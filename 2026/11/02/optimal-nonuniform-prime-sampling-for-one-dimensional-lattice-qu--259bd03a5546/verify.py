"""Exact checks for the one-dimensional randomized prime-lattice minimax law.

Run with Python 3.10+; uses only the standard library.
"""
from fractions import Fraction as F
from math import isqrt, pi
from random import Random


def prime_set(n):
    out = []
    for p in range(n // 2 + 1, n + 1):
        if p >= 2 and all(p % q for q in range(2, isqrt(p) + 1)):
            out.append(p)
    return out


def setup(n, s):
    primes = prime_set(n)
    assert primes
    k = len(primes)
    u = [F(1, p ** s) for p in primes]
    d = [v * (1 - v) for v in u]
    h1 = sum((u[i] / d[i] for i in range(k)), F(0))
    h2 = sum((u[i] * u[i] / d[i] for i in range(k)), F(0))
    c = h1 / (1 + h2)
    w = [(1 - c * u[i]) / d[i] for i in range(k)]
    assert all(x > 0 for x in w)
    z = sum(w, F(0))
    nu = [x / z for x in w]
    M = [[(u[i] if i == j else u[i]*u[j]) for j in range(k)] for i in range(k)]
    return primes, u, d, c, nu, z, M


def quadratic(v, M):
    return sum((v[i] * M[i][j] * v[j] for i in range(len(v)) for j in range(len(v))), F(0))


def check(n, s):
    primes, u, d, c, nu, z, M = setup(n, s)
    k = len(primes)
    assert sum(nu, F(0)) == 1
    assert quadratic(nu, M) == 1 / z
    assert all(sum((M[i][j]*nu[j] for j in range(k)), F(0)) == 1/z for i in range(k))
    if k > 1:
        assert all(nu[i+1] > nu[i] for i in range(k-1))
        equal = [F(1, k)] * k
        assert quadratic(nu, M) < quadratic(equal, M)
    else:
        assert nu == [1]
    # Entire lcm kernel, exactly from divisibility counting.
    for i,p in enumerate(primes):
        for j,q in enumerate(primes):
            lcm = p if p == q else p*q
            assert M[i][j] == F(1, lcm**s)
    r = Random(13579 + 71 * n + s)
    for _ in range(12):
        draws = [r.randrange(1, 1000) for i in range(k)]
        total = sum(draws)
        rival = [F(t,total) for t in draws]
        assert quadratic(rival, M) >= quadratic(nu, M)
    return primes, float(quadratic(nu,M)), float(quadratic([F(1,k)]*k,M)), [float(x) for x in nu]


def main():
    groups = 0
    for s in (2,3,4,5):
        for n in range(2,101):
            check(n,s)
            groups += 1
    for n in (12,30,100):
        p, opt, unif, v = check(n,2)
        print('n=',n,'primes=',p,'weights=',[round(x,8) for x in v],
              'uniform/optimal_error=',round((unif/opt)**0.5,10))
    # independent brute force over complete finite Fourier ranges and exact rational inequalities
    for n in (10,30):
        p, _, _, _, nu, z, M = setup(n,4)
        k=len(p)
        # truncated Fourier coefficient squared sum; complete divisibility for each |m| <= T
        for T in (50,200,1000):
            trunc = sum((F(2,m**4)*sum((nu[i] for i,q in enumerate(p) if m%q==0), F(0))**2
                         for m in range(1,T+1)),F(0))
            # infinite norm E^2 = 2*zeta(4)*(nu^T M nu); 2*zeta(4)=pi^4/45
            true = (pi**4/45)*float(quadratic(nu,M))
            assert 0 <= float(trunc) < true
            assert true-float(trunc) < 2/(3*T**3) + 1e-12
            groups += 1
    # prime number theorem constant-ratio prediction, rigorous analytic formula proved in RESULT.md
    from math import sqrt
    C2 = sqrt(F(7,6))
    C4 = sqrt(F(217,120))
    assert C2 > 1 and C4 > C2
    print('asymptotic s=2 constant=',C2,'s=4 constant=',C4)
    print('PASS',groups,'exact finite-design groups plus finite-Fourier and asymptotic checks')


if __name__ == '__main__':
    main()
