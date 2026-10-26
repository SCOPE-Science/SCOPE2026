#!/usr/bin/env python3
"""Independent finite checks for the locating-hop census of K_n square K_2.
The tests compute ordinary graph distances with BFS and evaluate the definition
on every selected vertex subset, without using the theorem's membership rule.
"""
from collections import Counter, deque
from math import comb


def graph(n):
    vertices = 2 * n
    out = [set() for _ in range(vertices)]
    for layer in range(2):
        for i in range(n):
            for j in range(n):
                if i != j:
                    out[layer * n + i].add(layer * n + j)
    for i in range(n):
        out[i].add(n + i)
        out[n + i].add(i)
    return out


def hop_masks(n):
    adjacency = graph(n)
    output = []
    for root in range(2 * n):
        d = [-1] * (2 * n)
        d[root] = 0
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in adjacency[v]:
                if d[w] == -1:
                    d[w] = d[v] + 1
                    queue.append(w)
        assert max(d) == 2
        output.append(sum(1 << v for v in range(2 * n) if d[v] == 2))
    return output


def according_to_definition(selection, distance_two, total):
    witnesses = set()
    for v in range(total):
        if (selection >> v) & 1:
            continue
        signature = distance_two[v] & selection
        if signature == 0 or signature in witnesses:
            return False
        witnesses.add(signature)
    return True


def characteristic(n, selection):
    a = {i for i in range(n) if (selection >> i) & 1}
    b = {i for i in range(n) if (selection >> (n + i)) & 1}
    if not a:
        return len(b) == n
    if not b:
        return len(a) == n
    if len(a) >= 2 and len(b) >= 2:
        return len(a | b) >= n - 1
    if len(a) == 1:
        return len(b) == n or (len(b) == n - 1 and a <= b)
    if len(b) == 1:
        return len(a) == n or (len(a) == n - 1 and b <= a)
    return False


def multiply(a, b):
    result = Counter()
    for i, v in a.items():
        for j, w in b.items():
            result[i + j] += v * w
    return result


def power(poly, n):
    result = Counter({0: 1})
    for _ in range(n):
        result = multiply(result, poly)
    return result


def predicted_all(n):
    q = Counter({1: 2, 2: 1})
    ans = power(q, n)
    for k, v in power(q, n - 1).items():
        ans[k] += n * v
    ans[n - 1] -= 2 * n * n
    ans[n] -= 2 * n
    if n == 3:
        ans[2] += 6
    return +ans


def predicted_minimal(n):
    if n == 3:
        return Counter({3: 14})
    if n == 4:
        return Counter({4: 56})
    return Counter({n - 1: n * (2 ** (n - 1) - 2 * n),
                    n: 2 * n * (n - 1) + 2})


def main():
    examined = 0
    for n in range(3, 9):
        hop = hop_masks(n)
        count = 1 << (2 * n)
        is_good = bytearray(count)
        profile = Counter()
        for s in range(count):
            v = according_to_definition(s, hop, 2 * n)
            if v != characteristic(n, s):
                raise AssertionError(f'wrong characterization: n={n}, mask={s}')
            is_good[s] = v
            if v:
                profile[s.bit_count()] += 1
        minimal = Counter()
        for s in range(count):
            if is_good[s] and all(not is_good[s ^ (1 << j)]
                                  for j in range(2 * n) if s & (1 << j)):
                minimal[s.bit_count()] += 1
        assert profile == predicted_all(n), (n, profile, predicted_all(n))
        assert minimal == predicted_minimal(n), (n, minimal, predicted_minimal(n))
        examined += count
        print(f'n={n} checked={count} all={sorted(profile.items())} '
              f'minimal={sorted(minimal.items())}')
    print('ALL PASSED:', examined, 'vertex subsets; complete BFS-based predicate, '
          'classification, two generating polynomials')


if __name__ == '__main__':
    main()
