#!/usr/bin/env python3
"""Standalone checks of a finite-graph symmetric exclusion excursion theorem."""
import itertools, math
import numpy as np
from scipy.linalg import eigvals, expm

checks = 0

def ok(condition, msg):
    global checks
    assert bool(condition), msg
    checks += 1

def near(actual, expected, atol=1.e-8, rtol=1.e-8):
    ok(np.isclose(actual, expected, atol=atol, rtol=rtol),
       f"actual={actual}, expected={expected}")

def path(n):
    g = [[] for _ in range(n)]
    for i in range(n-1):
        g[i].append((i+1, 1.))
        g[i+1].append((i, 1.))
    return g

def star(n):
    g = [[] for _ in range(n)]
    for i in range(1, n):
        g[0].append((i, 1.))
        g[i].append((0, 1.))
    return g

def full_generator(g, root, q):
    n = len(g)
    states = list(itertools.product((0, 1), repeat=n))
    idx = {state: k for k, state in enumerate(states)}
    mat = np.zeros((len(states), len(states)), dtype=float)
    for i, st in enumerate(states):
        for u in range(n):
            for v, w in g[u]:
                if u < v and st[u] != st[v]:
                    z = list(st)
                    z[u], z[v] = z[v], z[u]
                    mat[i, idx[tuple(z)]] += w
                    mat[i, i] -= w
        z = list(st)
        z[root] = 1 - z[root]
        rate = (1. - q) if not st[root] else q
        mat[i, idx[tuple(z)]] += rate
        mat[i, i] -= rate
    return mat, states

def green(g, root):
    n = len(g)
    a = np.diag([0. if x == root else 1. for x in range(n)])
    for x in range(n):
        for y, rate in g[x]:
            a[x, x] += rate
            a[x, y] -= rate
    ok(np.linalg.eigvalsh(a).min() > 0, 'Green inverse not positive definite')
    return np.linalg.solve(a, np.eye(n)[:, root])[root]

def fib(k):
    x, y = 0, 1
    for _ in range(k):
        x, y = y, x+y
    return x

for n in range(2, 6):
    for kind, g in (('path', path(n)), ('star', star(n))):
        coeff = green(g, 0)
        exact_coeff = (fib(2*n-1)/fib(2*n-2) if kind == 'path'
                       else 2/(n-1))
        near(coeff, exact_coeff, atol=1.e-12)
        for q in (.17, .34, .53):
            gen, states = full_generator(g, 0, q)
            ix = {st:i for i,st in enumerate(states)}
            ok(np.linalg.norm(gen.sum(axis=1), np.inf)<1.e-12,
               'row sums of full generator')
            pi = np.array([(1.-q)**sum(st)*q**(n-sum(st))
                           for st in states])
            near(sum(pi), 1., atol=1.e-12)
            ok(np.linalg.norm(pi@gen, np.inf)<5.e-11,
               'stationary product measure')
            keep = [i for i,st in enumerate(states) if any(st)]
            sub = gen[np.ix_(keep, keep)]
            entrance = tuple([1]+[0]*(n-1))
            index = states.index(entrance)-1
            actual_mean = np.linalg.solve(-sub, np.ones(len(keep)))[index]
            expected_mean = (q**(-n)-1.)/(1.-q)
            near(actual_mean, expected_mean, atol=1.e-8, rtol=5.e-10)
        if n <= 4:
            for q in (.04, .02, .01):
                gen, states = full_generator(g, 0, q)
                sub = gen[1:, 1:]
                lambda_q = -float(eigvals(sub).real.max())
                ok(lambda_q>0, 'principal killed eigenvalue positive')
                coeff_est = (1.-lambda_q / ((1.-q)*q**n))/q
                ok(abs(coeff_est - coeff) <= 12*q + .005,
                   f'coefficient deviation {n=}, {kind=}, {q=}: {coeff_est=}, {coeff=}')
    if n >= 3:
        ok(green(path(n), 0) > green(star(n), 0),
           'rooted path and star must differ')

for n in (2, 3):
    for kind, g in (('path', path(n)), ('star', star(n))):
        for q in (.04, .02):
            gen, states = full_generator(g, 0, q)
            sub = gen[1:, 1:]
            entrance_index = states[1:].index(tuple([1]+[0]*(n-1)))
            for u in (.25, .7, 1.3, 2.):
                survival = (expm((u/q**n)*sub)@np.ones(len(sub)))[entrance_index]
                ok(0 <= survival <= 1.000001, 'survival outside probability interval')
                near(survival, np.exp(-u), atol=.16, rtol=.16)

print(f'PASS: {checks} deterministic graph, Green, stationary, mean, spectral and survival checks')
