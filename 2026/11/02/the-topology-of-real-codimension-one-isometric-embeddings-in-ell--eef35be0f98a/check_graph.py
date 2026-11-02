"""Independent finite sanity checks for the signed-injection graph of real ell-p isometries.

The general theorem is proved analytically; this script checks small dimensions only.
"""
from itertools import permutations, product
from collections import deque
from math import factorial, isclose


def graph(n):
    k = n - 1
    vertices = list(product(permutations(range(n)), product((-1, 1), repeat=k)))
    # permutation entries are row positions of ordered columns, then blank row.
    index = {v: i for i, v in enumerate(vertices)}
    assert len(vertices) == (2 ** k) * factorial(n)
    adjacency = [set() for _ in vertices]
    for i, (rows, signs) in enumerate(vertices):
        for col in range(k):
            swapped = list(rows)
            swapped[col], swapped[k] = swapped[k], swapped[col]
            for new_sign in (-1, 1):
                next_signs = list(signs)
                next_signs[col] = new_sign
                j = index[(tuple(swapped), tuple(next_signs))]
                assert j != i
                adjacency[i].add(j)
                adjacency[j].add(i)
    edges = sum(len(s) for s in adjacency) // 2
    seen = {0}
    todo = deque([0])
    while todo:
        a = todo.popleft()
        for b in adjacency[a]:
            if b not in seen:
                seen.add(b)
                todo.append(b)
    assert len(seen) == len(vertices)
    assert {len(s) for s in adjacency} == {2*k}
    assert edges == 2**(n-1) * (n-1) * factorial(n)
    assert edges - len(vertices) + 1 == 1 + 2**(n-1)*(n-2)*factorial(n)
    # Each edge endpoint has a unique signed-injection coordinate arrangement.
    return len(vertices), edges, edges - len(vertices) + 1


def vector_isometry_checks():
    samples = 0
    for p in (1.0, 1.5, 3.0, 4.0):
        for n in (2, 3, 4, 5):
            k = n - 1
            for rows in permutations(range(n)):
                signs = [(-1 if j % 2 else 1) for j in range(k)]
                for col in range(k):
                    for new_sign in (-1, 1):
                        for t in (0.01, 0.2, 0.5, 0.8, 0.99):
                            A = [[0.0] * k for _ in range(n)]
                            for j in range(k):
                                if j == col:
                                    A[rows[j]][j] = signs[j] * (1-t)**(1/p)
                                    A[rows[k]][j] = new_sign * t**(1/p)
                                else:
                                    A[rows[j]][j] = signs[j]
                            for x in ((1.0,)*k, tuple((-1)**j * (j+1)/3 for j in range(k))):
                                lhs = sum(abs(sum(A[i][j]*x[j] for j in range(k)))**p for i in range(n))
                                rhs = sum(abs(xj)**p for xj in x)
                                assert isclose(lhs, rhs, rel_tol=1e-11, abs_tol=1e-11)
                                samples += 1
    return samples


if __name__ == '__main__':
    for n in (2, 3, 4, 5, 6):
        v, e, b = graph(n)
        print(f'n={n}: V={v}, E={e}, beta1={b}, connected=True')
    print('disjoint-support norm tests:', vector_isometry_checks(), 'passed')
