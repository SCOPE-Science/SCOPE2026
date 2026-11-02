# Self-review

## Correctness — PASS

The theorem is proved for every integer \(q\ge3\), \(n\ge1\), and \(3\le t\le q\). A partition into full coordinatewise-permutation cliques gives the upper bound; a fixed-coordinate cylinder realizes it. At equality any full transversal is saturated, because a coordinate-permutation automorphism transports the partition so that it contains that particular transversal. Swapping two vertices in a completed transversal gives a two-by-two identity, and connectivity of the complete-disagreement graph for \(q\ge3\) implies context-independent coordinate differences. The resulting additive Boolean function depends on at most one coordinate; nontrivial density forces exactly one. The counting step excludes duplicate descriptions. Direct clique enumeration and an independent transversal-equality solver replayed successfully. **Risk:** no finite computation substitutes for the universal swap and additivity argument; its assumptions are all explicit.

## Originality — PASS (historical priority provisional)

The closest recent exact-distance Hamming study (Csajbók–Mukkamala–Nagy, arXiv:2610.32789v1) gives the triangle-free problem, including the distance-one endpoint, but not the full-distance equality classification. Brakensiek (DOI:10.4230/LIPIcs.APPROX-RANDOM.2017.33) concerns independent-set stability on the same tensor-product host; the present \(t\ge3\) sets need not be independent. Popova (arXiv:2609.32903v1) analyzes induced-degree minima, which do not determine induced forbidden-clique maxima. Mathematical-record searches under exact-distance, tensor/direct/categorical product and transversal-clique formulations did not identify a covering theorem. **Risk:** equivalent historical work on transversal hypergraphs or clique-partition designs may exist, so independent priority research is still needed.

## Mathematical value — PASS

The result is a natural missing boundary case of an active exact-distance vertex Turán problem, rather than a fixed-size numerical example. It gives sharp maxima for every nontrivial forbidden clique order, proves a strong rigidity classification, and counts all extremizers. The proof isolates a reusable mechanism: saturation of all full transversals and Boolean rigidity from two-coordinate swaps. The result remains distinct from standard independent-set extremality because induced edges are allowed in the admissible sets.

## Scope

Only Hamming distance equal to dimension, alphabet size at least three, and forbidden cliques of order between three and the alphabet size are covered. No quantitative near-extremal stability is claimed.

Self-review: passed. Independent audit: not yet performed.
