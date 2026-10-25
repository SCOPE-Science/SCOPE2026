#!/usr/bin/env python3
"""Exact small-cycle checks for single-peaked jump Schelling integration."""
from fractions import Fraction
from itertools import combinations


def utility(colors, vertex):
    if colors[vertex] == '.':
        raise ValueError('unoccupied vertex')
    n = len(colors)
    occupied = [colors[j] for j in ((vertex - 1) % n, (vertex + 1) % n)
                if colors[j] != '.']
    f = Fraction(1 + occupied.count(colors[vertex]), 1 + len(occupied))
    return 2 * min(f, 1 - f)


def integration(colors):
    n = len(colors)
    return sum(colors[i] != '.' and any(
        colors[(i + d) % n] not in ('.', colors[i]) for d in (-1, 1))
        for i in range(n))


def evaluate(r, b):
    n = r + b + 1
    min_ne, max_global, states = None, -1, 0
    for vacancy in range(n):
        occupied = [v for v in range(n) if v != vacancy]
        for blues in combinations(occupied, b):
            colors = ['R'] * n
            colors[vacancy] = '.'
            for j in blues:
                colors[j] = 'B'
            states += 1
            score = integration(colors)
            max_global = max(max_global, score)
            is_equilibrium = True
            for i in occupied:
                before = utility(colors, i)
                after = colors[:]
                after[vacancy], after[i] = after[i], '.'
                if utility(after, vacancy) > before:
                    is_equilibrium = False
                    break
            if is_equilibrium:
                min_ne = score if min_ne is None else min(min_ne, score)
    return min_ne, max_global, states


def main():
    cases = 0
    examined = 0
    for r in range(1, 10):
        for b in range(1, r + 1):
            if r + b > 15:
                continue
            observed_ne, observed_opt, states = evaluate(r, b)
            predicted_ne = 2 if r == b == 1 else b + (b + 1) // 2 + 1
            predicted_opt = min(r + b, 3 * b)
            assert observed_ne == predicted_ne, (r, b, observed_ne, predicted_ne)
            assert observed_opt == predicted_opt, (r, b, observed_opt, predicted_opt)
            cases += 1
            examined += states
    print('PASS:', cases, 'color-count pairs,', examined, 'placements checked')


if __name__ == '__main__':
    main()
