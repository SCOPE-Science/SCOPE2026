#!/usr/bin/env python3
"""Finite verification for acyclic signatures of K_n minus a matching."""

from itertools import permutations
from math import factorial


def signature(n: int, r: int):
    missing = {(2*i, 2*i+1) for i in range(r)}
    edges = [(u, v) for u in range(n) for v in range(u+1, n)
             if (u, v) not in missing]
    seen = set()
    for order in permutations(range(n)):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        mask = 0
        for j, (u, v) in enumerate(edges):
            if pos[u] > pos[v]:
                mask |= 1 << j
        seen.add(mask)
    sig = sum(-1 if mask.bit_count() % 2 else 1 for mask in seen)
    return len(seen), sig


def predicted(n: int, r: int) -> int:
    s = n - 2*r
    if s == 0:
        return (-1)**(r//2) * factorial(r)
    if s == 1 and r % 2 == 0:
        return (-1)**(r//2) * factorial(r)
    return 0


def main():
    checked = 0
    print("n r acyclic_orientations signature predicted")
    for n in range(2, 10):
        for r in range(n//2 + 1):
            count, sig = signature(n, r)
            pred = predicted(n, r)
            assert sig == pred, (n, r, sig, pred)
            checked += 1
            print(n, r, count, sig, pred)
    print(f"PASS: {checked} parameter pairs checked for 2 <= n <= 9.")


if __name__ == "__main__":
    main()
