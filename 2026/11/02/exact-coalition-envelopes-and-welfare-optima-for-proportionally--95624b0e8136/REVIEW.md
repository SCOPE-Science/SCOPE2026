# Review of the coalitional-envelope finding

## Correctness — PASS

The precise claim is a fixed-profile identity for all nonempty coalitions at every positive approximation factor, followed by geometric and welfare consequences. The proof first fills the outermost coalition indices without widening its range, then separates the two free endpoints into a prefix maximum and suffix minimum. This produces an exact radius for every agent and an explicit attaining contiguous coalition. Both forbidden-ball endpoint sequences are proved nondecreasing, permitting an exact gap decomposition even when agent positions tie or gaps collapse. The welfare objective is affine on each gap; the endpoint optimizer is exact. The extremal equally spaced profile attains the component bound for all positive population sizes. The finite rational verifier checks 2,548 profiles/parameter combinations and further examples; it is not substituted for the universal proof.

## Originality — PASS, with residual priority risk

The 2023 initiating paper introduces this specific strong obnoxious PF axiom and proves existence at factor two, not the complete feasible region or its utility-maximizing facility. The 2021 attractive-facility paper explicitly observes that contiguous coalitions suffice for verifying PF; this preexisting observation is credited and excluded from the novelty claim. The assessed contribution is the further exact prefix/suffix decomposition, ordered forbidden interval geometry, tight component bound and deterministic exact fair-welfare optimizer. A strict example shows that previously optimized weaker UFS does not imply the new optimization result. Search results in the consulted indexed mathematical record did not reveal an equivalent statement. Unindexed or inaccessible specialist work may contain equivalent techniques, so publication priority is not independently certified.

## Value — PASS

The original literature establishes that the strong coalition axiom is universally feasible at factor two but focuses welfare optimization on weaker fairness axioms. The complete set-valued characterization and exact linear-time optimizer answer a natural missing question: which placements satisfy **all** coalitions and which of those maximizes total distance? An explicit profile exhibits a strict optimal-welfare loss relative to weaker fairness, while the tight number of components shows that feasible placements can be genuinely disconnected and that a full representation may require linear output. This is a structural algorithmic result rather than a renamed existence statement or a single arbitrary finite example.

## Relevant literature and limitations

- Lam et al., *Proportional Fairness in Obnoxious Facility Location*, arXiv:2301.04340 (Section 6, Lemma 5, Theorem 11, Appendix S): known 2-PF existence and the distinction between PF and UFS.
- Aziz et al., *Strategyproof and Proportionally Fair Facility Location*, arXiv:2111.01566 (Section 3, footnote 20): known reduction to contiguous coalitions in the distinct attractive-facility model.

The conclusion assumes a line segment, equal agent weights and absolute-distance utilities, with a sorted-input arithmetic model. It does not establish truthfulness, an approximation-ratio bound, or a result for networks or multiple facilities. Priority against inaccessible specialist literature is a remaining uncertainty.

Self-review: passed. Independent audit: not yet performed.
