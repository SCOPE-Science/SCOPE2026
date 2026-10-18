"""Self-contained finite-ring checks for the Artinian coprime-ideal classification.

All tests use the original ideal-coproduct definition, without assuming
classification or local-socle conclusions. Run: python verify_coprime_artinian.py
"""
from itertools import product
from math import prod


def algebra(name, basis_products):
    d = len(basis_products)
    N = 1 << d
    assert all(len(row) == d for row in basis_products)
    def mul(a, b):
        out = 0
        for i in range(d):
            if a & (1 << i):
                for j in range(d):
                    if b & (1 << j):
                        k = basis_products[i][j]
                        if k is not None:
                            out ^= 1 << k
        return out
    assert all(mul(1, a) == a and mul(a, 1) == a for a in range(N))
    for a, b, c in product(range(N), repeat=3):
        assert mul(mul(a, b), c) == mul(a, mul(b, c))
    zero = frozenset([0])
    spaces = {zero}
    frontier = [zero]
    while frontier:
        S = frontier.pop()
        for x in range(1, N):
            if x in S:
                continue
            T = frozenset(list(S) + [a ^ x for a in S])
            if T not in spaces:
                spaces.add(T)
                frontier.append(T)
    ideals = sorted(
        [S for S in spaces if all(mul(r, a) in S for r in range(N) for a in S)],
        key=lambda S: (len(S), sorted(S)),
    )
    ann = {}
    for I in ideals:
        ann[I] = frozenset(r for r in range(N) if all(mul(r, a) == 0 for a in I))
        assert ann[I] in ideals
    def prod_subset(C, A, J):
        return all(mul(c, a) in J for c in C for a in A)
    coprime = []
    for C in ideals:
        if C == zero:
            continue
        if all((C <= I or C <= J or not prod_subset(C, ann[I], J))
               for I in ideals for J in ideals):
            coprime.append(C)
    m = frozenset(range(0, N, 2))
    soc = ann[m]
    assert m in ideals
    expected = [soc] if len(soc) == 2 else []
    assert coprime == expected, (name, coprime, expected)
    return {'name': name, 'ideals': ideals, 'coprime': coprime,
            'socdim': (len(soc).bit_length() - 1), 'ann': ann, 'mul': mul}


def table(d, pair_dict):
    t = [[None for j in range(d)] for i in range(d)]
    for i in range(d):
        t[0][i] = t[i][0] = i
    for (i,j), k in pair_dict.items():
        t[i][j] = t[j][i] = k
    return t

rings = [
    algebra('F2', table(1, {})),
    algebra('dual_numbers', table(2, {})),
    algebra('truncated_cubic', table(3, {(1,1):2})),
    algebra('truncated_quartic', table(4, {(1,1):2,(1,2):3})),
    algebra('square_zero_two', table(3, {})),
    algebra('square_zero_three', table(4, {})),
    algebra('Gorenstein_bivariate_CI', table(4, {(1,2):3})),
]

def check_product(factors):
    pools = [R['ideals'] for R in factors]
    ideals = list(product(*pools))
    zero = tuple(frozenset([0]) for _ in factors)
    def contained(C, I):
        return all(c <= i for c, i in zip(C,I))
    def incop(C, I, J):
        return all(all(R['mul'](c,a) in j for c in cc for a in R['ann'][ii])
                   for R, cc, ii, j in zip(factors,C,I,J))
    cp = []
    for C in ideals:
        if C == zero:
            continue
        if all(contained(C, I) or contained(C, J) or not incop(C,I,J)
               for I in ideals for J in ideals):
            cp.append(C)
    expect = []
    for i,R in enumerate(factors):
        for C in R['coprime']:
            V = list(zero)
            V[i] = C
            expect.append(tuple(V))
    assert set(cp) == set(expect), ([r['name'] for r in factors],len(cp),len(expect))
    # Topology: all subsets of the spectrum occur among closed V_c(I).
    closed = {frozenset(i for i,C in enumerate(cp) if contained(C,I)) for I in ideals}
    assert len(closed) == 2 ** len(cp), ([r['name'] for r in factors],len(closed))
    return len(ideals), len(cp)

samples = [[rings[i]] for i in range(len(rings))]
samples += [[rings[i],rings[j]] for i,j in [(0,0),(0,4),(4,4),(2,4),(3,5),(6,4),(6,6)]]
samples += [[rings[i] for i in ii] for ii in [(0,2,4),(0,6,5),(0,2,6)]]
for fac in samples:
    n,c = check_product(fac)
    print('+'.join(r['name'] for r in fac), 'ideals=',n,'coprime=',c)
print('VERIFY_OK',len(samples),'Artinian examples, all ideals tested')
