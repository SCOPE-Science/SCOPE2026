#!/usr/bin/env python3
"""Exact finite verification for the Paley-17 two-independence complex."""
from collections import Counter, deque
from functools import lru_cache
from math import gcd
from functools import reduce

P = 17
ORDER = [9,3,0,6,15,11,8,10,13,12,1,2,16,4,14,5,7]
SQUARES = {i*i % P for i in range(1,P)}
NEIGHBORS = [sum(1 << j for j in range(P) if (j-i) % P in SQUARES)
             for i in range(P)]

def degree_test(mask):
    """Components have at most two vertices iff induced max degree is <=1."""
    return all((NEIGHBORS[v] & mask).bit_count() <= 1
               for v in range(P) if mask & (1 << v))

def component_test(mask):
    """Independent membership check by actual induced connected components."""
    rest = mask
    while rest:
        seed = rest & -rest
        visited = seed
        frontier = seed
        while frontier:
            v_bit = frontier & -frontier
            frontier -= v_bit
            v = v_bit.bit_length()-1
            new = (NEIGHBORS[v] & mask) & ~visited
            visited |= new
            frontier |= new
        if visited.bit_count() > 2:
            return False
        rest &= ~visited
    return True

def signed_facets(simplex):
    """Return all codimension-one faces with the ordered simplicial signs."""
    answer = []
    x = simplex
    while x:
        bit = x & -x
        x -= bit
        sign = -1 if (simplex & (bit - 1)).bit_count() % 2 else 1
        answer.append((simplex ^ bit, sign))
    return answer

def match_faces(all_faces):
    remaining = set(all_faces) - {0}
    matching = []
    for vertex in ORDER:
        bit = 1 << vertex
        # Compare against a fixed unmatched set at the start of each stage.
        for s in sorted(remaining):
            t = s | bit
            if not (s & bit) and s in remaining and t in remaining:
                remaining.remove(s)
                remaining.remove(t)
                matching.append((s,t))
    return matching, remaining

def verify_acyclic(all_faces, matching):
    nonempty = sorted(s for s in all_faces if s)
    ids = {s:i for i,s in enumerate(nonempty)}
    matched = set(matching)
    graph = [[] for _ in nonempty]
    indeg = [0] * len(nonempty)
    incidences = 0
    for high in nonempty:
        if high.bit_count()==1:
            continue
        for low,sgn in signed_facets(high):
            if (low,high) in matched:
                u,v = ids[low],ids[high]
            else:
                u,v = ids[high],ids[low]
            graph[u].append(v)
            indeg[v] += 1
            incidences += 1
    queue = deque(i for i,d in enumerate(indeg) if d==0)
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v]==0:
                queue.append(v)
    assert count == len(nonempty), "cyclic matching"
    return incidences

def rank_mod2(columns):
    pivots = {}
    for word in columns:
        while word:
            lead = word.bit_length()-1
            if lead not in pivots:
                pivots[lead] = word
                break
            word ^= pivots[lead]
    return len(pivots)

def chain_ranks_mod2(all_faces):
    ranks = {}
    for k in range(1,5):
        lower = sorted(s for s in all_faces if s.bit_count()==k)
        upper = sorted(s for s in all_faces if s.bit_count()==k+1)
        index = {s:i for i,s in enumerate(lower)}
        columns = [sum(1 << index[low] for low,_ in signed_facets(s))
                   for s in upper]
        ranks[k] = rank_mod2(columns)
    betti = {}
    for dim in range(5):
        nk = sum(s.bit_count()==dim+1 for s in all_faces)
        betti[dim] = nk - ranks.get(dim,0)-ranks.get(dim+1,0)
    return ranks,betti

def project_to_critical_two(matching, critical):
    low_to_high = {low:high for low,high in matching}
    high_to_low = {high:low for low,high in matching}
    critical_two = set(s for s in critical if s.bit_count()==3)
    assert len(critical_two)==1
    @lru_cache(None)
    def projection(s):
        if s in critical_two:
            return 1
        if s in high_to_low:
            return 0
        if s in low_to_high:
            high = low_to_high[s]
            facets = signed_facets(high)
            pivot = next(sign for face,sign in facets if face==s)
            other = sum(sign*projection(face)
                        for face,sign in facets if face!=s)
            return -other * pivot  # pivot is either +1 or -1
        raise AssertionError("unpaired, unrecognized two-face")
    return projection

def translate(mask, shift=1):
    return ((mask << shift)|(mask >> (P-shift))) & ((1<<P)-1)

def main():
    a = [s for s in range(1<<P) if degree_test(s)]
    b = [s for s in range(1<<P) if component_test(s)]
    assert a == b, "independent face enumerations disagree"
    counts = Counter(s.bit_count()-1 for s in a if s)
    assert [counts.get(d,0) for d in range(5)] == [17,136,340,306,68]
    assert len(a)==868
    aset = set(a)
    facet_counts = Counter(s.bit_count() for s in a if s and
                           not any((s | (1<<v)) in aset
                                   for v in range(P) if not(s & (1<<v))))
    assert facet_counts == {4:34,5:68}
    pairs,critical = match_faces(a)
    assert len(pairs)==423
    assert Counter(s.bit_count()-1 for s in critical)=={0:1,2:1,3:19}
    assert verify_acyclic(a,pairs)==2856
    p2 = project_to_critical_two(pairs,critical)
    critical_three=sorted(s for s in critical if s.bit_count()==4)
    degrees = {str(s):sum(sign*p2(low)
                          for low,sign in signed_facets(s))
               for s in critical_three}
    assert {int(k):v for k,v in degrees.items() if v} == {
        67620:-1,69728:-1,99360:-1}
    # Check the signed Morse map is a chain projection on every
    # matched two/three pair, not merely on the critical boundaries.
    for low,high in pairs:
        if low.bit_count()==3:
            assert sum(sign*p2(face)
                       for face,sign in signed_facets(high)) == 0
    boundary_gcd = reduce(gcd, (abs(d) for d in degrees.values()), 0)
    assert boundary_gcd == 1
    ranks,betti = chain_ranks_mod2(a)
    assert ranks == {1:16,2:120,3:220,4:68}
    assert betti == {0:1,1:0,2:0,3:18,4:0}
    # Translation by one is a graph automorphism; its C17 action is free
    # on simplices because each face has cardinality at most five.
    for k in range(1,P):
        assert all(translate(s,k) in aset for s in a)
        assert all(translate(s,k)!=s for s in a if s)
    # The nonidentity Lefschetz trace vanishes (no invariant simplex);
    # H_0 is trivial, so H_3 trace equals +1, while rank H_3 is 18.
    certificate = dict(
        graph="Paley(17)",quadratic_residues=sorted(SQUARES),
        vertex_count=17,facets=dict(sorted(facet_counts.items())),
        f_vector=[17,136,340,306,68],augmented_face_count=868,
        matching_order=ORDER,matching_pairs=423,
        critical_cells={str(dim):sorted(s for s in critical
                         if s.bit_count()-1==dim) for dim in (0,2,3)},
        hasse_incidences=2856,
        nonzero_integral_morse_boundary={k:v for k,v in degrees.items() if v},
        boundary_gcd=boundary_gcd,mod2_boundary_ranks=ranks,
        mod2_betti=betti,
        reduced_integral_homology={"3":"Z^18"},
        homotopy="wedge of 18 3-spheres",
        rational_translation_character={"identity":18,
                                        "nonidentity":1})
    print("PALEY17_SECOND_INDEPENDENCE_EXACT_CHECK_OK")
    print(__import__('json').dumps(certificate,sort_keys=True))
if __name__=="__main__":
    main()
