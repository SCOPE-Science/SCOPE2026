"""Exact-rational checks of the Wiener-index parent-label response in random recursive trees.

Standard library only. The enumerations verify finite sizes; the supplied analytic proof
establishes the theorem for all sizes.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, e


def harmonic(m, power=1):
    return sum((Q(1, j**power) for j in range(1, m + 1)), Q(0))


def expected_wiener(n):
    return n * (n + 1) * harmonic(n) - 2 * n * n


def excess(n, i, v):
    return Q(n * (n + 1), i * (i + 1)) * (
        (i - 1) * (harmonic(v - 1) + 1 + Q(2, v))
        - (i + 1) * harmonic(i - 1)
    )


def exact_root_cov(n):
    return n * (n + 1) * (
        Q(3, 2) - Q(3, n + 1) - harmonic(n - 1, 2)
        + harmonic(n - 1) / n
    )


def wiener_of_parents(parents):
    n = len(parents) - 1
    graph = [[] for _ in range(n + 1)]
    for vertex in range(2, n + 1):
        parent = parents[vertex]
        graph[vertex].append(parent)
        graph[parent].append(vertex)
    result = 0
    for src in range(1, n + 1):
        distances = [-1] * (n + 1)
        distances[src] = 0
        queue = [src]
        for vertex in queue:
            for neighbor in graph[vertex]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[vertex] + 1
                    queue.append(neighbor)
        result += sum(distances[src + 1:])
    return result


def exhaustive_small_sizes():
    trees = 0
    conditional_identities = 0
    covariance_identities = 0
    for n in range(2, 10):
        count = factorial(n - 1)
        sum_w = sum_k = sum_kw = 0
        joint_by_parent = {(i, v): 0 for i in range(2, n + 1) for v in range(1, i)}
        for parent_tuple in product(*(range(1, i) for i in range(2, n + 1))):
            parents = [0, 0] + list(parent_tuple)
            w = wiener_of_parents(parents)
            k = sum(parent == 1 for parent in parent_tuple)
            sum_w += w
            sum_k += k
            sum_kw += k * w
            for i, v in enumerate(parent_tuple, 2):
                joint_by_parent[(i, v)] += w
        trees += count
        ew = Q(sum_w, count)
        ek = Q(sum_k, count)
        assert ew == expected_wiener(n), (n, 'mean Wiener')
        assert ek == harmonic(n - 1), (n, 'mean root degree')
        assert Q(sum_kw, count) - ew * ek == exact_root_cov(n), (n, 'covariance')
        covariance_identities += 1
        for (i, v), joint_sum in joint_by_parent.items():
            # Each specific parent occurs in exactly 1/(i-1) of all trees.
            conditional_mean = Q(joint_sum * (i - 1), count)
            assert conditional_mean - ew == excess(n, i, v), (n, i, v)
            conditional_identities += 1
    return trees, conditional_identities, covariance_identities


def recurrence_and_threshold_checks():
    exact_identities = 0
    for n in range(2, 121):
        kernel_sum = sum((excess(n, i, 1) / (i - 1) for i in range(2, n + 1)), Q(0))
        assert kernel_sum == exact_root_cov(n)
        exact_identities += 1
        for i in range(2, min(n, 36) + 1):
            assert sum((excess(n, i, v) for v in range(1, i)), Q(0)) == 0
            exact_identities += 1
            values = [excess(n, i, v) for v in range(1, i)]
            assert values[0] == values[1] if i >= 3 else values[0] == 0
            assert all(values[j] < values[j + 1] for j in range(1, len(values) - 1))
            if i >= 4:
                assert values[0] < 0 < values[-1]
    ratios = []
    for i in (100, 1000, 10000):
        # Float test only for numerically illustrating the proved asymptotic;
        # all finite exact identities above use rational arithmetic.
        h = sum(1 / j for j in range(1, i))
        threshold = (i + 1) * h / (i - 1)
        low, high = 2, i - 1
        while low < high:
            mid = (low + high) // 2
            g = sum(1 / j for j in range(1, mid)) + 1 + 2 / mid
            if g >= threshold:
                high = mid
            else:
                low = mid + 1
        ratios.append((i, low, low / i))
    assert abs(ratios[-1][2] - 1 / e) < .003, ratios
    return exact_identities, ratios


if __name__ == '__main__':
    trees, conditional, mixed = exhaustive_small_sizes()
    recurrent, ratios = recurrence_and_threshold_checks()
    print('OK trees:', trees)
    print('OK conditional finite laws:', conditional)
    print('OK exhaustive covariance laws:', mixed)
    print('OK exact recursion and averaging identities:', recurrent)
    print('Illustrative age threshold ratios:', ratios)
