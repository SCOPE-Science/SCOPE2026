#!/usr/bin/env python3
from collections import Counter
from math import comb

def partitions(n):
    out = []
    def rec(rem, lo, cur):
        if rem == 0:
            if len(cur) >= 2:
                out.append(tuple(cur))
            return
        for x in range(lo, rem + 1):
            rec(rem - x, x, cur + [x])
    rec(n, 1, [])
    return out

def graph(profile):
    labels = []
    for i, size in enumerate(profile):
        labels.extend([i] * size)
    n = len(labels)
    adj = [set() for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            if labels[u] != labels[v]:
                adj[u].add(v)
                adj[v].add(u)
    return labels, adj

def connected(mask, adj, n):
    verts = [v for v in range(n) if (mask >> v) & 1]
    if not verts:
        return False
    if len(verts) == 1:
        return True
    seen = {verts[0]}
    stack = [verts[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if ((mask >> v) & 1) and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(verts)

def dominates(mask, adj, n):
    for v in range(n):
        if not ((mask >> v) & 1):
            if not any((mask >> u) & 1 for u in adj[v]):
                return False
    return True

def literal(mask, profile):
    labels, adj = graph(profile)
    n = len(labels)
    full = (1 << n) - 1
    return (
        dominates(mask, adj, n)
        and connected(mask, adj, n)
        and connected(full ^ mask, adj, n)
    )

def criterion(mask, profile):
    counts = []
    pos = 0
    for size in profile:
        counts.append(sum((mask >> (pos + j)) & 1 for j in range(size)))
        pos += size
    n = sum(profile)
    d = sum(counts)
    c = n - d
    selected_support = sum(x > 0 for x in counts)
    complement_support = sum(counts[i] < profile[i] for i in range(len(profile)))
    selected_ok = (
        selected_support >= 2
        or (
            d == 1
            and any(profile[i] == 1 and counts[i] == 1 for i in range(len(profile)))
        )
    )
    complement_ok = c == 1 or complement_support >= 2
    return selected_ok and complement_ok

def formula(profile):
    n = sum(profile)
    singleton_parts = sum(size == 1 for size in profile)
    coeff = Counter()
    for k in range(1, n):
        coeff[k] += comb(n, k)
    for size in profile:
        for k in range(2, size + 1):
            coeff[k] -= comb(size, k)
    for size in profile:
        for omitted in range(2, size + 1):
            coeff[n - omitted] -= comb(size, omitted)
    if len(profile) == 2 and profile[0] >= 2 and profile[1] >= 2:
        coeff[profile[0]] += 1
        coeff[profile[1]] += 1
    coeff[1] -= n - singleton_parts
    return Counter({k: v for k, v in coeff.items() if v})

profiles = 0
subset_checks = 0
dcd_sets = 0
coefficient_checks = 0

for n in range(2, 10):
    for profile in partitions(n):
        profiles += 1
        actual = Counter()
        predicted = Counter()
        for mask in range(1 << n):
            subset_checks += 1
            a = literal(mask, profile)
            b = criterion(mask, profile)
            if a != b:
                raise AssertionError(("criterion", profile, mask, a, b))
            if a:
                actual[mask.bit_count()] += 1
                dcd_sets += 1
            if b:
                predicted[mask.bit_count()] += 1
        if actual != predicted:
            raise AssertionError(("profile-count", profile, actual, predicted))
        closed = formula(profile)
        if actual != closed:
            raise AssertionError(("polynomial", profile, actual, closed))
        coefficient_checks += n + 1

print(
    "VERIFY_OK "
    f"profiles={profiles} "
    f"subset_checks={subset_checks} "
    f"dcd_sets={dcd_sets} "
    f"coefficient_checks={coefficient_checks} "
    "max_order=9"
)
