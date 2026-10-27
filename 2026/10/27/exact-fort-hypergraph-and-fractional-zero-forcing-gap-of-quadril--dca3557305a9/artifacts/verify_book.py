"""Reproduce finite tests for forts and minimum zero forcing on square-page book graphs.
Uses only the Python standard library; the mathematical assertions for all r use separate proofs.
"""
from itertools import combinations, product
from math import comb
from fractions import Fraction


def adjacency(r):
    n = 2*r + 2
    out = [0]*n
    def edge(x, y):
        out[x] |= 1 << y
        out[y] |= 1 << x
    edge(0, 1)
    for i in range(r):
        a = 2 + 2*i
        b = a + 1
        edge(0, a)
        edge(a, b)
        edge(b, 1)
    return out


def is_fort(mask, neighborhoods):
    if mask == 0:
        return False
    for v, neighbors in enumerate(neighborhoods):
        if not (mask >> v & 1) and (neighbors & mask).bit_count() == 1:
            return False
    return True


def is_zero_forcing(mask, neighborhoods):
    n = len(neighborhoods)
    target = (1 << n) - 1
    while True:
        gained = 0
        for v, neighbors in enumerate(neighborhoods):
            if mask >> v & 1:
                remaining = neighbors & ~mask
                if remaining.bit_count() == 1:
                    gained |= remaining
        if gained == 0:
            return mask == target
        mask |= gained


def minimal_fort_candidates(r):
    out = set()
    for i, j in combinations(range(r), 2):
        out.add(sum(3 << (2+2*k) for k in (i,j)))
    out.add(1 + sum(1 << (3+2*i) for i in range(r)))
    out.add(2 + sum(1 << (2+2*i) for i in range(r)))
    for choices in product(range(2), repeat=r):
        if len(set(choices)) > 1:
            out.add(3 + sum(1 << (2+2*i+v) for i,v in enumerate(choices)))
    return out


def minimum_forcing_candidates(r):
    out = set()
    for doubled in range(r):
        for omitted in range(r):
            if doubled == omitted:
                continue
            others = [i for i in range(r) if i not in (doubled, omitted)]
            for choices in product(range(2), repeat=len(others)):
                out.add((3 << (2+2*doubled)) +
                        sum(1 << (2+2*i+v) for i,v in zip(others,choices)))
    for hub in (0,1):
        for omitted in range(r):
            others = [i for i in range(r) if i != omitted]
            for choices in product(range(2), repeat=len(others)):
                if hub not in choices:  # opposite-spine fort must be met
                    continue
                out.add((1 << hub) +
                        sum(1 << (2+2*i+v) for i,v in zip(others,choices)))
    return out


def main():
    examined_fort_subsets = 0
    examined_zf_subsets = 0
    for r in range(2,8):
        adj = adjacency(r)
        n = len(adj)
        candidates = minimal_fort_candidates(r)
        expected = comb(r,2) + 2**r
        assert len(candidates) == expected, (r,'count minimal candidates')
        for fort in candidates:
            assert is_fort(fort,adj), (r,'candidate not a fort',fort)
            sub = (fort-1)&fort
            while sub:
                assert not is_fort(sub,adj), (r,'candidate not minimal',fort,sub)
                sub=(sub-1)&fort
        for mask in range(1,1<<n):
            examined_fort_subsets += 1
            if is_fort(mask,adj):
                assert any((f&mask)==f for f in candidates), (r,'unlisted minimal fort',mask)
        expected_min_forcing = minimum_forcing_candidates(r)
        expected_count = r*((r+3)*2**(r-2)-2)
        assert len(expected_min_forcing)==expected_count,(r,'candidate forcing count')
        for k in range(r+1):
            for subset in combinations(range(n),k):
                examined_zf_subsets+=1
                mask=sum(1<<x for x in subset)
                forcing=is_zero_forcing(mask,adj)
                assert forcing == (mask in expected_min_forcing), (r,'forcing mismatch',mask,k)
        print(f'r={r} |V|={n} minimal_forts={len(candidates)} Z={r} minimum_Z_sets={len(expected_min_forcing)}')
    # Exact rational primal feasibility for every fort type; the text supplies matching lower bounds.
    for r in range(2,31):
        t=Fraction(1,4)
        h=max(Fraction(0),1-r*t)
        assert 4*t>=1 and h+r*t>=1 and 2*h+r*t>=1
        assert 2*h+2*r*t == max(Fraction(2),Fraction(r,2))
    print(f'EXHAUSTIVE_FORT_SUBSETS={examined_fort_subsets}')
    print(f'EXHAUSTIVE_MINIMUM_Z_SUBSETS={examined_zf_subsets}')
    print('LP_PRIMAL_RATIONAL_CASES=29')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
