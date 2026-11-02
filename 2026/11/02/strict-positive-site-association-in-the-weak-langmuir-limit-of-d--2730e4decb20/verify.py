"""Independent finite-state and combinatorial checks for a weak-Langmuir exclusion theorem.

Requires Python 3.10+ and NumPy. This script is corroboration, not the infinite-parameter proof.
"""
import itertools
import math
import numpy as np


def symmetric_means(weights):
    n = len(weights)
    e = [1.0] + [0.0] * n
    for w in weights:
        for j in range(n, 0, -1):
            e[j] += w * e[j - 1]
    return [e[k] / math.comb(n, k) for k in range(n + 1)], e


def weak_law(weights, prob):
    n = len(weights)
    _, e = symmetric_means(weights)
    states = range(1 << n)
    return np.array([math.comb(n, s.bit_count()) * prob ** s.bit_count()
        * (1 - prob) ** (n - s.bit_count())
        * math.prod(weights[i] for i in range(n) if s >> i & 1) / e[s.bit_count()]
        for s in states], dtype=float)


def covariances(mu, n):
    bits = np.array([[(s >> i) & 1 for i in range(n)] for s in range(1 << n)], dtype=float)
    m = bits.T @ mu
    return (bits.T * mu) @ bits - np.outer(m, m)


def test_combinatorial():
    rng = np.random.default_rng(872134)
    count = 0
    for n in range(2, 8):
        for trial in range(40):
            weights = np.exp(rng.uniform(-1.5, 1.5, size=n))
            prob = rng.uniform(0.1, 0.9)
            mu = weak_law(weights, prob)
            assert abs(mu.sum() - 1) < 1e-12
            means, e = symmetric_means(weights)
            assert all(means[k + 1] ** 2 > means[k] * means[k + 2] + 1e-14 for k in range(n - 1))
            for s in range(1 << n):
                for i in range(n):
                    for j in range(i + 1, n):
                        if ((s >> i) & 1) or ((s >> j) & 1):
                            continue
                        a, b, c, d = mu[s], mu[s | 1 << i], mu[s | 1 << j], mu[s | 1 << i | 1 << j]
                        assert a * d >= b * c - 1e-14
            C = covariances(mu, n)
            assert all(C[i, j] > 1e-14 for i in range(n) for j in range(i + 1, n))
            # Every nontrivial canonical sector is strictly negatively pair-correlated.
            for k in range(1, n):
                conditional = np.zeros(1 << n)
                for s in range(1 << n):
                    if s.bit_count() == k:
                        conditional[s] = math.prod(weights[i] for i in range(n) if s >> i & 1) / e[k]
                Q = covariances(conditional, n)
                assert all(Q[i, j] < -1e-14 for i in range(n) for j in range(i + 1, n))
            count += 1
    # Exact two-site identity; the right side is q^2 (1-q)^2 ((u-v)/(u+v))^2.
    for u,v,q in [(1,2,.5), (3,7,.27),(5,1,.72)]:
        c = covariances(weak_law([u,v],q),2)[0,1]
        exact = q*q*(1-q)**2*((u-v)/(u+v))**2
        assert abs(c-exact) < 1e-14
    return count


def generator(epsilon, nx=2, ny=3):
    n=nx*ny; m=1<<n
    a,b=2.0,3.0
    px,qx=3.0,1.0
    py,qy=[2.2,1.5],[0.8,0.65]
    G=np.zeros((m,m))
    def site(x,y): return x*ny+y
    for s in range(m):
        def add(t,rate):
            if rate:
                G[t,s]+=rate
                G[s,s]-=rate
        for x in range(nx):
            for y in range(ny):
                i=site(x,y); occ=(s>>i)&1
                add(s^(1<<i), epsilon * (b if occ else a))
                if not occ: continue
                for xx,yy,rate in [(x+1,y,px),(x-1,y,qx),
                                   (x,(y+1)%ny,py[x]),(x,(y-1)%ny,qy[x])]:
                    if xx<0 or xx>=nx: continue
                    j=site(xx,yy)
                    if not ((s>>j)&1):
                        add(s^(1<<i)^(1<<j),rate)
    assert np.max(abs(G.sum(axis=0))) < 1e-12
    return G


def steady(G):
    B=G.copy(); rhs=np.zeros(len(G)); B[-1,:]=1; rhs[-1]=1
    mu=np.linalg.solve(B,rhs)
    assert min(mu)>-1e-12
    assert np.max(np.abs(G @ mu))<1e-11
    return mu


def test_2d():
    n=6; weights=[3.0**x for x in range(2) for _ in range(3)]
    law=weak_law(weights, .4)
    # The closed-x / periodic-y hopping generator has the claimed sector stationary weights.
    assert np.max(np.abs(generator(0) @ law)) < 1e-12
    C=covariances(law,n)
    min_cov=min(C[i,j] for i in range(n) for j in range(i+1,n))
    assert min_cov > 0
    errors=[]
    for eps in (0.1,0.01,0.001,0.0001):
        G=generator(eps)
        mu=steady(G)
        # Number marginal is exactly Bin(6,0.4) for EVERY positive epsilon.
        for k in range(n+1):
            assert abs(sum(mu[s] for s in range(1<<n) if s.bit_count()==k)
                       - math.comb(n,k)*.4**k*.6**(n-k)) < 1e-11
        errors.append(float(np.max(np.abs(mu-law))))
    assert errors[-1] < errors[-2] < errors[-3] < errors[-4]
    assert errors[-1] < 0.00002
    Csmall=covariances(steady(generator(0.0001)),n)
    assert all(Csmall[i,j] > 0 for i in range(n) for j in range(i+1,n))
    return min_cov,errors


if __name__ == '__main__':
    count=test_combinatorial()
    min_cov, errors=test_2d()
    print(f'PASS: {count} independent weighted-subset cases, all local lattice squares and pair signs')
    print('PASS: strict fixed-size pair anticorrelation, two-site identity and exact binomial N-marginals')
    print(f'PASS: six-site driven two-dimensional hopping; minimum positive covariance {min_cov:.9g}')
    print(f'PASS: finite-rate stationary convergence at four rates; max errors {errors}')
