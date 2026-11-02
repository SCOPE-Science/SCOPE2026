"""Standalone finite-matrix checks for radial-wheel negative-type thresholds.

Usage: python verify.py
Requires NumPy. These finite checks supplement, not replace, the proof.
"""
import math
import numpy as np


def constants(n):
    assert isinstance(n, int) and n >= 4
    c = 1.0 if n % 2 == 0 else math.cos(math.pi / n)
    a = 2*c/(2*c - 1)
    b = ((n - 3)*a + 2)/(2*n)
    maximum = math.log2(a/b)
    critical_length = b ** (1 / maximum)
    return a, b, critical_length, maximum


def g(n, length, p):
    return (n - 3)*(2*length)**p + 2 - 2*n*length**p


def global_root(n, length):
    lo, hi = 0.0, 2.0
    while g(n, length, hi) < 0:
        hi *= 2
    for _ in range(85):
        md = (lo + hi)/2
        if g(n, length, md) > 0:
            hi = md
        else:
            lo = md
    return (hi + lo)/2


def predicted(n, length):
    a, b, ell, maximum = constants(n)
    pg = global_root(n, length)
    ps = math.log(a)/math.log(2*length) if length > 0.5 else math.inf
    return min(pg, ps), ell


def graph_metric(n, length):
    size = n + 1
    d = np.full((size, size), math.inf)
    np.fill_diagonal(d, 0)
    for i in range(n):
        j = (i + 1) % n
        d[i,j] = d[j,i] = 1
        d[i,n] = d[n,i] = length
    for k in range(size):
        d = np.minimum(d, d[:,[k]] + d[[k],:])
    return d


def max_zero_sum_eigenvalue(d, p):
    n = len(d)
    powered = d**p
    # Orthonormal basis for the zero-sum subspace.
    V = np.zeros((n, n-1))
    for j in range(1,n):
        V[:j,j-1] = 1/math.sqrt(j*(j+1))
        V[j,j-1] = -j/math.sqrt(j*(j+1))
    return np.linalg.eigvalsh(V.T @ powered @ V)


def main():
    rng = np.random.default_rng(1729)
    checks = 0
    for n in range(4, 17):
        a, b, ell, max_p = constants(n)
        assert 0.5 < ell < 1 and max_p > 1
        checks += 2
        assert abs(g(n, ell, max_p)) < 1e-10
        assert abs((2*ell)**max_p - a) < 1e-10
        checks += 2
        for length in (0.5, 0.55, 0.75, 0.93, ell, 1.0):
            p, _ = predicted(n, length)
            d = graph_metric(n, length)
            for i in range(n):
                for j in range(n):
                    expected = 0 if i == j else (1 if (i-j)%n in (1,n-1) else 2*length)
                    assert abs(d[i,j] - expected) < 1e-12
                    checks += 1
                assert abs(d[i,n]-length)<1e-12
                checks += 1
            eigen = max_zero_sum_eigenvalue(d, p)
            assert abs(eigen[-1]) < 1e-8, (n,length,p,eigen[-3:])
            checks += 1
            for factor in (0.999, 1.001):
                signs = max_zero_sum_eigenvalue(d, p*factor)
                if factor < 1:
                    assert signs[-1] < -1e-7, (n,length,p,signs[-3:])
                else:
                    assert signs[-1] > 1e-7, (n,length,p,signs[-3:])
                checks += 1
            predicted_mult = (1 if length < ell - 1e-10 else
                              (1 if n%2 == 0 else 2) if length > ell + 1e-10 else
                              (2 if n%2 == 0 else 3))
            actual_mult = sum(abs(x) < 1e-8 for x in eigen)
            assert actual_mult == predicted_mult, (n,length,predicted_mult,actual_mult)
            checks += 1
            # Check exact quadratic-form decomposition on arbitrary vectors.
            for _ in range(4):
                x = rng.normal(size=n)
                xbar = np.mean(x)
                u = x - xbar
                z = np.r_[x, -sum(x)]
                q_direct = z @ (d**p) @ z
                aa = (2*length)**p
                bb = length**p
                cycle_pair = 2*sum(u[k]*u[(k+1)%n] for k in range(n))
                q_formula = n*((n-3)*aa + 2 - 2*n*bb)*xbar**2 - aa*(u@u) + (1-aa)*cycle_pair
                assert abs(q_direct-q_formula) < 3e-9, (n,length,q_direct,q_formula)
                checks += 1
    # The 4-rim geometric transition is a square with its Euclidean center.
    a,b,ell,pmax = constants(4)
    assert abs(ell-1/math.sqrt(2)) < 1e-12
    assert abs(pmax-2) < 1e-12
    checks += 2
    # Check the fixed-length and optimal-length large-rim asymptotics.
    for n in (100,200,400,800):
        length = .75
        p,_ = predicted(n, length)
        coefficient=(3-1/length)/math.log(2)
        assert abs(n*(p-1)-coefficient) < 5/n
        _,_,critical,optimum=constants(n)
        assert abs(n*(1-critical)-2)<10/n
        assert abs(n*(optimum-1)-2/math.log(2)) < 18/n
        checks += 3
    print('PASS standalone metric, quadratic form, spectral threshold, multiplicity and asymptotic checks:', checks)
    print('n=4: critical spoke length and optimal exponent:', constants(4)[2:])
    print('n=5: critical spoke length and optimal exponent:', constants(5)[2:])


if __name__ == '__main__':
    main()
