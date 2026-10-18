"""Finite independent zero-forcing check for adjacent hard-core configurations.

This is a finite sanity check, not a substitute for the general proof.
Run: python3 verify_adjacent42.py
"""
from itertools import combinations


def token_neighbours(config, n):
    occupied = set(config)
    ans = set()
    for vertex in occupied:
        for dest in ((vertex - 1) % n, (vertex + 1) % n):
            if dest not in occupied:
                ans.add(tuple(sorted((occupied - {vertex}) | {dest})))
    return ans


def is_adjacent(config, n):
    occupied = set(config)
    return any((vertex + 1) % n in occupied for vertex in occupied)


def zero_force(n, k):
    vertices = list(combinations(range(n), k))
    neighbours = {v: token_neighbours(v, n) for v in vertices}
    blue = {v for v in vertices if is_adjacent(v, n)}
    initial_blue = len(blue)
    rounds = 0
    while len(blue) < len(vertices):
        new = set()
        for v in blue:
            remaining = neighbours[v] - blue
            if len(remaining) == 1:
                new.update(remaining)
        if not new:
            break
        blue.update(new)
        rounds += 1
    return len(vertices), initial_blue, len(vertices) - len(blue), rounds


def main():
    examined = 0
    for n in range(5, 17):
        for k in range(3, min(6, n)):
            total, blue, missed, rounds = zero_force(n, k)
            print(f'N={n:2d} k={k} states={total:5d} initial={blue:5d} remaining={missed:3d} rounds={rounds:2d}')
            assert missed == 0, (n, k, missed)
            examined += 1
    for n in range(5, 13):
        total, blue, missed, rounds = zero_force(n, 2)
        assert missed > 0 and rounds == 0, (n, 2, missed)
    print(f'PASS: {examined} k>=3 finite token graphs; eight k=2 boundary checks')


if __name__ == '__main__':
    main()
