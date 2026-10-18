# Scientific assessment: strong discrete-Morse complexes of square bouquets

## Correctness — PASS

The theorem applies to all integers \(p\ge2\), to the **full** strong matching complex of the unfilled one-point bouquet \(B_p=\bigvee_{i=1}^p C_4\). The descending-link criterion is exactly one preceding neighbor for a non-hub vertex. There are six local non-hub incidence atoms: their permitted faces make a six-cycle. The position of the hub splits the local faces into a four-vertex path and two independent three-vertex sets. The full complex is the join of the six-cycles plus cones whose bases contain a four-vertex path join factor whenever \(p\ge2\). These bases collapse; their cones collapse **relative to the common join**, establishing actual simplicial collapse and integral sphere homology, not merely experimental Betti numbers. The \(p=1\) connected eight-vertex twelve-edge graph has cycle rank five. Two standard-library programs separately reconstruct all faces for \(p=1,2,3\) by vertex-ordering automata and verify mod-two homology and genuine free-face collapses for \(p=2,3\); finite tests support but do not replace the arbitrary-\(p\) proof. No unproved infinite extension is asserted.

## Originality — PASS, with identified residual uncertainty

Knudson and Owens-White (2026, arXiv:2609.06844, first public 2026-09-06) define the precise full strong complex, study paths, cycles, stars and other base complexes, and prove a join identity for **disjoint unions**. This does not give the result for a connected graph in which the cycles share a hub. Donovan and Scoville (2023, Theorem 5.8) treat the **ordinary edge matching** complex of Dutch windmills; their simplicial vertices and permitted faces are different. Accessible mathematical-record comparisons using aliases (square bouquets, quadrilateral Dutch windmills, one-point cycle wedges, connected graph joins, strong filtration matchings) and other available scientific claims found triangular friendship bouquets in the full strong complex, not four-cycle bouquets. In particular, the triangular-petal formula is not a square-petal corollary: the local matching subcomplexes and cone links change. Exact target novelty was not found in accessible sources. A potential unindexed, unpublished or otherwise unavailable result remains a bibliographic risk, and database search is not proof of uniqueness.

## Mathematical value — PASS

The infinite connected family exhibits a sharp phenomenon in a recently introduced combinatorial-topological invariant: one four-cycle has five independent fundamental-group loops, yet adding a second petal forces a three-sphere, and each additional petal raises the sphere dimension by exactly two. The proof is structural, giving a global simplicial collapse and a connected analogue of the familiar disjoint-union join behavior. This is a meaningful all-parameter homotopy and simple-homotopy classification rather than an arbitrary finite Betti-number calculation. It creates a tractable benchmark for strong discrete Morse matchings on cactus graphs. No general classification of cactus graphs or different cycle lengths is claimed.

## Closest literature and scientific limits

Primary source: K. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844 (2026). Same functor, distinct graph family; the disjoint-union formula is inapplicable to the shared hub.

Related family: C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, New York J. Math. 29 (2023), 1393–1412. Same Dutch windmill graph family, different matching complex.

Foundational construction: X. Fernández, *Strong discrete Morse theory*, Proc. R. Soc. Edinburgh A (published online 2026), DOI 10.1017/prm.2025.10105.

Finite verification covers only one, two, and three petals. The proof covers every integer at least two. Bibliographic completeness and independent external verification remain open.

Self-review: passed. Independent audit: not yet performed.
