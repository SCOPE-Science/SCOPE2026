#!/usr/bin/env python3
"""Exact rank-three Hintikka types of finite Boolean inclusion posets.

Requires Python 3.9+ standard library. The orbit-based and raw-subset solvers
are independent implementations. The mathematical all-n stabilization is
proved in RESULT.md; a finite program alone is not that proof.
"""
from functools import lru_cache
from itertools import product


def orbit_profiles(rank, largest):
    intern = {}
    def label(s):
        if s not in intern:
            intern[s] = len(intern) + 1
        return intern[s]

    @lru_cache(None)
    def typ(counts, r):
        k = len(counts).bit_length() - 1
        # Counts give sizes of 2^k Venn cells for k selected subsets.
        # Atom i<=j iff there is no base point in Xi minus Xj.
        atom = tuple(not any(c and (mask >> i & 1) and not (mask >> j & 1)
                             for mask, c in enumerate(counts))
                     for i in range(k) for j in range(k))
        if not r:
            return label((0, k, atom))
        children = set()
        for a in product(*(range(c + 1) for c in counts)):
            next_counts = tuple(x - y for x, y in zip(counts, a)) + tuple(a)
            children.add(typ(next_counts, r - 1))
        return label((r, k, atom, frozenset(children)))

    seq = [typ((n,), rank) for n in range(largest + 1)]
    return seq, typ.cache_info(), len(intern)


def direct_profile(n, canon):
    """Exhaust all ordered tuples of actual subsets; no Venn orbit reduction."""
    N = 1 << n
    subset = [[(a & ~b) == 0 for b in range(N)] for a in range(N)]
    def atom3(i, j, k):
        return (subset[i][j], subset[j][i], subset[i][k], subset[k][i],
                subset[j][k], subset[k][j])
    triples = {(i, j, k): canon((0, atom3(i, j, k)))
               for i in range(N) for j in range(N) for k in range(N)}
    pairs = {(i, j): canon((1, subset[i][j], subset[j][i],
                            frozenset(triples[(i, j, k)] for k in range(N))))
             for i in range(N) for j in range(N)}
    singles = [canon((2, frozenset(pairs[(i, j)] for j in range(N))))
               for i in range(N)]
    return canon((3, frozenset(singles)))


def main():
    ids3, info3, nt3 = orbit_profiles(3, 9)
    ids2, info2, nt2 = orbit_profiles(2, 8)
    assert len(set(ids3)) == 7
    assert len(set(ids3[:7])) == 7
    assert ids3[6:] == [ids3[6]] * 4
    assert len(set(ids2)) == 3
    assert ids2[2:] == [ids2[2]] * 7
    catalog = {}
    def canon(key):
        if key not in catalog:
            catalog[key] = len(catalog) + 1
        return catalog[key]
    direct_ids = [direct_profile(n, canon) for n in range(8)]
    assert len(set(direct_ids[:7])) == 7
    assert direct_ids[6] == direct_ids[7]
    assert all((ids3[i] == ids3[j]) == (direct_ids[i] == direct_ids[j])
               for i in range(8) for j in range(8))
    # Check the local two-branch splitting lemma at the thresholds used by
    # the symbolic Ehrenfeucht-Fraisse proof (bounded sanity check only).
    split_cases = 0
    for t in [1, 2, 4]:
        for c in range(2*t, 4*t+6):
            for d in range(2*t, 4*t+6):
                for a in range(c+1):
                    b = c - a
                    ok = any(((a == x) or (a >= t and x >= t)) and
                             ((b == d-x) or (b >= t and d-x >= t))
                             for x in range(d+1))
                    assert ok, (t,c,d,a)
                    split_cases += 1
    print('rank3_class_ids_n0_to_n9', ids3)
    print('rank2_class_ids_n0_to_n8', ids2)
    print('raw_rank3_ids_n0_to_n7', direct_ids)
    print('orbit_states_rank3', info3.misses, 'types', nt3)
    print('raw_types',len(catalog),'local_splitting_cases',split_cases)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
