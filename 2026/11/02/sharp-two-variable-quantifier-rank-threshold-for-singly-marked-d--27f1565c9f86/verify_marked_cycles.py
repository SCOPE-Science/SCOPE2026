"""Exact FO2 successor/marker rank profiles; two independent recurrences.
Usage: python3 verify_marked_cycles.py
"""
from collections import defaultdict

MAX_N = 24
MAX_Q = 8
NS = tuple(range(3, MAX_N + 1))


def pair_atom(n, a, b):
    return (a == b, (a + 1) % n == b, (b + 1) % n == a)


def unary_support():
    colors = {(n, x): int(x == 0) for n in NS for x in range(n)}
    records = []
    for r in range(MAX_Q):
        palettes = {n: frozenset(colors[n, x] for x in range(n)) for n in NS}
        records.append(palettes)
        nxt = {}
        for n in NS:
            for x in range(n):
                supports = frozenset((pair_atom(n, x, y), colors[n, y]) for y in range(n))
                nxt[n, x] = (colors[n, x], supports)
        ids = {v: i for i, v in enumerate(set(nxt.values()))}
        colors = {k: ids[v] for k, v in nxt.items()}
    return records


def full_formula_types():
    assignments = {n: [(a, b) for a in (-1, *range(n)) for b in (-1, *range(n))] for n in NS}
    types = {}
    for n in NS:
        for a, b in assignments[n]:
            types[n, a, b] = (
                a != -1, b != -1, a == 0 if a != -1 else False,
                b == 0 if b != -1 else False, a == b if a >= 0 and b >= 0 else False,
                (a + 1) % n == b if a >= 0 and b >= 0 else False,
                (b + 1) % n == a if a >= 0 and b >= 0 else False,
            )
    out = []
    for q in range(MAX_Q + 1):
        ids0 = {v: i for i, v in enumerate(set(types.values()))}
        out.append({n: ids0[types[n, -1, -1]] for n in NS})
        if q == MAX_Q: break
        # Exact logical-type recursion: all existential extensions and their negations.
        ids = {v: i for i, v in enumerate(set(types.values()))}
        compressed = {key: ids[v] for key, v in types.items()}
        nxt = {(n, a, b): (
            compressed[n, a, b],
            frozenset(compressed[n, z, b] for z in range(n)),
            frozenset(compressed[n, a, z] for z in range(n))
        ) for n in NS for a, b in assignments[n]}
        idsn = {v: i for i, v in enumerate(set(nxt.values()))}
        types = {k: idsn[v] for k, v in nxt.items()}
    return out


def equality_matrix(signature):
    return {(m, n): signature[m] == signature[n] for m in NS for n in NS}


def main():
    unary = unary_support()
    full = full_formula_types()
    for q in range(1, MAX_Q + 1):
        prediction = {(m,n): (m==n or (m>=2*q+1 and n>=2*q+1)) for m in NS for n in NS}
        a = equality_matrix(unary[q-1])
        b = equality_matrix(full[q])
        assert a == prediction, ('unary', q)
        assert b == prediction, ('full', q)
        print(f'q={q}: {2*q-1} classes; stable length={2*q+1}; two recurrences agree')
    print(f'VERIFIED: {MAX_Q * len(NS)**2} pair/rank comparisons, by both independent algorithms')

if __name__ == '__main__': main()
