#!/usr/bin/env python3
"""Reproduce finite examples for cyclic covers of binary words with runs <= 2.

The proof for all orders is mathematical (see RESULT.md), not a consequence
of this finite checker. Python standard library only.
"""
from collections import Counter, defaultdict, deque


def admissible(w):
    return '000' not in w and '111' not in w


def alternating(w):
    return all(x != y for x, y in zip(w, w[1:]))


def alpha(w):
    k = 0
    while k + 1 < len(w) and w[k] != w[k + 1]:
        k += 1
    return k


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def words(n):
    return (f'{j:0{n}b}' for j in range(1 << n))


def assemble(n):
    required = [w for w in words(n) if admissible(w)]
    duplicated = [w for w in required
                  if w[0] != w[1] and w[-2] != w[-1]
                  and not alternating(w)]
    edges = required + duplicated
    vset = {w[:-1] for w in required} | {w[1:] for w in required}
    out = Counter(w[:-1] for w in edges)
    inn = Counter(w[1:] for w in edges)
    assert all(out[v] == inn[v] for v in vset)

    outgoing = defaultdict(list)
    backward = defaultdict(list)
    forward = defaultdict(list)
    for w in required:
        forward[w[:-1]].append(w[1:])
        backward[w[1:]].append(w[:-1])
    for nb in (forward, backward):
        seen = {next(iter(vset))}
        q = deque(seen)
        while q:
            for v in nb[q.popleft()]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        assert seen == vset, 'required digraph must be strongly connected'

    for w in sorted(edges, reverse=True):
        outgoing[w[:-1]].append(w[1:])
    start = min(vset)
    stack, trail = [start], []
    while stack:
        if outgoing[stack[-1]]:
            stack.append(outgoing[stack[-1]].pop())
        else:
            trail.append(stack.pop())
    trail.reverse()
    assert len(trail) == len(edges) + 1 and trail[0] == trail[-1]
    cycle = ''.join(v[-1] for v in trail[1:])
    actual = Counter(''.join(cycle[(i + j) % len(cycle)] for j in range(n))
                     for i in range(len(cycle)))
    assert actual == Counter(edges)
    assert all(admissible(w) for w in actual)

    # Each binary edge, not just an admissible edge, changes the potential by <=1.
    assert all(alpha(w[:-1]) - alpha(w[1:]) <= 1 for w in words(n))
    assert all(alpha(w[:-1]) - alpha(w[1:]) == 1 for w in duplicated)
    required_drift = sum(alpha(w[:-1]) - alpha(w[1:]) for w in required)
    assert required_drift == -len(duplicated)

    expected = 2 * (fibonacci(n - 1) + fibonacci(n + 1)) - 2
    assert len(required) == 2 * fibonacci(n + 1)
    assert len(duplicated) == 2 * fibonacci(n - 1) - 2
    assert len(cycle) == expected
    return len(required), len(duplicated), cycle


def verify():
    for n in range(3, 17):
        required, extra, cycle = assemble(n)
        print(f'n={n:2d} required={required:5d} extra={extra:5d} optimal_length={len(cycle):5d}')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
