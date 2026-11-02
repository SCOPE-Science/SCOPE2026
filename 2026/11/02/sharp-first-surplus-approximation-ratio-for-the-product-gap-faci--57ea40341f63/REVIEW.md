# Review: first-surplus Product-Gap approximation

**Correctness: PASS.** The omission weights are derived directly from the defining consecutive-gap products, and normalize to twice the product of all gaps times their reciprocal sum. The unconstrained real-line optimal social cost equals the minimum adjacent gap by a triangle-inequality pigeonhole argument. The edge-adjacency estimate and a positive normalization slack prove a strict bound for every positive-optimum profile; a one-short-end-gap family approaches the sharp constant. An independent exact-rational checker tests the direct lottery without assuming the derived formula.

**Originality: PASS, subject to residual priority risk.** Jia's first public manuscript (arXiv:2608.19633v1, 2026-08-20; Definitions and Section 4) and Chan--Lin--Wang (arXiv:2608.22484, first public 2026-08-23; current version inspected; Section 5 and Lemma 5) define the same mechanism and prove the sharp general-population factor \(2k\). Their relevant full-text sections and tightness examples do not state or imply the strictly smaller exact first-surplus worst-case value \(k-\frac12\). Prior results on other \(k=n-1\) mechanisms do not determine this rule's approximation ratio. An unindexed earlier specialization remains conceivable.

**Value: PASS.** Exactly \(k+1\) agents is the first nontrivial population size after \(k\) facilities can cover every report at zero cost. The all-\(k\) exact ratio, explicit full omission law, and sharpness construction characterize a natural parameter frontier; the factor falls from \(2k\) to \(k-\frac12\), not merely by a small additive correction. The result does not require a new incentive theorem.

Limitations: only real-line nearest-facility social cost, the stated lottery and exactly one excess agent; the upper bound is a nonattained supremum, and no strategyproofness for \(k\ge4\) is asserted.

Self-review: passed. Independent audit: not yet performed.
