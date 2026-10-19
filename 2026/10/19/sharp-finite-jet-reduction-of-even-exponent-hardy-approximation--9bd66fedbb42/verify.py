#!/usr/bin/env python3
"""Reproducible tests for finite-jet Hardy even-moment approximation."""
import cmath
import math


def multiply(a, b, cutoff=None):
    out = [0j] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if cutoff is None or i + j <= cutoff:
                out[i + j] += x * y
    if cutoff is not None:
        return out[: cutoff + 1]
    return out


def objective_from_jet(m, n, q, fjet):
    L = (m - 1) * n
    assert len(q) <= n + 1 and len(fjet) >= L + 1
    qp = [[1 + 0j]]
    fp = [[1 + 0j]]
    for _ in range(m):
        qp.append(multiply(qp[-1], q))
        fp.append(multiply(fp[-1], fjet[:L+1], cutoff=L))
    answer = 0j
    for j in range(m + 1):
        answer += math.comb(m, j) ** 2 * sum(abs(a)**2 for a in qp[j])
        for k in range(j):
            prod = multiply(qp[j], fp[j-k], cutoff=k*n)
            inner = sum(prod[t] * qp[k][t].conjugate()
                        for t in range(min(len(prod), len(qp[k]))))
            answer += 2 * ((-1) ** (j + k)) * math.comb(m, j) * math.comb(m, k) * inner.real
    assert abs(answer.imag) < 1e-8
    return answer.real


def blaschke(a, z):
    return (z - a) / (1 - a * z)


def first_jet_of_blaschke(a, L):
    return [-a] + [(1-a*a) * a**(k-1) for k in range(1,L+1)]


def pow_eval(q, z):
    out = 0j
    for a in reversed(q):
        out = out * z + a
    return out


def circle_average(fun, size=8192):
    return sum(fun(cmath.exp(2j * math.pi * j / size)) for j in range(size))/size


def schur_parameters(a):
    f = a[:]
    out = []
    while f:
        gamma = f[0]
        assert abs(gamma) < 1 - 1e-8
        out.append(gamma)
        if len(f) == 1:
            break
        denominator = [1-abs(gamma)**2] + [-gamma.conjugate() * z for z in f[1:]]
        numerator = f[1:]
        g = []
        for k in range(len(numerator)):
            g.append((numerator[k]-sum(denominator[j] * g[k-j]
                        for j in range(1,k+1)))/denominator[0])
        f = g
    return out


def evaluate_schur_blaschke(gammas, z):
    x = 1 + 0j
    for gamma in reversed(gammas):
        x = (gamma + z * x)/(1 + gamma.conjugate() * z * x)
    return x


def check(m, n, a, b, rootA, rootB):
    L = (m-1)*n
    assert rootA > L and rootB > L
    fjet = [-b * t for t in first_jet_of_blaschke(a, L)]
    q = [(0.2-0.15j), (0.11+0.2j), (-0.08+0.05j)][:n+1]
    assert len(q) == n+1
    alg = objective_from_jet(m,n,q,fjet)
    numbers = []
    for K in [rootA,rootB]:
        integ = circle_average(lambda z: abs(1-pow_eval(q,z)*blaschke(a,z)*blaschke(b,z**K))**(2*m))
        numbers.append(integ)
        assert abs(alg-integ) < 1e-9, (m,n,K,alg,integ)
    params = schur_parameters(fjet)
    bpoly = lambda z: evaluate_schur_blaschke(params,z)
    jetB = [circle_average(lambda z,k=k:bpoly(z)/z**k) for k in range(L+1)]
    assert max(abs(jetB[k]-fjet[k]) for k in range(L+1)) < 1e-10
    assert max(abs(abs(bpoly(cmath.exp(2j*math.pi*t/37)))-1) for t in range(37)) < 1e-10
    repl = circle_average(lambda z:abs(1-pow_eval(q,z)*bpoly(z))**(2*m))
    assert abs(repl-alg) < 1e-9
    print('matching jets m,n,L:',m,n,L,'objective:',format(alg,'.12f'),
          'two inner factors:',*(format(x,'.12f') for x in numbers),
          'finite Blaschke:',format(repl,'.12f'))


def sharpness(m,n):
    L = (m-1)*n
    assert L>0
    q = [1 + 0j]+[0j]*(n-1)+[1+0j]
    fp = [0j]*L+[1+0j]
    fm = [0j]*L+[-1+0j]
    plus = objective_from_jet(m,n,q,fp)
    minus = objective_from_jet(m,n,q,fm)
    assert abs((plus-minus)+4*m) < 1e-8
    print('sharpness m,n,L:',m,n,L,'objectives:',plus,minus,'difference:',plus-minus)


if __name__ == '__main__':
    check(2,1,1/3,1/2,2,3)
    check(3,2,1/3,1/2,5,6)
    check(4,1,1/5,1/3,4,5)
    for m,n in [(2,1),(3,2),(4,1),(5,3)]:
        sharpness(m,n)
    print('ALL TESTS PASSED: independent circle integration, finite jets, Schur replacement, and optimal cutoff witness.')
