#!/usr/bin/env python3
"""Reproduce finite checks supporting a rank classification for multipartite quantum walks.

Requires NumPy. The classification for arbitrary part sizes and number of parts
is proved algebraically; these finite checks do not establish its infinite scope.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import numpy as np


def graph(parts):
    labels = [j for j, n in enumerate(parts) for _ in range(n)]
    return np.array([[int(a != b) for b in labels] for a in labels], dtype=float), labels


def predicted_nullity(parts):
    return sum(n == 2 for n in parts) + int(sum(n == 1 for n in parts) == 2)


def mixing(A):
    eigenvalues, vectors = np.linalg.eigh(A)
    groups = []
    for i, ev in enumerate(eigenvalues):
        if not groups or abs(ev - groups[-1][0]) > 2e-8:
            groups.append([ev, [i]])
        else:
            groups[-1][1].append(i)
    ans = np.zeros_like(A)
    for _, js in groups:
        P = vectors[:, js] @ vectors[:, js].T
        ans += P * P
    return ans, len(groups)


def exact_idempotents(parts):
    n = sum(parts)
    labels = [j for j, q in enumerate(parts) for _ in range(q)]
    Es = [[F(int(i == j) - (F(1, parts[labels[i]]) if labels[i] == labels[j] else 0))
           if parts[labels[i]] > 1 and labels[i] == labels[j] else F(0)
           for j in range(n)] for i in range(n)]
    singleton_indices = [i for i, q in enumerate(labels) if parts[q] == 1]
    s = len(singleton_indices)
    Et = [[F(int(i == j)) - F(1, s) if s >= 2 and i in singleton_indices and j in singleton_indices
           else F(0) for j in range(n)] for i in range(n)]
    A = [[F(int(a != b)) for b in labels] for a in labels]
    def mult(X,Y):
        return [[sum((X[i][k] * Y[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]
    assert mult(Es,Es) == Es and mult(Et,Et) == Et and not any(any(y for y in row) for row in mult(Es,Et))
    assert not any(any(y for y in row) for row in mult(A,Es))
    assert mult(A,Et) == [[-y for y in row] for row in Et]
    for i,ni in enumerate(parts):
        ids = [k for k,q in enumerate(labels) if q==i]
        if ni >= 2:
            for a in ids:
                for b in ids:
                    expected = (F(1) - F(2,ni) if a==b else F(0)) + F(1,ni*ni)
                    assert Es[a][b]**2 == expected
    for a in singleton_indices:
        for b in singleton_indices:
            if s >= 2:
                expected = (F(1)-F(2,s) if a==b else F(0)) + F(1,s*s)
                assert Et[a][b]**2 == expected
    return n


def run():
    cases = 0
    eigengroups = 0
    exact_cases = 0
    first_exception = None
    min_positive = 1.0
    for r in range(2, 6):
        for parts in combinations_with_replacement(range(1, 5), r):
            n = sum(parts)
            if n > 18:
                continue
            A, labels = graph(parts)
            M, g = mixing(A)
            eigengroups += g
            eigen = np.linalg.eigvalsh(M)
            predicted = predicted_nullity(parts)
            actual = int(np.sum(eigen < 2e-8))
            assert actual == predicted, (parts, eigen, actual, predicted)
            positive = eigen[predicted:] if predicted else eigen
            if len(positive):
                min_positive = min(min_positive, float(min(positive)))
            assert np.max(np.abs(M.sum(axis=1) - 1)) < 1e-9
            assert min(eigen) > -1e-8
            # Kernel vectors predicted by false-twin and true-twin classes.
            for j, part_n in enumerate(parts):
                ids = [i for i, x in enumerate(labels) if x == j]
                if part_n == 2:
                    v = np.zeros(n); v[ids[0]] = 1; v[ids[1]] = -1
                    assert max(abs(M @ v)) < 1e-8
            si = [i for i, j in enumerate(labels) if parts[j] == 1]
            if len(si) == 2:
                v = np.zeros(n); v[si[0]] = 1; v[si[1]] = -1
                assert max(abs(M @ v)) < 1e-8
            if parts == (1,1,2) and first_exception is None:
                first_exception = (n, n-predicted)
            cases += 1
            if n <= 12:
                exact_idempotents(parts); exact_cases += 1
    assert first_exception == (4, 2)
    print(f'VERIFY_OK independent_matrix_cases={cases} exact_projector_cases={exact_cases} '
          f'distinct_eigenvalue_groups={eigengroups} diamond_rank=2/4 '
          f'least_positive_eigenvalue_tested={min_positive:.9g}')

if __name__ == '__main__':
    run()
