# Scientific assessment

## Correctness

The proof starts from the exact universally accessing-root clause and formula-indexed implication forcing. Each false implication at any retained nonroot world forces the same implication false at the original root, which justifies using one root-selected material counterexample for every such world. A simultaneous subformula induction verifies both root and nonroot truth, including nested formulas. For closed axioms the frame-level transfer follows from valuation independence, and the Boolean 3-SAT dual-rail reduction uses the guaranteed root self-loop, not an unwarranted nonroot reflexivity assumption. The standalone finite checker passed 1,150 random compression tests, a disjoint-witness example, and 360 SAT-encoding cases. These computations supplement, rather than replace, the general proof.

## Originality

The closest direct source is Kurahashi–Noguchi (arXiv:2605.20769v1, especially §4, Theorem 5.10 and Appendix A). Its finite-frame theorem is qualitative and its finite canonical construction uses saturated formula types; no explicit linear witness-star compression or designated-root semantic complexity classification appears there. The closely related Kurahashi–Sato modal finite-frame paper concerns unrooted formula-indexed semantics with additional modal relations. Tominaga's published 2026 meeting abstract gives NP-completeness for the modal pure logic of necessitation and closed extensions, not the explicit rooted propositional normal form. Derivability translations between the two logics do not alone identify designated-root satisfiability. A residual risk is that the unpublished detail of Tominaga's abstract or the inaccessible 1992 original paper may contain a related witness construction; the present assessment does not claim an exhaustive originality certificate.

## Value

The result replaces the recent qualitative finite-frame conclusion by a bounded **linear-size** canonical witness set, and simultaneously normalizes all nonroot formula-indexed relations to empty/singleton rows. This is a structural model transformation for arbitrary nested formulas, not a pointwise truth-table observation. It gives explicit, polynomially checkable root-satisfiability certificates and a sharp complexity-class boundary for each fixed closed negative extension. The designated-root qualification matters: removing root universality invalidates the central global-witness implication and prevents the same proof.

## Limits and closest-literature risk

The theorem assumes the unrestrained rooted FMT semantics of Kurahashi–Noguchi, not arbitrary additional frame constraints. No optimal-world lower bound or complexity statement for semantic satisfiability at arbitrary worlds is claimed. Both modal NP-completeness (Tominaga, 2026 meeting summary) and the original unrooted FMT semantics (Fitting–Marek–Truszczyński, 1992) remain comparison risks to the extent their full proofs are inaccessible. Finite code checks are diagnostic only.

Self-review: passed. Independent audit: not yet performed.
