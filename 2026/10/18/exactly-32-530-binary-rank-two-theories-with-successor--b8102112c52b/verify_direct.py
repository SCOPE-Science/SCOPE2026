#!/usr/bin/env python3
"""Independent positional-witness enumeration of the rank-two quotient.

This verifier does not import or reuse the bitmask-profile transition program.
For every point it enumerates all potential witnesses and stores their atomic
order/successor/letter profiles. A breadth-first search enumerates signatures.
"""
from collections import Counter, deque


def signature(word):
    realizations = set()
    for i, a in enumerate(word):
        witnessed = set()
        for j, b in enumerate(word):
            if i == j:
                relative = 0
            elif j == i - 1:
                relative = 1
            elif j < i:
                relative = 2
            elif j == i + 1:
                relative = 3
            else:
                relative = 4
            witnessed.add((b, relative))
        realizations.add((a, frozenset(witnessed)))
    return frozenset(realizations)


def calculate():
    empty = ()
    q = deque([empty])
    visited = {signature(empty): empty}
    counts = Counter({0: 1})
    while q:
        w = q.popleft()
        for a in (0, 1):
            v = w + (a,)
            sig = signature(v)
            if sig not in visited:
                visited[sig] = v
                q.append(v)
                counts[len(v)] += 1
    answer = (len(visited),
              sum(len(set(w)) == 2 for w in visited.values()),
              max(counts),
              tuple(counts[i] for i in range(max(counts) + 1)))
    assert answer[:3] == (32541, 32530, 24), answer
    assert answer[-1][-1] == 16
    return answer


if __name__ == '__main__':
    print(calculate())
