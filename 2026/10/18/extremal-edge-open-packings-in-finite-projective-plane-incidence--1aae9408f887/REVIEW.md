# Scientific review: projective-plane edge-open packings

## Correctness — PASS
The proof uses only finite projective-plane incidence axioms. Each selected edge maps bijectively to its leaf after orienting the induced star components. Mixed-side leaf sets have nonincidence constraint and the double-counting inequality \(|X|+|Y|\le q^2+1\), strictly below the constructed \(q(q+1)\) optimum. With all leaves on one side, two centers force at least one omitted line; equality forces all centers onto that line and every other line to meet precisely its unique center. Duality and distinctness yield all \(2(q^2+q+1)\) maxima. The code independently checks the complete \(q=2,3\) censuses and constructions for \(q=5,7\). Unverified computational orders do not enter the proof.

## Originality — PASS, residual historical risk
The original edge-open-packing article establishes the generic degree bound and enumerates other standard graph families. The full relevant section of Brešar–Samadi (arXiv:2403.00750v1, Theorem 4.1) classifies equality at \(|E|/\delta\), not the strict near-equality value or its projective-plane maximizers. The injective-edge-coloring article (arXiv:2010.00429) studies numbers of colors, not maximum class size. Searches using Levi-graph, induced-star-forest, and injective-color-class aliases did not reveal a stronger theorem. The order-two Heawood case is excluded from the asserted theorem. An unindexed equivalence in classical incidence-geometry or induced-star literature remains possible.

## Value — PASS
The result proves an exact invariant for an infinite geometric class without a Desarguesian assumption. The sharp one-step improvement to the general degree bound is accompanied by a complete rigidity and counting theorem, not just an isolated numeric example. The mixed-leaf obstruction is an independent incidence-counting tool potentially usable for partial-plane configurations.

## Scientific limitations
Finite tests cover prime fields of orders 2, 3, 5, and 7; exhaustive maximal-packing enumeration is only performed at orders 2 and 3. No experiment establishes the general theorem without the written proof. Existence of planes of arbitrary order is not assumed. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
