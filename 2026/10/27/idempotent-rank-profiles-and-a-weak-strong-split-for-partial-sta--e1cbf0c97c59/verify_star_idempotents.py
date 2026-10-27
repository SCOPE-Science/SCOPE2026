#!/usr/bin/env python3
"""Direct exhaustive check of six star partial-map idempotent spectra.

The value -1 denotes an undefined partial-map value; the center is 0.
Only Python's standard library is required.
"""
from collections import Counter
from itertools import product
from math import comb

KINDS = ("PEnd", "PwEnd", "PsEnd", "PswEnd", "IEnd", "PAut")


def direct(m):
    n = m + 1
    out = {kind: Counter() for kind in KINDS}

    def edge(u, v):
        return u != v and (u == 0 or v == 0)

    for f in product(range(-1, n), repeat=n):
        domain = [u for u, value in enumerate(f) if value != -1]
        image = {f[u] for u in domain}
        if any(v not in domain or f[v] != v for v in image):
            continue
        strict = all(not edge(u, v) or edge(f[u], f[v])
                     for u in domain for v in domain)
        weak = all(not edge(u, v) or f[u] == f[v] or edge(f[u], f[v])
                   for u in domain for v in domain)
        strong = all(edge(u, v) == edge(f[u], f[v])
                     for u in domain for v in domain)
        strong_weak = all((edge(u, v) and f[u] != f[v]) == edge(f[u], f[v])
                          for u in domain for v in domain)
        injective = len(domain) == len(image)
        flags = dict(PEnd=strict, PwEnd=weak, PsEnd=strong,
                     PswEnd=strong_weak, IEnd=strict and injective,
                     PAut=strong and injective)
        for kind in KINDS:
            if flags[kind]:
                out[kind][len(image)] += 1
    return out


def predicted(m):
    A = {r: comb(m, r) * (r + 1) ** (m - r) for r in range(m + 1)}
    B = {r: comb(m, r) * (r + 2) ** (m - r) for r in range(m + 1)}
    result = {kind: Counter() for kind in KINDS}
    for r in range(m + 1):
        a = A[r]
        result["PEnd"][r] += a
        result["PEnd"][r + 1] += a
        result["PsEnd"][r] += a
        result["PsEnd"][r + 1] += a
        result["PwEnd"][r] += a
        result["PwEnd"][r + 1] += B[r]
        result["PswEnd"][r] += a
        result["PswEnd"][r + 1] += a
    result["PwEnd"][1] += m * 2 ** (m - 1)
    result["PswEnd"][1] += 2 ** m - 1 + m * 2 ** (m - 1)
    for r in range(m + 2):
        result["IEnd"][r] = comb(m + 1, r)
        result["PAut"][r] = comb(m + 1, r)
    return result


def main():
    for m in range(1, 7):
        measured = direct(m)
        expected = predicted(m)
        for kind in KINDS:
            assert measured[kind] == expected[kind], (
                m, kind, measured[kind], expected[kind])
        print("m=%d PASS totals=%s" % (
            m, tuple(sum(measured[k].values()) for k in KINDS)))
    print("ALL SIX RANK SPECTRA VERIFIED THROUGH SIX LEAVES")


if __name__ == "__main__":
    main()
