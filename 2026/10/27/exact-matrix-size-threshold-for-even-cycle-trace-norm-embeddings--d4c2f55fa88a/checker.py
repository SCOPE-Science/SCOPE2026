#!/usr/bin/env python3
"""Finite diagnostic checks for trace-norm cycle embeddings.

Requires NumPy. Floating point tests are not proofs of universal claims.
"""
import math
import numpy as np


def nuclear_norm(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())


def ratio(values, norm):
    m = len(values)
    assert m % 2 == 0
    k = m // 2
    num = sum(norm(values[(j+k) % m] - values[j])**2 for j in range(m))/m
    den = sum(norm(values[(j+step) % m] - values[j])**2
              for j in range(m) for step in (-1, 0, 1))/(3*m)
    return math.sqrt(num/den)


def cycle_embedding(k):
    d = k
    edge = [np.diag(np.eye(d)[j]) for j in range(k)]
    edge += [-a for a in edge]
    values = [np.zeros((d,d),dtype=complex)]
    for a in edge: values.append(values[-1]+a)
    assert np.array_equal(values[-1], values[0])
    return values[:-1]


def run():
    assertions = 0
    for k in range(2, 13):
        v = cycle_embedding(k)
        m = 2*k
        for i in range(m):
            for j in range(m):
                distance = min((i-j) % m, (j-i) % m)
                assert abs(nuclear_norm(v[i]-v[j])-distance) < 1.e-9
                assertions += 1
        assert abs(ratio(v, nuclear_norm)-k*math.sqrt(1.5)) < 1.e-8
        assertions += 1
        a = [np.array([[complex(math.cos(2*math.pi*j/m), math.sin(2*math.pi*j/m))]]) for j in range(m)]
        exact = math.sqrt(1.5)/math.sin(math.pi/m)
        assert abs(ratio(a,nuclear_norm)-exact) < 1.e-8
        assertions += 1
    rng = np.random.default_rng(190739)
    for k in (2,3,4,5,6):
        for d in (1,2,3,5):
            for _ in range(120):
                a = rng.standard_normal((2*k,d,d))+1j*rng.standard_normal((2*k,d,d))
                rr = ratio(a, nuclear_norm)
                assert rr <= k*math.sqrt(1.5)*(1+1.e-10)
                assertions += 1
    print('PASS:',assertions,'finite diagnostic assertions')


if __name__ == '__main__':
    run()
