#!/usr/bin/env python3
"""Deterministic checks for a Bernoulli recursive-tree hitting-time theorem.

Uses only the Python standard library. Exact finite tests check the tree
identities; Gaussian limits are proved analytically, not by this program.
"""
from fractions import Fraction
from itertools import product
from math import isclose
from random import Random
from statistics import mean, pvariance

checks = 0


def test(condition, explanation='failed exact identity'):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)


def parents_of(steps):
    # T_N has vertices 0,...,N, with parent(1)=0.
    N = len(steps) + 1
    parent = [-1, 0]
    parent.extend(j - step for j, step in enumerate(steps, start=2))
    test(len(parent) == N + 1)
    return parent


def tree_data(parent):
    N = len(parent) - 1
    descendants = [1] * (N + 1)
    adjacency = [[] for _ in range(N + 1)]
    for j in range(1, N + 1):
        parent_j = parent[j]
        test(0 <= parent_j < j)
        descendants[parent_j] += 0  # Filled below in reverse order.
        adjacency[j].append(parent_j)
        adjacency[parent_j].append(j)
    for j in range(N, 0, -1):
        descendants[parent[j]] += descendants[j]
    path = []
    j = N
    while j:
        path.append(j)
        j = parent[j]
    depth = len(path)
    forward = sum(2 * (N + 1 - descendants[b]) - 1 for b in path)
    reverse = 2 * N * depth - forward
    area = sum(path)
    longest_two_run = 0
    streak = 0
    for j in range(2, N + 1):
        if j - parent[j] == 2:
            streak += 1
            longest_two_run = max(longest_two_run, streak)
        else:
            streak = 0
    return adjacency, descendants, path, forward, reverse, area, longest_two_run


def exact_walk_expectation(adjacency, target, start):
    N = len(adjacency) - 1
    names = [j for j in range(N + 1) if j != target]
    index = {j: k for k, j in enumerate(names)}
    a = [[Fraction(0) for _ in range(N + 1)] for _ in range(N)]
    for i, j in enumerate(names):
        a[i][i] = Fraction(len(adjacency[j]))
        a[i][-1] = Fraction(len(adjacency[j]))
        for v in adjacency[j]:
            if v != target:
                a[i][index[v]] -= 1
    for col in range(N):
        pivot = next(i for i in range(col, N) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        for k in range(col, N + 1):
            a[col][k] /= scale
        for i in range(N):
            if i == col:
                continue
            factor = a[i][col]
            if factor:
                for k in range(col, N + 1):
                    a[i][k] -= factor * a[col][k]
    return a[index[start]][-1]


def check_configuration(steps, solve=False):
    parent = parents_of(steps)
    N = len(parent) - 1
    adj, subtree, path, H, R, area, longest = tree_data(parent)
    test(H > 0 and R > 0)
    test(H + R == 2 * N * len(path), 'commute identity')
    test(H % 2 == len(path) % 2, 'path parity')
    test(abs(H - 2 * area) <= N * (2 * (longest + 1) + 1), 'global-run bound')
    for b in path:
        bypass = N + 1 - subtree[b] - b
        test(0 <= bypass <= longest + 1, f'bypass at {b}: {bypass}>{longest+1}')
    if solve:
        test(exact_walk_expectation(adj, N, 0) == H, 'independent forward linear system')
        test(exact_walk_expectation(adj, 0, N) == R, 'independent reverse linear system')
    return H, R


for N in range(1, 13):
    for bits in product((1, 2), repeat=N-1):
        check_configuration(bits, solve=(N <= 7))
print(f'exhaustive finite-tree checks: N=1,...,12; assertions={checks}')

# Exact two-point and boundary examples. At p=1 the tree is a path.
for N in (3, 10, 30, 100):
    H, R = check_configuration((1,) * (N-1))
    test(H == N * N and R == N * N, 'pure path')

# A quantitative finite-size diagnostic, not a proof of a limit theorem.
for p in (0.25, 0.5, 0.75):
    N = 4000
    rng = Random(78123 + int(1000*p))
    samples = []
    for _ in range(400):
        steps = [1 if rng.random() < p else 2 for j in range(2, N+1)]
        parent = parents_of(steps)
        _, _, path, H, R, _, _ = tree_data(parent)
        scale = N ** 1.5
        center = N * N / (2-p)
        samples.append(((H-center)/scale, (R-center)/scale))
    a = [x for x, _ in samples]
    b = [y for _, y in samples]
    va, vb = pvariance(a), pvariance(b)
    covariance = mean((x-mean(a))*(y-mean(b)) for x,y in samples)
    correlation = covariance / (va * vb) ** 0.5
    predicted = 4 * p * (1-p) / (3 * (2-p)**3)
    test(abs(va/predicted-1)<0.3 and abs(vb/predicted-1)<0.3, 'finite variance diagnostic')
    test(0.25<correlation<0.75, 'finite correlation diagnostic')
    test(abs(mean(a))<0.15 and abs(mean(b))<0.15, 'finite centering diagnostic')
    print(f'p={p:.2f}: sample means=({mean(a):.4f},{mean(b):.4f}), variances=({va:.4f},{vb:.4f}), predicted={predicted:.4f}, correlation={correlation:.4f}, limit=0.5000')

print(f'ALL CHECKS PASSED: {checks} deterministic assertions')
