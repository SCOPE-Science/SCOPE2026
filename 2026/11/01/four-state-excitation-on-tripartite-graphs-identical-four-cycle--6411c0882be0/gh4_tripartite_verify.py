#!/usr/bin/env python3
"""Exact finite-state certificate for four-state excitation on K_{a,b,c}.

No external libraries, network services, or archived data are used.
Python 3.8+ is sufficient.  All labeled configurations in the listed
finite graph sizes are independently simulated vertex by vertex.
"""
from collections import Counter
from itertools import product, permutations
from math import comb

COLORS = tuple(range(4))
SUPPORTS = range(1, 16)
STATE_SET = tuple(product(SUPPORTS, repeat=3))


def next_support(s):
    result = []
    for i, mask in enumerate(s):
        excite = any(s[j] & 2 for j in range(3) if j != i)
        newmask = 0
        for c in COLORS:
            if mask & (1 << c):
                newmask |= 1 << ((c + 1) % 4 if c else int(excite))
        result.append(newmask)
    return tuple(result)


def one_step_tags(colors):
    """One representative of every initially occupied color on each shore."""
    excite = [any(1 in colors[j] for j in range(3) if j != i) for i in range(3)]
    return tuple(tuple((c + 1) % 4 if c else int(excite[i]) for c in colors[i])
                 for i in range(3))


def tagged_initial(s):
    return tuple(tuple(c for c in COLORS if s[i] & (1 << c)) for i in range(3))


def profiles(s, horizon=10):
    x = tagged_initial(s)
    seq = [x]
    for _ in range(horizon):
        x = one_step_tags(x)
        seq.append(x)
    return seq


def support_of(x):
    masks = []
    for colors in x:
        mask = 0
        for c in colors: mask |= 1 << c
        masks.append(mask)
    return tuple(masks)


def onto(j, n):
    return sum((-1)**i * comb(j, i) * (j - i)**n for i in range(j + 1))


def coeff_table(S):
    C = Counter(tuple(sorted(m.bit_count() for m in s)) for s in S)
    result = {}
    for cardinalities in sorted(C):
        vals = {sum(tuple(m.bit_count() for m in s) == pp for s in S)
                for pp in set(permutations(cardinalities))}
        assert len(vals) == 1, (cardinalities, vals)
        result[cardinalities] = vals.pop()
    return result


def total_from_table(table, a, b, c):
    U = [None] + [[onto(j, n) for n in (a,b,c)] for j in range(1,5)]
    return sum(v * sum(U[i][0]*U[j][1]*U[k][2]
                       for i,j,k in set(permutations(t)))
               for t,v in table.items())


def cyclic_contact_step(x):
    # Independent four-color successor-contact cellular automaton.
    out = []
    for i, shore in enumerate(x):
        neighbors = {c for j, y in enumerate(x) if j != i for c in y}
        out.append(tuple(((c+1) % 4 if (c+1) % 4 in neighbors else c)
                         for c in shore))
    return tuple(out)


def cyclic_contact_profile(s):
    x = tagged_initial(s)
    out = [x]
    for _ in range(7):
        x = cyclic_contact_step(x)
        out.append(x)
    return out


def micro_step(x):
    active = [1 in shore for shore in x]
    return tuple(tuple((c+1) % 4 if c else int(any(active[j] for j in range(3) if j != i))
                       for c in shore)
                 for i, shore in enumerate(x))


def direct_counts(a,b,c):
    count_fixed = count_period4 = extinction = 0
    depths = Counter()
    for flat in product(COLORS, repeat=a+b+c):
        x = (flat[:a], flat[a:a+b], flat[a+b:])
        orbit = [x]
        for _ in range(10): orbit.append(micro_step(orbit[-1]))
        assert orbit[10] == orbit[6]
        t = next(t for t in range(7) if orbit[t] == orbit[t+4])
        depths[t] += 1
        y = orbit[t]
        if micro_step(y) == y:
            assert all(c == 0 for shore in y for c in shore)
            if t == 0: count_fixed += 1
            extinction += 1
        else:
            assert orbit[t+2] != y
            if t == 0: count_period4 += 1
    return count_fixed,count_period4,extinction,depths


def main():
    assert len(STATE_SET) == 15**3 == 3375
    periodic,extinct = [],[]
    depth_hist = Counter()
    matching_primitive_orbits = 0
    for s in STATE_SET:
        history = profiles(s)
        for k in range(10):
            assert support_of(history[k+1]) == next_support(s if k == 0 else support_of(history[k]))
        assert history[10] == history[6], (s, history)
        cca = cyclic_contact_profile(s)
        assert cca[7] == cca[3], s
        gh_primitive = (history[4] == history[0] and history[1] != history[0])
        cca_primitive = (cca[4] == cca[0] and cca[1] != cca[0])
        assert gh_primitive == cca_primitive, s
        if gh_primitive:
            assert history[1] == cca[1], s  # identical successor on the full orbit
            matching_primitive_orbits += 1
        entry = next(t for t in range(7) if history[t] == history[t+4])
        depth_hist[entry] += 1
        if entry == 0: periodic.append(s)
        if all(c == 0 for shore in history[6] for c in shore): extinct.append(s)
        if entry == 0 and s != (1,1,1):
            assert history[1] != history[0] and history[2] != history[0]
    assert matching_primitive_orbits == 619
    assert len(periodic) == 620, len(periodic)
    assert len(extinct) == 1442, len(extinct)
    assert depth_hist == Counter({0:620,1:248,2:658,3:739,4:641,5:391,6:78}), depth_hist
    P, E = coeff_table(periodic), coeff_table(extinct)
    assert P == {
        (1,1,1):1,(1,1,2):4,(1,2,2):16,(1,2,3):8,
        (1,3,3):12,(1,3,4):4,(1,4,4):4,(2,2,2):42,
        (2,2,3):32,(2,2,4):6,(2,3,3):36,(2,3,4):12,
        (2,4,4):6,(3,3,3):36,(3,3,4):12,(3,4,4):4,(4,4,4):1}
    assert E == {
        (1,1,1):64,(1,1,2):88,(1,1,3):52,(1,1,4):12,
        (1,2,2):98,(1,2,3):44,(1,2,4):7,(1,3,3):12,
        (2,2,2):108,(2,2,3):42,(2,2,4):4,(2,3,3):12,(3,3,3):4}
    # Bound sharp on a triangle at 5, and on every larger tripartite graph at 6.
    for sizes in ((1,1,1),(1,1,2),(1,2,1),(2,1,1),(2,2,2)):
        allowed = [s for s in STATE_SET
                   if all(m.bit_count() <= n for m,n in zip(s,sizes))]
        maximum = max(next(t for t in range(7) if (z:=profiles(s))[t] == z[t+4]) for s in allowed)
        assert maximum == (5 if sizes==(1,1,1) else 6)
    sample_counts = 0
    for a,b,c in [(1,1,1),(1,1,2),(1,2,2),(2,2,2),
                  (1,2,3),(2,2,3),(2,3,3),(3,3,3)]:
        f, p, e, depth = direct_counts(a,b,c)
        assert f == 1
        assert p == total_from_table(P,a,b,c)-1, (a,b,c,p)
        assert e == total_from_table(E,a,b,c), (a,b,c,e)
        assert max(depth)==(5 if (a,b,c)==(1,1,1) else 6)
        assert p % 4 == 0
        sample_counts += 4**(a+b+c)
    print('SUPPORT_STATES',len(STATE_SET))
    print('RECURRENT_SUPPORT_STATES',len(periodic))
    print('IDENTICAL_FOUR_CYCLE_SUPPORT_STATES',matching_primitive_orbits)
    print('EXTINCTION_SUPPORT_STATES',len(extinct))
    print('EXACT_SUPPORT_ENTRY_HISTOGRAM',sorted(depth_hist.items()))
    print('PERIODIC_TABLE',sorted(P.items()))
    print('EXTINCTION_TABLE',sorted(E.items()))
    print('INDEPENDENT_MICROSCOPIC_STATES',sample_counts)
    print('SHARP_DEPTH_6_WITNESS',((0,),(3,),(1,2)))
    print('GH4_TRIPARTITE_VERIFY_OK')

if __name__ == '__main__': main()
