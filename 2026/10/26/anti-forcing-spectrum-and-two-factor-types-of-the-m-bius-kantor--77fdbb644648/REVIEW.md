# Independent mathematical audit

## correctness

PASS

For labelled GP(8,3) on u_i,v_i, exactly 24 simple edges form a cubic bipartite graph with sixteen vertices. Independent bipartite permanent subset DP and vertex-matching backtracking count 33 perfect matchings. For each M, contracting the eight matching edges yields a directed graph on eight vertices and sixteen nonmatching arcs, whose directed cycles correspond bijectively to M-alternating cycles. The minimum feedback-arc-set recurrence over all 256 vertex subsets computes af(M) exactly, and complementing M yields cycle types: three (8,8) matchings have af=4, six (16) and twenty-four (6,10) have af=5. Independent from the submitted verifier, independently generated all perfect matchings and evaluated directed feedback-arc DP, reproducing {((8,8),4):3, ((16,),5):6, ((6,10),5):24}. The inspected separate complete verifier enumerates all 96 automorphisms and three orbits and independently certifies deletion witnesses and arc-disjoint alternating-cycle packings of matching sizes 4,5,5; the elementary DP lower bounds independently corroborate af. Therefore anti-forcing polynomial 3z^4+30z^5 and claimed matching-specific equality follow for exactly this graph; no general nonplanar minimax assertion is made.

## originality

PASS

Lei–Yeh–Zhang (2014) introduced anti-forcing and planar bipartite minimax results; the Möbius–Kantor graph is nonplanar (cubic bipartite girth six on 16 vertices and 24 edges exceeds planar bound 21), so that theorem does not directly cover it. Deng–Zhang (2016) full arXiv HTML gives broad cyclomatic bounds and examples, not the inspected graph-specific census. Balasubramanian (2025) primary full-text Table 1 already records 33 GP(8,3) perfect matchings and automorphism group 96, so those numerical facts are acknowledged prior; it does not record their anti-forcing numbers, complementary two-factor partition or arc-disjoint cycle packing. The new claim is exactly the anti-forcing distribution/cycle type. No directly covering Resultary entry was found; best-of-knowledge, with finite-graph tabulation risk.

## value

PASS

The Möbius–Kantor graph GP(8,3) is the canonical small cubic symmetric nonplanar bipartite graph (Levi graph of the Möbius–Kantor configuration). Anti-forcing number is a natural measure of how many nonmatching edges must be removed to make each perfect matching unique. The full anti-forcing spectrum, three complementary 2-factor types and nonplanar equality of packing/covering provide a complete classification of this natural invariant, not a mere repetition of its known matching count. A finite-graph invariant can have independently useful mathematical value without yielding a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
