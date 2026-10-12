#!/usr/bin/env python3
from functools import lru_cache
from itertools import product
from math import ceil


def star_edges(signs):
    # Vertex 0 is the centre; leaf i has edge sign signs[i-1].
    return {(0, i + 1): signs[i] for i in range(len(signs))}


def spread(state, signs):
    n = len(state)
    out = list(state)
    for v in range(n):
        if state[v] != 0:
            continue
        influence = 0
        if v == 0:
            for leaf in range(1, n):
                influence += signs[leaf - 1] * state[leaf]
        else:
            influence = signs[v - 1] * state[0]
        if influence > 0:
            out[v] = 1
        elif influence < 0:
            out[v] = -1
    return tuple(out)


def reachable_final_colours(signs):
    n = len(signs) + 1

    @lru_cache(maxsize=None)
    def rec(state):
        after = spread(state, signs)
        if all(x != 0 for x in after):
            return frozenset((after,))
        ans = set()
        for v, x in enumerate(after):
            if x == 0:
                for colour in (-1, 1):
                    nxt = list(after)
                    nxt[v] = colour
                    ans.update(rec(tuple(nxt)))
        return frozenset(ans)

    return rec((0,) * n)


def plurality_direct(signs):
    finals = reachable_final_colours(signs)
    return max(max(sum(x == 1 for x in f), sum(x == -1 for x in f)) for f in finals)


def plurality_formula(signs):
    m = len(signs)
    p = sum(s == 1 for s in signs)
    q = m - p
    if p == 0:
        return m
    if q == 0:
        return m + 1
    return max(p + 2, q + 1)


def main():
    signature_cases = 0
    final_colourings = 0
    minima = {}
    for m in range(3, 9):
        best = m + 1
        for signs in product((-1, 1), repeat=m):
            direct = plurality_direct(signs)
            formula = plurality_formula(signs)
            if direct != formula:
                raise AssertionError((m, signs, direct, formula))
            signature_cases += 1
            final_colourings += len(reachable_final_colours(signs))
            best = min(best, direct)
        expected = ceil((m + 3) / 2)
        if best != expected:
            raise AssertionError(('switching minimum', m, best, expected))
        minima[m] = best

    # Algebraic boundary checks well beyond the exhaustive simulation range.
    for m in range(3, 501):
        values = []
        for p in range(m + 1):
            signs = (1,) * p + (-1,) * (m - p)
            values.append(plurality_formula(signs))
        if min(values) != ceil((m + 3) / 2):
            raise AssertionError(('large switching minimum', m))

    print('ALL CHECKS PASSED')
    print(f'exhaustive_star_signatures={signature_cases}')
    print(f'reachable_final_colourings_checked={final_colourings}')
    print('exhaustive_leaf_range=3..8')
    print('switching_minimum_formula_range=3..500')
    print('small_switching_minima=' + ','.join(f'{m}:{minima[m]}' for m in sorted(minima)))


if __name__ == '__main__':
    main()
