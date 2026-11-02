# Scientific review: complete-prism edge landmark classification

## Correctness

**PASS.** The proof explicitly computes distance from both layer types to every edge type, turns indistinguishability into four necessary-and-sufficient conditions, and handles all possible edge pairs. The missing-column lower bound is exact. A case analysis classifies every minimum set for both parameter regimes, including \(n=2,3,4\), and the resulting combinatorial counts are derived without symmetry quotienting. The graph-level BFS verifier independently reconstructs edge-distance codes and checks all minimum-size candidate subsets through \(n=11\). Finite experiments alone would not prove the infinite theorem; its unrestricted conclusion follows from the symbolic edge-type argument.

## Originality

**PASS, conditional on available literature.** The 2022 vertex-edge dominant edge metric paper introduces the invariant and treats path/cycle product families, not all \(K_n\square K_2\). The 2024 Cartesian-product edge metric paper proves the general interval \([n-1,n]\) after specialization, not the sharp threshold or its exact extremal families. A closely related indexed complete-prism result concerns *mixed* metric dimension, a strictly stronger requirement; its \(n\)-element minimum cannot supply the present \(n-1\)-element bases for \(n\ge7\). No equivalent complete statement emerged from targeted mathematical-record and literature searches. The closest mixed-result full text was not accessible and publication priority is not independently certified.

## Value

**PASS.** This natural infinite family exhibits a sharp order-seven phase transition, and the theorem answers both the exact optimization and full multiplicity question instead of giving a routine numerical instance of a general bound. The endpoint cases illustrate precisely which extra configurations appear at low order. A structural explanation in terms of supported matching columns and layer counts is part of the result, and may guide further analysis of Cartesian graph products.

## Limitations and sources

The classification concerns simple complete prisms and does not classify general graph prisms or mixed metric landmark systems. Principal source: Ikhlaq–Hayat–Siddiqui (2022), arXiv:2211.09327. Closest broader bound: Chandran–Reji (2024), DOI:10.22199/issn.0717-6279-5770. Related but different invariant: indexed *Mixed metric bases of complete prisms* record (source identified in RESULT.md). More complete literature discovery and independent expert audit may refine publication-priority status.

Self-review: passed. Independent audit: not yet performed.
