"""Finite checks for atom-marked disjointness modal models.

Run: python3 verify.py
The unrestricted classification is proved separately; these are finite cross-checks.
"""
from collections import defaultdict


def analytic_type(n, mask):
    s = mask.bit_count()
    if n == 1:
        return 'A'  # the unique state is both atom and top
    if s == n:
        return 'E'  # top, not an atom
    if s == 1:
        return {2: 'B', 3: 'C'}.get(n, 'D')
    if s == n - 1:
        return 'F' if n == 3 else 'G'
    return 'H'


EXPECTED_SUCCESSORS = {
    'A': set(),
    'B': {'B'},
    'C': {'C', 'F'},
    'D': {'D', 'G', 'H'},
    'E': set(),
    'F': {'C'},
    'G': {'D'},
    'H': {'D', 'H'},
}


# Formulas: ('p',), ('top',), ('not',phi), ('and',phi,psi), ('dia',phi).
def P(): return ('p',)
def TOP(): return ('top',)
def NOT(a): return ('not', a)
def AND(*fs):
    x = fs[0]
    for f in fs[1:]:
        x = ('and', x, f)
    return x

def DIA(a): return ('dia', a)

J = DIA(AND(NOT(P()), DIA(NOT(P()))))
CHARACTERISTICS = {
    'A': AND(P(), NOT(DIA(TOP()))),
    'B': AND(P(), DIA(TOP()), NOT(DIA(NOT(P())))),
    'C': AND(P(), DIA(NOT(P())), NOT(J)),
    'D': AND(P(), J),
    'E': AND(NOT(P()), NOT(DIA(TOP()))),
    'F': AND(NOT(P()), DIA(P()), NOT(DIA(NOT(P()))), NOT(DIA(J))),
    'G': AND(NOT(P()), DIA(P()), NOT(DIA(NOT(P()))), DIA(J)),
    'H': AND(NOT(P()), DIA(NOT(P()))),
}


def depth(f):
    op = f[0]
    if op in ('p', 'top'):
        return 0
    if op == 'dia':
        return depth(f[1]) + 1
    if op == 'not':
        return depth(f[1])
    return max(depth(f[1]), depth(f[2]))


def run():
    points = []
    succ = {}
    for n in range(1, 10):
        for s in range(1, 1 << n):
            v = (n, s)
            points.append(v)
            succ[v] = [(n, t) for t in range(1, 1 << n) if not(s & t)]
    assert len(points) == sum((1 << n) - 1 for n in range(1, 10))
    typ = {v: analytic_type(*v) for v in points}
    bytype = defaultdict(list)
    for v, t in typ.items():
        bytype[t].append(v)
        got = {typ[w] for w in succ[v]}
        assert got == EXPECTED_SUCCESSORS[t], (v, t, got)
    assert set(bytype) == set(EXPECTED_SUCCESSORS)

    # Direct Kripke semantics: no quotient is used in evaluating these formulas.
    cache = {}
    def sat(v, f):
        key = (v, f)
        if key in cache:
            return cache[key]
        op = f[0]
        if op == 'p': result = v[1].bit_count() == 1
        elif op == 'top': result = True
        elif op == 'not': result = not sat(v, f[1])
        elif op == 'and': result = sat(v, f[1]) and sat(v, f[2])
        elif op == 'dia': result = any(sat(w, f[1]) for w in succ[v])
        else: raise AssertionError(f)
        cache[key] = result
        return result

    formula_checks = 0
    for v in points:
        for name, formula in CHARACTERISTICS.items():
            assert sat(v, formula) == (typ[v] == name), (v, name)
            formula_checks += 1
    assert max(map(depth, CHARACTERISTICS.values())) == 3

    # Independent depth-limited modal equivalence signatures by forward refinement.
    rank = {v: int(v[1].bit_count() == 1) for v in points}
    counts = [len(set(rank.values()))]
    levels = [rank]
    for d in range(1, 5):
        signatures = {v: (rank[v], tuple(sorted({rank[w] for w in succ[v]})))
                      for v in points}
        ids = {s: i for i, s in enumerate(sorted(set(signatures.values()), key=str))}
        rank = {v: ids[signatures[v]] for v in points}
        levels.append(rank)
        counts.append(len(ids))
    assert counts == [2, 6, 7, 8, 8], counts
    assert [2 ** x for x in counts] == [4, 64, 128, 256, 256]
    for a in points:
        for b in points:
            assert (levels[3][a] == levels[3][b]) == (typ[a] == typ[b])
    # Least depth is genuinely 3: the two coatom sorts have the same depth-2 type.
    x, y = (3, 0b011), (4, 0b0111)
    assert typ[x] == 'F' and typ[y] == 'G'
    assert levels[2][x] == levels[2][y]
    assert levels[3][x] != levels[3][y]

    print('ATOM_DISJOINTNESS_VERIFY_OK',
          'finite_models=9',
          f'worlds={len(points)}',
          f'characteristic_semantics={formula_checks}',
          'depth_classes=2,6,7,8,8',
          'formula_classes=4,64,128,256,256',
          'all_successor_profiles=true',
          'sharp_depth=3')


if __name__ == '__main__':
    run()
