#!/usr/bin/env python3
from itertools import product

def count_transfer(source, target):
    k = len(target)
    prefix = [0]
    for q in target:
        prefix.append(prefix[-1] + q)

    r = source[0]
    S = [0] * k
    M = [0] * k
    for j in range(k):
        x = prefix[j]
        a = target[j] * ((x + 1) ** r - x ** r)
        b = (x + target[j]) ** r - x ** r - a
        S[j], M[j] = a, b

    for r in source[1:]:
        newS = [0] * k
        newM = [0] * k
        for j in range(k):
            newS[j] += S[j]
            for u in range(j):
                xM = prefix[j] - prefix[u + 1]
                xS = xM + 1

                aM = target[j] * ((xM + 1) ** r - xM ** r)
                bM = (xM + target[j]) ** r - xM ** r - aM
                aS = target[j] * ((xS + 1) ** r - xS ** r)
                bS = (xS + target[j]) ** r - xS ** r - aS

                newS[j] += M[u] * aM + S[u] * aS
                newM[j] += M[u] * bM + S[u] * bS
        S, M = newS, newM
    return sum(S) + sum(M)

def levels(sizes):
    out = []
    for level, size in enumerate(sizes):
        out.extend([level] * size)
    return out

def monotone(mapping, source_levels, target_levels):
    n = len(source_levels)
    for x in range(n):
        for y in range(n):
            if source_levels[x] < source_levels[y]:
                fx, fy = mapping[x], mapping[y]
                lx, ly = target_levels[fx], target_levels[fy]
                if not (lx < ly or (lx == ly and fx == fy)):
                    return False
    return True

def count_bruteforce(source, target):
    source_levels = levels(source)
    target_levels = levels(target)
    return sum(
        monotone(mapping, source_levels, target_levels)
        for mapping in product(range(len(target_levels)), repeat=len(source_levels))
    )

def compositions(n):
    if n == 1:
        return [(1,)]
    out = []
    for mask in range(1 << (n - 1)):
        part = 1
        comp = []
        for i in range(n - 1):
            if mask & (1 << i):
                comp.append(part)
                part = 1
            else:
                part += 1
        comp.append(part)
        out.append(tuple(comp))
    return out

small = []
for n in range(1, 5):
    small.extend(compositions(n))

cases = 0
for source in small:
    for target in small:
        transfer = count_transfer(source, target)
        brute = count_bruteforce(source, target)
        assert transfer == brute, (source, target, transfer, brute)
        cases += 1

anchors = [
    ((2, 2, 2), (2, 2), 44),
    ((2, 2, 2, 2), (2, 2, 2), 738),
    ((3, 2), (2, 3), 143),
    ((2, 1, 2), (1, 2), 17),
]
for source, target, expected in anchors:
    transfer = count_transfer(source, target)
    brute = count_bruteforce(source, target)
    assert transfer == expected == brute, (source, target, transfer, brute, expected)

print(f"VERIFY_OK exhaustive_pairs={cases} anchors={len(anchors)}")
