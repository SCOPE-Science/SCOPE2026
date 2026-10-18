#!/usr/bin/env python3
"""Finite diagnostics for the seven-cycle weighted Schatten-fourth minimax formulas.

This checks matrix identities and samples candidate minimizers; it is not
an exhaustive certificate for the continuous simplex optimization.
"""
import cmath
import itertools
import math
import random

N = 7

def adjoint(A):
    return [[A[j][i].conjugate() for j in range(N)] for i in range(N)]

def product(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def trace(A):
    return sum(A[i][i] for i in range(N))

def direct(w, t, angle):
    W = [[0j for _ in range(N)] for _ in range(N)]
    for j in range(N):
        W[(j + 1) % N][j] = w[j]
    Z = [[t * cmath.exp(1j * angle) * W[i][j] + (1 - t) * cmath.exp(-1j * angle) * W[j][i].conjugate() for j in range(N)] for i in range(N)]
    H = product(adjoint(Z), Z)
    return trace(product(H, H)).real

def cyclic(q, x):
    return sum(v * v for v in x) + q * sum(x[j] * x[(j + 1) % N] for j in range(N))

def analytic(q):
    c1 = 1 / math.cos(math.pi / N)
    c2 = math.sqrt(5) - 1
    if q <= c1:
        return (1 + q) / 7
    if q <= c2:
        return (4 + 2 * q - q*q) / (20 - 2 * q - q*q)
    return (q + 2) / (2 * (4 + q))

def profile(q):
    c1 = 1 / math.cos(math.pi / N)
    c2 = math.sqrt(5) - 1
    if q < c1:
        return [1 / 7] * N
    if q <= c2:
        d = 20 - 2*q - q*q
        a, b, c = (4+2*q-q*q)/d, 4/d, 2*(2-q)/d
        return [a, 0, b, c, c, b, 0]
    a, b = 1/(4+q), (2+q)/(2*(4+q))
    return [a, 0, b, 0, b, 0, a]

def check():
    rng = random.Random(1357911)
    tests = 0
    for t in [0, .11, .28, .5, .74, 1]:
        u = 1-t
        A, B = t**4+u**4, 4*t*t*u*u
        for _ in range(30):
            angles = [rng.uniform(-math.pi, math.pi) for _ in range(N)]
            x = [rng.random() for _ in range(N)]
            sx = sum(x)
            x = [xi/sx for xi in x]
            w = [math.sqrt(xi)*cmath.exp(1j*a) for xi,a in zip(x,angles)]
            for theta in [0.01, 0.26, 1.73]:
                measured = direct(w, t, theta)
                predicted = A * cyclic(B/A, x)
                assert abs(measured-predicted)<1e-10,(t,measured,predicted)
                tests += 1
    for q in [0, .4, 1, 1.1099162641747418, 1.11, 1.15, 1.2, 1.2360679774997898, 1.3, 1.5, 1.9, 2]:
        opt = analytic(q)
        x = profile(q)
        assert abs(sum(x)-1)<1e-11
        assert min(x)>-1e-11
        assert abs(cyclic(q,x)-opt)<1e-10,(q,opt,cyclic(q,x))
        for _ in range(4500):
            z=[rng.gammavariate(1,1) for _ in range(N)]
            total=sum(z)
            z=[p/total for p in z]
            assert cyclic(q,z)+1e-10>=opt, (q,z,cyclic(q,z),opt)
            tests +=1
    # Every four-vertex set either embeds in a five-face with missing
    # vertices at circular distance two, or induces two disjoint edges.
    for S in itertools.combinations(range(N),4):
        T=set(range(N))-set(S)
        has_distance_two=any((i+2)%N in T for i in T)
        if not has_distance_two:
            edges=sorted((i,(i+1)%N) for i in S if (i+1)%N in S)
            assert len(edges)==2 and len(set(v for e in edges for v in e))==4
        tests+=1
    # At the second threshold the path-four kernel is a sum-zero vector.
    q=math.sqrt(5)-1
    z=[math.sin(math.pi/5),-math.sin(2*math.pi/5),math.sin(2*math.pi/5),-math.sin(math.pi/5)]
    assert abs(sum(z))<1e-12
    for i in range(4):
        g=z[i]+q/2*((z[i-1] if i else 0)+(z[i+1] if i<3 else 0))
        assert abs(g)<1e-12
        tests+=1
    print('DIAGNOSTICS_OK',tests)

if __name__=='__main__':
    check()
