#!/usr/bin/env python3
"""Finite exact verification of the rational homology characters of two
Heawood graph matching complexes. Requires Python 3 standard library only.

The point and line labels are the nonzero binary triples 1,...,7;
(p,l) is an incidence precisely when the binary dot product vanishes.
"""
from collections import Counter
from itertools import product
from math import gcd

PTS = tuple(range(1, 8))
EDGES = tuple((p, l) for p in PTS for l in PTS if ((p & l).bit_count() & 1) == 0)
assert len(EDGES) == 21
IDX = {e: i for i, e in enumerate(EDGES)}
EDGE_ENDS = tuple((1 << p) | (1 << (l + 7)) for p, l in EDGES)
I = tuple(range(21))

def extension_facets():
    """Exhaust all point-to-line bijections compatible with incidence."""
    out = set()
    def rec(k, used, mask):
        if k == 7:
            out.add(mask)
            return
        p = PTS[k]
        for l in PTS:
            if ((p, l) in IDX) and not (used & (1 << l)):
                rec(k + 1, used | (1 << l), mask | (1 << IDX[p, l]))
    rec(0, 0, 0)
    return out

def perfect_faces(facets):
    fs = {0}
    for f in facets:
        sub = f
        while sub:
            fs.add(sub)
            sub = (sub - 1) & f
    return fs

def matching_faces():
    out = {0}
    def dfs(next_edge, used_endpoints, mask):
        for i in range(next_edge, len(EDGES)):
            if not (used_endpoints & EDGE_ENDS[i]):
                new = mask | (1 << i)
                assert new not in out
                out.add(new)
                dfs(i + 1, used_endpoints | EDGE_ENDS[i], new)
    dfs(0, 0, 0)
    return out

def permanent_subset_count():
    """Independent subset-DP count of perfect matchings."""
    counts = {0: 1}
    for p in PTS:
        nxt = {}
        for subset, ways in counts.items():
            for l in PTS:
                if (p, l) in IDX and not (subset & (1 << l)):
                    ns = subset | (1 << l)
                    nxt[ns] = nxt.get(ns, 0) + ways
        counts = nxt
    return counts.get(sum(1 << l for l in PTS), 0)

def fvector(faces):
    c = Counter(f.bit_count() - 1 for f in faces if f)
    return tuple(c[k] for k in range(7))

def mod2_boundary_ranks(faces):
    chains = [[f for f in faces if f.bit_count() == k+1] for k in range(7)]
    rows = [None] + [{f: i for i, f in enumerate(chains[k - 1])} for k in range(1, 7)]
    ranks = []
    for k in range(1, 7):
        basis = {}
        for f in chains[k]:
            col = 0
            b = f
            while b:
                low = b & -b
                b ^= low
                col ^= 1 << rows[k][f ^ low]
            while col:
                p = col.bit_length() - 1
                if p in basis:
                    col ^= basis[p]
                else:
                    basis[p] = col
                    break
        ranks.append(len(basis))
    return tuple(ranks)

def rational_ranks_forced(fvec, mod2):
    """Prove all Q-ranks equal F2-ranks using the chain inequalities.

    Rational rank >= mod-2 rank for an integral boundary matrix.
    In any chain complex, rank(d_k)+rank(d_{k+1})<=dim C_k.
    The augmentation identity additionally gives rank(d_1)<=dim C_0-1.
    """
    lower = [0, *mod2, 0]
    upper = [0] + [min(fvec[k-1], fvec[k]) for k in range(1, 7)] + [0]
    upper[1] = min(upper[1], fvec[0]-1)
    for _ in range(9):
        for k in range(7):
            upper[k] = min(upper[k], fvec[k] - lower[k+1])
            upper[k+1] = min(upper[k+1], fvec[k] - lower[k])
    assert lower == upper, (lower, upper)
    betti = [fvec[k]-lower[k]-lower[k+1] for k in range(7)]
    return tuple(betti)

def linear(cols, x):
    result = 0
    for k in range(3):
        if (x >> k) & 1:
            result ^= cols[k]
    return result

def dot(x, y):
    return ((x & y).bit_count() & 1)

def automorphisms():
    """GL(3,2) and the incidence polarity, hence all 336 automorphisms."""
    out = []
    for cols in product(PTS, repeat=3):
        if len({linear(cols, v) for v in range(8)}) != 8:
            continue
        pmap = {p: linear(cols, p) for p in PTS}
        lmap = {}
        for l in PTS:
            eligible = [l2 for l2 in PTS if all(dot(l2,pmap[p]) == dot(l,p) for p in PTS)]
            assert len(eligible) == 1
            lmap[l] = eligible[0]
        preserve = tuple(IDX[(pmap[p],lmap[l])] for p,l in EDGES)
        exchange = tuple(IDX[(lmap[l],pmap[p])] for p,l in EDGES)
        out.append((1, preserve))
        out.append((-1, exchange))
    assert len(out) == len({p for _,p in out}) == 336
    assert sum(s == 1 for s, _ in out) == 168
    return out

def order(perm):
    seen = set()
    ans = 1
    for i in range(21):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = perm[j]
        ans = ans * length // gcd(ans, length)
    return ans

def cycles(perm):
    seen = set()
    result = []
    for i in range(21):
        if i in seen:
            continue
        j = i
        mask = 0
        while j not in seen:
            seen.add(j)
            mask |= 1 << j
            j = perm[j]
        result.append(mask)
    return result

def direct_reduced_trace(faces, perm):
    total = -1  # subtract trace on H_0
    for mask in faces:
        if not mask:
            continue
        ids = [i for i in range(21) if (mask >> i) & 1]
        images = [perm[i] for i in ids]
        if set(images) != set(ids):
            continue
        inversions = sum(images[a] > images[b]
                         for a in range(len(images)) for b in range(a+1, len(images)))
        total += (-1 if ((len(ids)-1+inversions) % 2) else 1)
    return total

def orbit_reduced_trace(faces, perm):
    """Independent fixed-face calculation via unions of edge-permutation cycles."""
    edge_cycles = cycles(perm)
    total = 0
    def rec(j, mask, selected):
        nonlocal total
        if j == len(edge_cycles):
            total += (-1 if (selected & 1) else 1)
            return
        rec(j+1, mask, selected)
        candidate = mask | edge_cycles[j]
        if candidate in faces:
            rec(j+1, candidate, selected+1)
    rec(0, 0, 0)
    return -total

def compose(p, q):
    return tuple(p[q[i]] for i in range(21))

def inverse(p):
    out = [0]*21
    for i, v in enumerate(p):
        out[v] = i
    return tuple(out)

def sylow_sevens(aut):
    subgroups = set()
    for sign, g in aut:
        if sign != 1 or order(g) != 7:
            continue
        elements = [I]
        current = I
        for _ in range(6):
            current = compose(g,current)
            elements.append(current)
        assert len(set(elements)) == 7
        subgroups.add(frozenset(elements))
    assert len(subgroups) == 8
    return tuple(subgroups)

def fixed_sylow(perm, subgroups):
    ip = inverse(perm)
    return sum(frozenset(compose(compose(perm,x),ip) for x in s) == s for s in subgroups)

def inner(a,b):
    v = sum(x*y for x,y in zip(a,b))
    assert v % len(a) == 0, v
    return v//len(a)

def run():
    pf = extension_facets()
    assert len(pf) == permanent_subset_count() == 24
    pfaces = perfect_faces(pf)
    mfaces = matching_faces()
    assert len(pfaces) == 2202 and len(mfaces) == 3462
    assert pfaces <= mfaces
    pfvec, mfvec = fvector(pfaces), fvector(mfaces)
    assert pfvec == (21,168,560,756,504,168,24)
    assert mfvec == (21,168,644,1218,1050,336,24)
    prank, mrank = mod2_boundary_ranks(pfaces), mod2_boundary_ranks(mfaces)
    assert prank == (20,148,396,360,144,24)
    assert mrank == (20,148,496,722,312,24)
    assert rational_ranks_forced(pfvec,prank) == (1,0,16,0,0,0,0)
    assert rational_ranks_forced(mfvec,mrank) == (1,0,0,0,16,0,0)
    aut = automorphisms()
    subgroups = sylow_sevens(aut)
    char_pm, char_matching, char_eps, char_T, char_W = [],[],[],[],[]
    types = Counter()
    for sign, g in aut:
        a = direct_reduced_trace(pfaces,g)
        b = direct_reduced_trace(mfaces,g)
        assert a == orbit_reduced_trace(pfaces,g)
        assert b == orbit_reduced_trace(mfaces,g)
        assert a == sign*b
        t = fixed_sylow(g, subgroups)-1
        w = b-1-t
        char_pm.append(a)
        char_matching.append(b)
        char_eps.append(sign)
        char_T.append(t)
        char_W.append(w)
        types[(sign,order(g),a,b)] += 1
    expected = {
        (1,1,16,16):1, (1,2,0,0):21, (1,3,1,1):56,
        (1,4,0,0):42, (1,7,2,2):48,
        (-1,2,-4,4):28, (-1,6,-1,1):56, (-1,8,0,0):84,
    }
    assert types == expected, (types, expected)
    ones = [1]*336
    for i,x in enumerate((ones,char_T,char_W)):
        for j,y in enumerate((ones,char_T,char_W)):
            assert inner(x,y) == int(i==j), (i,j,inner(x,y))
    assert sum(char_pm) == 0  # no full-group invariants
    assert sum(a for a,s in zip(char_pm,char_eps) if s==1) == 168 # dimension 1
    identity_positions = [i for i,(s,g) in enumerate(aut) if g == I]
    assert len(identity_positions)==1
    ii=identity_positions[0]
    assert (char_pm[ii],char_T[ii],char_W[ii])==(16,7,8)
    print('INCIDENCES=21 PERFECT_MATCHINGS=24')
    print('PERFECT_F_VECTOR='+repr(pfvec))
    print('ORDINARY_F_VECTOR='+repr(mfvec))
    print('PERFECT_BOUNDARY_RANKS_F2='+repr(prank))
    print('ORDINARY_BOUNDARY_RANKS_F2='+repr(mrank))
    print('PERFECT_RATIONAL_BETTI=(1, 0, 16, 0, 0, 0, 0)')
    print('ORDINARY_RATIONAL_BETTI=(1, 0, 0, 0, 16, 0, 0)')
    print('GROUP_ORDER=336 COLOR_PRESERVING=168 SYLOW_SEVEN_SUBGROUPS=8')
    for t,n in sorted(types.items()):
        print('ACTION_SIGN=%+d ORDER=%d PERFECT_TRACE=%d ORDINARY_TRACE=%d COUNT=%d' % (*t,n))
    print('PERFECT_EQUALS_SIGN_TWIST_OF_ORDINARY=336/336')
    print('ORDINARY_DECOMPOSITION=1+T7+W8')
    print('PERFECT_DECOMPOSITION=EPSILON_TENSOR_(1+T7+W8)')
    print('PERFECT_FULL_INVARIANTS=0 PERFECT_PRESERVING_INVARIANTS=1')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
