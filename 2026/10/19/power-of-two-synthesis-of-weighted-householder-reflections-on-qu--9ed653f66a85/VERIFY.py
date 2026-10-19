#!/usr/bin/env python3
"""Finite-matrix checks for the stated quantum-spider/path identities.

Requires NumPy. These checks illustrate exact formulas and do not replace
analytical proofs or establish a universal non-existence statement.
"""
import math
import numpy as np


def weighted_spider(weights, length):
    k = len(weights)
    num = 1 + k * length
    adjacency = np.zeros((num, num), dtype=float)
    for i, weight in enumerate(weights):
        previous = 0
        for depth in range(length):
            current = 1 + i * length + depth
            adjacency[previous, current] = float(weight)
            adjacency[current, previous] = float(weight)
            previous = current
    degree = adjacency.sum(axis=1)
    hamiltonian = np.eye(num) - adjacency / np.sqrt(np.outer(degree, degree))
    v = np.sqrt(np.asarray(weights, dtype=float) / np.sum(weights))
    householder = 2.0 * np.outer(v, v) - np.eye(k)
    target = np.eye(num)
    for depth in range(length):
        layer = [1 + i * length + depth for i in range(k)]
        target[np.ix_(layer, layer)] = householder
    return hamiltonian, target, v


def normalized_path(num):
    adjacency = np.zeros((num, num), dtype=float)
    for i in range(num - 1):
        adjacency[i, i + 1] = adjacency[i + 1, i] = 1.0
    degree = adjacency.sum(axis=1)
    return np.eye(num) - adjacency / np.sqrt(np.outer(degree, degree))


def propagator(hamiltonian, time):
    eig, eigvec = np.linalg.eigh(hamiltonian)
    return (eigvec * np.exp(-1j * time * eig)) @ eigvec.T


def main():
    rng = np.random.default_rng(20261013)
    norm_err = 0.0
    kernel_err = 0.0
    trials = 0
    for length in range(1, 8):
        n = 2 * length + 1
        path_h = normalized_path(n)
        reflection = np.eye(n)[::-1]
        for num_arms in [3, 4, 6]:
            for rep in range(3):
                weights = np.exp(rng.normal(size=num_arms))
                spider_h, spider_r, v = weighted_spider(weights, length)
                for time in [0.0, 0.17, 1.2, 3.95, 8.8, 21.0]:
                    walk = propagator(spider_h, time)
                    path_walk = propagator(path_h, time)
                    diff = abs(np.linalg.norm(walk - spider_r, 2) -
                               np.linalg.norm(path_walk - reflection, 2))
                    norm_err = max(norm_err, diff)
                    assert diff < 1e-11, (length, num_arms, diff)
                    for i in range(num_arms):
                        for j in range(num_arms):
                            if i == j:
                                continue
                            a = walk[1 + j * length + length - 1,
                                     1 + i * length + length - 1]
                            b = 2 * v[i] * v[j] * path_walk[-1, 0]
                            err = abs(a - b)
                            kernel_err = max(kernel_err, err)
                            assert err < 1e-11, (length, num_arms, i, j, err)
                    trials += 1
    one_h, one_r, _ = weighted_spider([1, 2, 5, 3], 1)
    assert np.linalg.norm(propagator(one_h, math.pi) - one_r, 2) < 1e-12
    two_h, two_r, _ = weighted_spider([1, 2, 5, 3], 2)
    errors = [np.linalg.norm(propagator(two_h, 2*math.pi*m) - two_r, 2)
              for m in [5, 29, 169]]
    assert errors[0] > errors[1] > errors[2]
    print('PASS: tested', trials, 'times/weighted graph configurations')
    print('max operator-norm identity discrepancy:', norm_err)
    print('max cross-terminal amplitude discrepancy:', kernel_err)
    print('L=2 sample improving errors:', errors)


if __name__ == '__main__':
    main()
