"""Exact ternary length-five cross-bifix-free / Hamming-distance-two census.

Python >=3.9, standard library only. Every candidate word and every
compatibility edge are reconstructed from definitions. Two clique engines
use different search invariants; an independent global census checks the
canonical first/last-symbol reduction.
"""
from collections import Counter
from itertools import combinations, permutations, product

Q = '012'
N = 5


def self_nonoverlap(w):
    return all(w[:k] != w[N-k:] for k in range(1, N))


def compat_prefix(w, z):
    return (sum(a != b for a, b in zip(w, z)) >= 2 and
            all(w[:k] != z[N-k:] and z[:k] != w[N-k:]
                for k in range(1, N)))


def compat_concat(w, z):
    # Independently form the complete proper-prefix and proper-suffix
    # languages of each word and test whether either intersection is empty.
    if sum(a == b for a, b in zip(w, z)) >= 4:
        return False
    pw = {w[:k] for k in range(1, len(w))}
    pz = {z[:k] for k in range(1, len(z))}
    sw = {w[-k:] for k in range(1, len(w))}
    sz = {z[-k:] for k in range(1, len(z))}
    return not ((pw & sz) or (pz & sw))


def graph(words, adjacency_predicate):
    words = tuple(sorted(words))
    m = len(words)
    edges = 0
    neighbors = [0]*m
    for i in range(m):
        for j in range(i+1, m):
            if adjacency_predicate(words[i], words[j]):
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
                edges += 1
    return words, neighbors, edges


def bron_kerbosch_maximal(neighbors):
    """Enumerate every maximal clique with the standard P/X invariant."""
    m = len(neighbors)
    out = []
    def rec(R, P, X):
        if not (P or X):
            out.append(R)
            return
        choice_set = P | X
        if choice_set:
            # Deterministic pivot minimizing candidates outside its neighborhood.
            candidates = []
            while choice_set:
                bit = choice_set & -choice_set
                choice_set -= bit
                v = bit.bit_length()-1
                candidates.append(( (P & ~neighbors[v]).bit_count(), v))
            pivot = min(candidates)[1]
            pending = P & ~neighbors[pivot]
        else:
            pending = P
        while pending:
            bit = pending & -pending
            pending -= bit
            i = bit.bit_length()-1
            rec(R | bit, P & neighbors[i], X & neighbors[i])
            P -= bit
            X |= bit
    rec(0, (1<<m)-1, 0)
    return out


def all_cliques_forward(neighbors):
    """Count every clique, not just maximal ones, by increasing vertex index.

    The branching invariant is that the candidate set is exactly all
    vertices later than the last chosen vertex compatible with the prefix.
    """
    counts = Counter()
    opt = []
    top = 0
    def rec(prefix, available):
        nonlocal top, opt
        length = prefix.bit_count()
        counts[length] += 1
        if length > top:
            top, opt = length, [prefix]
        elif length == top:
            opt.append(prefix)
        while available:
            bit = available & -available
            available -= bit
            i = bit.bit_length()-1
            rec(prefix|bit, available & neighbors[i])
    rec(0, (1<<len(neighbors))-1)
    return top, opt, counts


def words_from_mask(ws, mask):
    return frozenset(ws[i] for i in range(len(ws)) if mask & (1<<i))


def distance_spectrum(code):
    return tuple(sum(sum(a != b for a,b in zip(x,y)) == d
                     for x,y in combinations(sorted(code),2)) for d in (2,3,4,5))


def main():
    universe = [''.join(t) for t in product(Q, repeat=N)]
    viable = [w for w in universe if self_nonoverlap(w)]
    assert len(universe) == 243 and len(viable) == 144
    # Independently reconstruct every edge on the 144 viable words.
    for i,w in enumerate(viable):
        for z in viable[i+1:]:
            assert compat_prefix(w,z) == compat_concat(w,z), (w,z)

    canonical = [w for w in viable if w[0] in '01' and w[-1] == '2']
    ws, nb, ec = graph(canonical, compat_prefix)
    assert (len(ws), ec) == (48, 706)
    maxima = bron_kerbosch_maximal(nb)
    hist = dict(sorted(Counter(m.bit_count() for m in maxima).items()))
    assert hist == {3:2,4:18,5:406,6:1294,7:726,8:170,9:4}, hist
    vmax = {words_from_mask(ws,m) for m in maxima if m.bit_count()==9}
    assert len(vmax) == 4
    top, all_tops, sizes = all_cliques_forward(nb)
    assert top == 9 and len(all_tops)==4
    assert set(words_from_mask(ws,m) for m in all_tops)==vmax
    assert dict(sorted(sizes.items())) == {0:1,1:48,2:706,3:4226,
        4:11320,5:13850,6:7752,7:1946,8:204,9:4}

    # A singleton/singleton pair of end-symbol supports cannot attain 9.
    one_one = [w for w in viable if w[0]=='0' and w[-1]=='2']
    ws11, nb11, ee11 = graph(one_one, compat_concat)
    hist11 = Counter(m.bit_count() for m in bron_kerbosch_maximal(nb11))
    assert (len(ws11),ee11,max(hist11)) == (24,152,5)

    # Independent global upper bound/census, with no partition assumptions.
    wg, ng, eg = graph(viable, compat_concat)
    allmax = bron_kerbosch_maximal(ng)
    gh = dict(sorted(Counter(m.bit_count() for m in allmax).items()))
    assert (len(wg), eg) == (144, 3324)
    assert gh == {3:12,4:108,5:2436,6:7764,7:4356,8:1020,9:24}, gh
    global_opt = {words_from_mask(wg,m) for m in allmax if m.bit_count()==9}
    assert len(global_opt)==24

    # Symbol relabeling S_3 and reversal preserve non-overlap and distance.
    generated = set()
    for code in vmax:
        for p in permutations(Q):
            for reverse in (False, True):
                tr = str.maketrans('012',''.join(p))
                transformed = frozenset((w[::-1] if reverse else w).translate(tr)
                                        for w in code)
                generated.add(transformed)
    assert generated == global_opt
    remaining = global_opt.copy()
    orbit_data=[]
    while remaining:
        c = min(remaining,key=lambda c:sorted(c))
        orbit = set()
        for p in permutations(Q):
            tr = str.maketrans('012',''.join(p))
            for rev in (False,True):
                orbit.add(frozenset((w[::-1] if rev else w).translate(tr)
                                    for w in c))
        assert orbit <= remaining
        orbit_data.append((len(orbit), distance_spectrum(c)))
        remaining -= orbit
    assert sorted(orbit_data) == [(12,(21,10,5,0)),(12,(22,8,6,0))],orbit_data

    for code in global_opt:
        assert all(self_nonoverlap(w) for w in code)
        assert all(compat_prefix(x,y) for x,y in combinations(code,2))
    print('VERIFY_OK viable=144 edges=3324 maximum=9 labeled_optima=24 '
          'orbits=2 orbit_sizes=12,12 canonical_candidates=48 '
          'canonical_maxima=4 singleton_pair_cap=5')

if __name__=='__main__':
    main()
