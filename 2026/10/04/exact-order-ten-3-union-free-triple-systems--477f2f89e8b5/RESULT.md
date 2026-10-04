# Exact order-ten 3-union-free triple systems
## Finding
For 3-union-free 3-uniform hypergraphs on 10 vertices, \(U_3(10,3)=8\), and every 8-edge extremal family is, up to relabeling, the pair-star consisting of all triples containing one fixed pair.

## Assumptions and scope
Let \(V\) be a 10-element set and let \(\mathcal{H}\subseteq\binom{V}{3}\) be a simple 3-uniform hypergraph. It is 3-union-free when the map \(\mathcal{A}\mapsto\bigcup_{A\in\mathcal{A}}A\) is injective on all nonempty subfamilies \(\mathcal{A}\subseteq\mathcal{H}\) with \(1\le |\mathcal{A}|\le3\). The quantity \(U_3(10,3)\) is the maximum possible number of edges in such a hypergraph.

## Proof
For the lower bound, fix a pair \(\{a,b\}\subset V\) and take every triple containing it. There are exactly \(10-2=8\) such triples. Any subfamily of this pair-star has union \(\{a,b\}\) together with exactly the set of its third vertices, so distinct subfamilies have distinct unions. Thus \(U_3(10,3)\ge8\).

For the upper bound, the exact verifier fixes one edge as \(\{0,1,2\}\). Its stabilizer in the symmetric group has exactly three orbits on a distinct second edge, according as the intersection with \(\{0,1,2\}\) has size \(2\), \(1\), or \(0\); representatives are \(\{0,1,3\}\), \(\{0,3,4\}\), and \(\{3,4,5\}\). Hence every family of at least two edges is represented in one of the three searches.

During each search, the verifier stores all unions of one, two, and three selected edges. A candidate edge is rejected exactly when adding it creates a union already represented by a different selected subfamily, or creates two equal new unions. Such a collision persists after further edges are added, so rejecting that candidate from the current branch is sound. The remaining candidates are traversed in a fixed order, and recursion enumerates every feasible subset of the suffix. For each of the three second-edge orbits, exhaustive search finds no 9-edge family. Therefore \(U_3(10,3)\le8\), proving equality.

For uniqueness at equality, the same three orbit searches exhaustively find no 8-edge 3-union-free family whose edges fail to have a common pair. If an 8-edge family does have a common pair, then it must contain all eight triples through that pair, since exactly eight triples on ten vertices contain a fixed pair. Thus every extremal family is a pair-star up to relabeling.

## Verification
Run `python3 verify.py` in the package directory. The deterministic checker first verifies the 8-edge pair-star directly, then performs the six symmetry-reduced exhaustive searches described above. The recorded node counts are 21,112, 115,499, and 111,602 for the three 9-edge searches, and 27,951, 148,500, and 138,843 for the three 8-edge non-pair-star searches. `verification_output.txt` records the replay output and ends with `ALL CHECKS PASSED`.

The computation is exhaustive only for this finite 10-vertex statement. It is not being used as evidence for any infinite-order assertion.

## Relationship to prior work
Liu, Shangguan, and Zhang define the same extremal function \(U_t(n,r)\) and identify the family \(U_3(n,2s-1)\), which includes \(U_3(n,3)\), among the exceptional regimes left open by their 2026 asymptotic theory. Their preprint was first public on 2026-05-12. Füredi and Ruszinkó earlier studied the same union-free triple-system regime and proved an asymptotic lower bound for \(U_3(n,3)\), rather than an exact order-ten value.

Targeted searches for the exact order-ten statement, its pair-star extremal classification, the older “uniquely decipherable code of order 3” terminology, and related cover-free terminology found no source implying the claim. A published exact small-order record located during comparison covers orders only through nine. These searches support, but cannot logically certify, bibliographic novelty; old coding-theory tables under alternate terminology remain a residual literature risk.

## Limitations
The result concerns only simple 3-uniform hypergraphs on exactly ten vertices and the 3-union-free condition. It does not determine \(U_3(n,3)\) for \(n\ge11\), its asymptotic order, or stability beyond the exact extremal classification at order ten. The originality assessment is limited by discoverability of older literature and by incomplete access to one closely related published small-order artifact whose indexed summary explicitly states a range ending at nine.

## References
1. M. Liu, C. Shangguan, and C. Zhang, “Sharp bounds for uniform union-free hypergraphs,” arXiv:2605.11949, first submitted 2026-05-12.
2. Z. Füredi and M. Ruszinkó, “Uniform hypergraphs containing no grids,” arXiv:1103.1691; Advances in Mathematics 240 (2013), 302–324.
3. “Exact small-order 3-union-free triple systems through nine vertices,” published scientific record `2026/9/30/SCOPE-exact-small-order-3-union-free-triple-systems--03aae5a816cb`.
