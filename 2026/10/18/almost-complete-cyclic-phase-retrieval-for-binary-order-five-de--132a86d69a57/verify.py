#!/usr/bin/env python3
"""Independent exhaustive checks for order-five de Bruijn cyclic homometry.

Run next to cycles.csv and ambiguities.csv using only the Python standard library.
All counts are integer-exact. The two cycle generators use independent
search spaces; the three correlation formulas use different primitives.
"""
import csv
from collections import Counter, defaultdict
from pathlib import Path

N = 32

def canonical(s):
    assert len(s) == N and set(s) <= {'0', '1'}
    zero_starts = [i for i in range(N) if all(s[(i+j) % N] == '0' for j in range(5))]
    assert len(zero_starts) == 1
    i = zero_starts[0]
    return s[i:] + s[:i]


def valid(s):
    return len(s) == N and len({''.join(s[(i+j) % N] for j in range(5))
                                    for i in range(N)}) == N


def cycles_by_euler():
    # Every Eulerian tour contains edge 00000 exactly once; anchor it first.
    answer = set()
    def dfs(vertex, used, trace):
        if len(trace) == N:
            if vertex == 0:
                s = ''.join(str(edge & 1) for edge in trace)
                answer.add(canonical(s))
            return
        for e in (2*vertex, 2*vertex+1):
            if not (used & (1 << e)):
                dfs(e & 15, used | (1 << e), trace + [e])
    dfs(0, 1, [0])
    return answer


def cycles_by_pairings():
    # Every Euler circuit determines one of two bijections at each vertex
    # between incoming edges v,v+16 and outgoing edges 2v,2v+1.
    answer = set()
    for mask in range(1 << 16):
        next_edge = [0]*N
        for v in range(16):
            z = (mask >> v) & 1
            next_edge[v] = 2*v + z
            next_edge[v+16] = 2*v + 1-z
        seen = 0
        path = []
        e = 0
        for _ in range(N):
            if seen & (1 << e):
                break
            seen |= 1 << e
            path.append(e)
            e = next_edge[e]
        if len(path) == N and e == 0:
            s = ''.join(str(edge & 1) for edge in path)
            answer.add(canonical(s))
    return answer


def correlation_products(s):
    values = [1 if digit == '1' else -1 for digit in s]
    return tuple(sum(values[j]*values[(j+t) % N] for j in range(N))
                 for t in range(1, 17))


def correlation_differences(s):
    ones = {i for i, bit in enumerate(s) if bit == '1'}
    k = len(ones)
    return tuple(N-4*k+4*sum((j+t) % N in ones for j in ones)
                 for t in range(1, 17))


def correlation_popcount(s):
    v = sum((bit == '1') << i for i, bit in enumerate(s))
    mask = (1 << N)-1
    return tuple(N-2*(v ^ ((v >> t) | (v << (N-t)) & mask)).bit_count()
                 for t in range(1,17))


def dihedral_class(s):
    transformed = [s, s[::-1], ''.join('1' if b == '0' else '0' for b in s),
                   ''.join('1' if b == '0' else '0' for b in s[::-1])]
    return frozenset(canonical(t) for t in transformed)


def main():
    from_dfs = cycles_by_euler()
    from_pairs = cycles_by_pairings()
    assert len(from_dfs) == 2048 and from_dfs == from_pairs
    assert all(valid(s) for s in from_dfs)
    corr = {}
    orbit_rep = {}
    orb_members = defaultdict(set)
    for s in sorted(from_dfs):
        a, b, c = correlation_products(s), correlation_differences(s), correlation_popcount(s)
        assert a == b == c
        assert a[:4] == (0,0,0,0)
        corr[s] = a
        orbit = dihedral_class(s)
        assert orbit <= from_dfs
        rep = min(orbit)
        orbit_rep[s] = rep
        orb_members[rep].add(s)
        assert len(orbit) in (2, 4)
    assert len(orb_members) == 528
    assert Counter(map(len, orb_members.values())) == Counter({2:32, 4:496})
    fibers = defaultdict(list)
    for s, signature in corr.items():
        fibers[signature].append(s)
    assert len(fibers) == 526
    assert Counter(map(len, fibers.values())) == Counter({2:30, 4:495, 8:1})
    detailed = Counter((len(f), len(set(orbit_rep[s] for s in f)))
                       for f in fibers.values())
    assert detailed == Counter({(2,1):30, (4,1):494, (4,2):1, (8,2):1})
    distinct_prefixes = {t:len({v[:t] for v in fibers}) for t in range(1,17)}
    assert distinct_prefixes == {1:1,2:1,3:1,4:1,5:4,6:23,7:92,8:236,
                                 9:408,10:484,11:514,12:521,13:526,
                                 14:526,15:526,16:526}
    ambiguous = []
    for sig,f in fibers.items():
        reps = sorted({orbit_rep[s] for s in f})
        if len(reps) == 2:
            ambiguous.append((len(f), tuple(sig), tuple(reps),
                              tuple(len(orb_members[r]) for r in reps)))
    ambiguous.sort()
    assert [(n, sizes) for n,_,_,sizes in ambiguous] == [(4,(2,2)),(8,(4,4))]
    # A literal data table is compared against newly generated objects, not
    # trusted as an input to the enumeration or to the correlation checks.
    p = Path(__file__).resolve().parent
    with (p/'cycles.csv').open(newline='', encoding='utf-8') as fp:
        table = list(csv.DictReader(fp))
    assert len(table) == 2048 and len({row['cycle'] for row in table}) == 2048
    sig_index = {sig:i+1 for i,sig in enumerate(sorted(fibers))}
    for row in table:
        s = row['cycle']
        assert s in from_dfs
        assert row['orbit_representative'] == orbit_rep[s]
        assert int(row['orbit_size']) == len(orb_members[orbit_rep[s]])
        assert int(row['signature_id']) == sig_index[corr[s]]
        assert int(row['fiber_size']) == len(fibers[corr[s]])
        assert int(row['fiber_orbits']) == len({orbit_rep[v] for v in fibers[corr[s]]})
        assert tuple(int(row[f'R{t}']) for t in range(1,17)) == corr[s]
    with (p/'ambiguities.csv').open(newline='', encoding='utf-8') as fp:
        atable = list(csv.DictReader(fp))
    assert len(atable) == 2
    for row,(n,sig,reps,sizes) in zip(sorted(atable,key=lambda x:int(x['fiber_size'])),ambiguous):
        assert int(row['fiber_size']) == n
        assert row['orbit_A'] == reps[0] and row['orbit_B'] == reps[1]
        assert int(row['orbit_size_A']) == sizes[0] and int(row['orbit_size_B']) == sizes[1]
        assert tuple(int(x) for x in row['signature'].split(',')) == sig
    print('VERIFY_OK generators=2 pairings=65536 cycles=2048 rooted_windows=65536')
    print('VERIFY_OK correlation_formulas=3 independent_shifts=16 autocorrelation_signatures=526')
    print('VERIFY_OK bracelets=528 bracelet_sizes=2:32,4:496')
    print('VERIFY_OK full_fibers=2:30,4:495,8:1 nontrivial_fibers=2')
    print('VERIFY_OK homometric_anomalies=4:two_size2_orbits,8:two_size4_orbits')
    print('VERIFY_OK cutoff_lag12_signatures=521 cutoff_lag13_signatures=526')
    print('VERIFY_OK csv_cycles=2048 csv_ambiguities=2')

if __name__ == '__main__':
    main()
