# Mathematical review

## Correctness — PASS
The exact open neighborhoods produce two explicit subcomplexes \(P,Q\). Their extra simplices are free cones over facets, so each piece collapses onto the boundary of its own \(n\)-vertex simplex; the intersection is exactly the crown graph. Its connected first Betti number is \(n^2-3n+1\). Because the two pieces are simply connected for every \(n\ge4\), the two intersection maps are nullhomotopic, and the homotopy pushout gives the asserted integral sphere wedge. The published combinatorial Alexander duality theorem and the standard \(2n-j-3\) degree shift yield every dominance-homology group. A standalone finite checker independently corroborates face identities, exact duality and mod-two homology. The theorem is not inferred from these finite checks.

## Originality — PASS against inspected evidence
The closest published dominance source [3] proves general Alexander duality, rather than crown-graph homology; this known tool is explicitly credited. The closest rook-neighborhood computation [4] assumes both Cartesian factors have size at least three, excluding the two-layer clique prism treated here. The cycle-product neighborhood result [5] has a cycle factor of length at least five; crown graphs in its proof are auxiliary edge-relation graphs, not the complex calculated here. Shukla's graph-class theorem [1] does not cover the infinite high-degree family. Published crown-graph two-independence and finite crown configuration calculations classify different objects. Searching both the crown/dominance and the graph-complement/neighborhood formulations found no statement implying the simultaneous all-parameter homotopy and integral-homology claims. An unindexed equivalent source remains a risk.

## Value — PASS
The crown graph is the canonical complete bipartite graph with a perfect matching removed, and its complement is the canonical two-layer clique prism. A full uniform integral computation answers the natural exact-homology question motivated by the dominance-neighborhood duality framework, exhibiting two distinct homological dimensions for every \(n\ge5\) and a distinguished rank-seven boundary case. The explicit two-piece homotopy pushout explains those dimensions and multiplicities rather than merely enumerating individual graph instances. No general classification of all bipartite graphs is asserted.

## Limits and prior work
The claimed homotopy equivalence is only for the complementary open-neighborhood complex; Alexander duality gives homology, not homotopy, of the dominance complex. The all-parameter proof requires \(n\ge4\), and finite binary computations cannot establish an integral infinite-family theorem alone. The standard duality is due to Matsushita–Wakatsuki and is not presented as new. The search is not a universal priority guarantee.

Self-review: passed. Independent audit: not yet performed.
