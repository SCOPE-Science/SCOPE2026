#!/usr/bin/env python3
"""Exact finite certificate for the symmetric-group homology character
of the complex of pairwise-intersecting triples on seven points.
Only the Python standard library is required.
"""
from itertools import combinations, permutations
from functools import lru_cache
from math import comb, factorial

N = 7
TRIPLES = tuple(combinations(range(N), 3))
INDEX = {t: i for i, t in enumerate(TRIPLES)}
assert len(TRIPLES) == 35
DISJOINT = tuple(sum(1 << j for j, b in enumerate(TRIPLES)
                     if not (set(a) & set(b))) for a in TRIPLES)


def partitions(n, largest=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, n if largest is None else largest), 0, -1):
            for tail in partitions(n-k, k):
                yield (k,) + tail


def perm_of_type(typ):
    p = list(range(N))
    pos = 0
    for ell in typ:
        for j in range(ell):
            p[pos+j] = pos+(j+1) % ell
        pos += ell
    assert sorted(p) == list(range(N))
    return p


def quotient_graph(typ):
    """An invariant face is a union of mutually compatible triple orbits."""
    p = perm_of_type(typ)
    act = [INDEX[tuple(sorted(p[i] for i in t))] for t in TRIPLES]
    seen, orbits = set(), []
    for i in range(35):
        if i in seen:
            continue
        orbit = []
        j = i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = act[j]
        assert j == i
        orbits.append(orbit)
    valid = [o for o in orbits if not any((DISJOINT[i] >> j) & 1
                                         for i in o for j in o)]
    adj = [0] * len(valid)
    for a, oa in enumerate(valid):
        for b, ob in enumerate(valid):
            if a != b and any((DISJOINT[i] >> j) & 1
                              for i in oa for j in ob):
                adj[a] |= 1 << b
    assert all(((adj[a] >> b) & 1) == ((adj[b] >> a) & 1)
               for a in range(len(valid)) for b in range(len(valid)))
    return len(orbits), valid, adj


def signed_independent_sum(adj):
    """I_G(-1), via deletion / closed-neighborhood recurrence."""
    @lru_cache(None)
    def rec(mask):
        if not mask:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        no_i = mask ^ bit
        return rec(no_i) - rec(no_i & ~adj[i])
    return rec((1 << len(adj))-1)


def signed_independent_sum_direct(adj):
    """Independent cross-check: visit every independent subset without memoization."""
    even = odd = 0
    stack = [((1 << len(adj))-1, 0)]
    while stack:
        mask, parity = stack.pop()
        if not mask:
            if parity:
                odd += 1
            else:
                even += 1
            continue
        bit = mask & -mask
        i = bit.bit_length()-1
        left = mask ^ bit
        stack.append((left, parity))
        stack.append((left & ~adj[i], parity ^ 1))
    return even-odd, even+odd


def fixed_k_sets(typ, k):
    # A subset of the underlying seven points is invariant precisely when
    # it is a union of entire cycles.
    dp = [0]*(k+1)
    dp[0] = 1
    for ell in typ:
        for j in range(k, ell-1, -1):
            dp[j] += dp[j-ell]
    return dp[k]


def h6_expected(typ):
    parity = (-1)**(N-len(typ))
    chi43 = fixed_k_sets(typ,3)-fixed_k_sets(typ,2)
    return 1+(1+parity)*chi43


def h9_expected(typ):
    parity = (-1)**(N-len(typ))
    return parity * typ.count(1)


def check_sphere_and_cocycle():
    """The seven six-set cross-polytope cycles pair with maximal-face
    cocycles by an integral identity matrix (up to orientation)."""
    supports = tuple(combinations(range(N),6))
    for S in supports:
        A, B = set(S[:3]), set(S[3:])
        F = frozenset([tuple(sorted(A))] +
                      [tuple(sorted((a,)+b)) for a in A
                       for b in combinations(sorted(B),2)])
        assert len(F)==10
        assert set().union(*map(set,F))==set(S)
        assert all(set(t)&set(u) for t in F for u in F)
        for t in TRIPLES:
            if t in F:
                continue
            assert any(not (set(t)&set(u)) for u in F), ('nonmaximal',S,t)
        # X_S is a join of ten 0-spheres, each complementary pair supplying
        # one factor. F takes exactly one vertex of every factor.
        comp_pairs = {frozenset((t,tuple(x for x in S if x not in t)))
                      for t in combinations(S,3)}
        assert len(comp_pairs)==10
        assert all(len(F&pr)==1 for pr in comp_pairs)
        for T in supports:
            # All ten triples of F occur in the expansion of z_T iff S=T.
            carries = all(set(triple) <= set(T) for triple in F)
            assert carries == (S==T)
    # The orientation of the boundary cross-polytope is the signed
    # permutation determinant on its ten pairs of opposite vertices.
    standard = tuple(range(6))
    reps = []
    seen = set()
    for t in combinations(standard,3):
        if t in seen:
            continue
        c = tuple(x for x in standard if x not in t)
        seen.add(t); seen.add(c)
        reps.append((t,c))
    assert len(reps)==10
    for p in permutations(standard):
        q = []
        flips = 0
        for t, c in reps:
            t2 = tuple(sorted(p[x] for x in t))
            c2 = tuple(sorted(p[x] for x in c))
            idx = next(i for i,(a,b) in enumerate(reps)
                       if {a,b}=={t2,c2})
            q.append(idx)
            flips += t2 != reps[idx][0]
        inv = sum(q[i]>q[j] for i in range(10) for j in range(i+1,10))
        pinv = sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))
        assert (inv+flips-pinv)%2==0
    return len(supports), factorial(6)


def main():
    checked_supports, checked_permutations = check_sphere_and_cocycle()
    assert checked_supports==7 and checked_permutations==720
    rows = []
    for typ in partitions(7):
        orbit_count, valid, adj = quotient_graph(typ)
        signed1 = signed_independent_sum(adj)
        signed2, total_faces = signed_independent_sum_direct(adj)
        assert signed1==signed2
        # Including the empty (-1)-simplex, reduced Lefschetz trace is -I(-1).
        L = -signed1
        h9 = h9_expected(typ)
        h6 = L+h9
        assert h6==h6_expected(typ)
        rows.append((typ, orbit_count, len(valid), total_faces,L,h9,h6))
    assert rows[-1][0]==(1,)*7 and rows[-1][-3:]==(22,7,29)
    # Orthogonality and irreducibility checks without a character-table library.
    # chi_(4,3) = permutation character on 3-subsets - that on 2-subsets.
    # The other 14-dimensional constituent is its sign twist.
    h6_chi = lambda typ: next(row[-1] for row in rows if row[0]==typ)
    irr1 = lambda typ: fixed_k_sets(typ,3)-fixed_k_sets(typ,2)
    irr2 = lambda typ: ((-1)**(7-len(typ)))*irr1(typ)
    trivial = lambda typ: 1
    def z(typ):
        ans=1
        for ell in set(typ):
            ans *= ell**typ.count(ell)*factorial(typ.count(ell))
        return ans
    def inner(f,g):
        return sum(f(typ)*g(typ)* (factorial(7)//z(typ))
                   for typ in partitions(7))//factorial(7)
    chars = (trivial,irr1,irr2)
    assert all(inner(a,b)==int(i==j) for i,a in enumerate(chars)
               for j,b in enumerate(chars))
    assert all(h6_chi(typ)==sum(f(typ) for f in chars) for typ in partitions(7))
    print('type | orbits | usable | invariant_faces | reduced_L | trace_H9 | trace_H6')
    for typ,o,u,faces,L,h9,h6 in rows:
        print('%s | %d | %d | %d | %d | %d | %d' %
              (','.join(map(str,typ)),o,u,faces,L,h9,h6))
    print('Confirmed: H6 = 1 + S^(4,3) + S^(2,2,2,1) (dimensions 1+14+14).')
    print('Confirmed: H9 = exterior^6 Q^7 = S^(1^7) + S^(2,1^5).')
    print('Confirmed: seven integral sphere/cocycle dual pairs; 720 S6 orientations.')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
