# Independent mathematical audit

## correctness

PASS

Rebuilt GP(12,5) and verified all distances and MMD comparisons. The 60 MMD pairs are precisely the distance-four pairs. Independently recovered the two 12-vertex rook components from their maximal 3- and 4-cliques and checked the complete row/column adjacency relations. A third vertex cannot strongly resolve an MMD pair: the requisite shortest path would extend from one endpoint along a neighbor farther from the other. Every strong resolving set therefore covers the MMD edges. An independent set in each rook has size at most three, attained in precisely 4×3×2 ways. Independently constructed all 576 six-vertex complements and directly checked that each corresponding size-18 set resolves all 276 pairs. In each rook a maximum independent triple uses each column and misses exactly one row. Its exchanges swap that missing row with the row of one column, giving the three star transpositions on permutations of four rows. The explicit star-to-Nauru correspondence preserves the full edge relation. An exchange cannot transfer a rook complement token between factors, since both triples already have fixed maximal size. This proves the Cartesian square. Independent reconstruction checked all 1,728 exchanges and the distance profile (1,6,21,54,100,138,141,90,25) from all 576 roots, agreeing with the convolution of the common factor shells. Radius and diameter are both eight.

## originality

PASS

The permutation-star description of the ambient graph and the general MMD-cover framework are established. The inspected sources do not provide the rook decomposition and strong-basis exchange interpretation for this graph. A catalogue hit on 576 minimum sets in Nauru concerns power domination rather than strong resolution and has different exchange edges and diameter. The contribution is the strong resolving structure and resulting self-product, not the known Nauru isomorphism.

## value

PASS

A natural minimum landmark-selection problem on a standard symmetric cubic graph has a nontrivial structural solution: the move graph recovers two copies of the original graph as independent coordinates. This gives a benchmark where minimum bases, exchanges and sharp distances have a common explanation, beyond computing a dimension or spot-checking a graph-table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
