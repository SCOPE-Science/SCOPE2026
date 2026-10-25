#!/usr/bin/env python3
"""Recompute the base face cycles and sanity-check the local K_{4,n} extension."""
from collections import Counter

BASE_A = [
    (0,1,2,3,4), (0,4,2,1,3), (0,3,4,2,1), (0,2,4,3,1)
]
BASE_B = [
    (0,1,2,3), (0,3,1,2), (0,2,3,1), (0,2,1,3), (0,3,2,1)
]

def faces(rot_a, rot_b, n):
    successor = {}
    for i, row in enumerate(rot_a):
        for j, b in enumerate(row):
            successor[(('A', i), ('B', b))] = ('B', row[(j+1) % len(row)])
    for j, row in enumerate(rot_b):
        for i, a in enumerate(row):
            successor[(('B', j), ('A', a))] = ('A', row[(i+1) % len(row)])
    darts = []
    for i in range(4):
        for j in range(n):
            darts.extend([(('A', i), ('B', j)), (('B', j), ('A', i))])
    seen, result = set(), []
    for dart in darts:
        if dart in seen:
            continue
        walk, current = [], dart
        while current not in seen:
            seen.add(current)
            walk.append(current[0])
            u, v = current
            current = (v, successor[(v, u)])
        result.append(walk)
    return result

def extend(rot_a, rot_b, n):
    new_a = []
    for i, row in enumerate(rot_a):
        k = row.index(0)
        if i in (0, 2):
            row2 = row[:k] + (n, n+1) + row[k:]
        else:
            row2 = row[:k+1] + (n+1, n) + row[k+1:]
        new_a.append(row2)
    return new_a, rot_b + [(0,1,2,3), (0,3,2,1)]

def main():
    a, b, n = BASE_A, BASE_B, 5
    for expected_n in (5, 7, 9, 11):
        f = faces(a, b, n)
        lengths = Counter(map(len, f))
        assert lengths == {4: 2*n-3, 6: 2}, (n, lengths)
        assert len(f) == 2*n-1
        if n < 11:
            a, b = extend(a, b, n)
            n += 2
    print("PASS: face-length multisets verified for n=5,7,9,11")

if __name__ == '__main__':
    main()
