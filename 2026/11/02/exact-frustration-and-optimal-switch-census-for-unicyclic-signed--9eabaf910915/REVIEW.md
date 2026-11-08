# Independent mathematical audit

## correctness

PASS

Bal Section 8 gives the orientation minimization ell(A(G))=min sum_v indeg(v)outdeg(v). On an even unique cycle, bipartite source/sink orientation yields zero, and connectedness forces exactly two. For an odd cycle, some cycle vertex is mixed, contributing >=deg(v)-1>=d_star-1. Choosing a minimum-degree cycle vertex, alternating source/sink on the remaining even number of cycle vertices and into attached trees yields one mixed vertex and exactly d_star-1. Equality forces one such degree-d_star cycle vertex, two alternating path directions, and when d_star>=3 two uniform directions for its incident tree edges, giving 2t or 4t orientations. Because the ordinary line graph is connected, global edge reversal is the only orientation duplication of any fixed signed adjacency, halving counts of distinct optimal signatures. Independent full orientation brute force verified triangle, triangle with one and three pendant leaves, five-cycle with leaves, and quadrilateral with leaves. No finite test is substituted for all unicyclic graphs.

## originality

PASS

General antisymmetric/spectral signed line graph and minimization formula are prior mathematics. The odd/even unicyclic degree-minimum closed form, complete rigidity and labelled optimizer counts have not been found in inspected primary full text; qualified novelty.

## value

PASS

A natural first cyclic class converts a general NP-hard-looking switching optimization into a sharp local cycle-degree formula and counts every optimum; the optimizer census gives substantially more than a routine lower-bound observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
