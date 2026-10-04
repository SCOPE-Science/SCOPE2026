# Same-model review

## Correctness
PASS. The proof reduces the first-passage event to integer Bernoulli-count boundaries \(\lceil q_s(\beta)\rceil\). The derivative identity for \(q_s\) and strict convexity of the Bernoulli log moment generating function imply at most one interior minimum for each \(q_s\), hence finitely many effective boundary changes. The finite \(t=30\) statement is replayed by exact rational dynamic programming after numerically bracketing only analytically isolated scalar roots. The computation does not stand in for the general proof.

## Originality
PASS. The motivating 2026 source was inspected at the level of its abstract, flattened-family definitions, and horizon-tuning derivation. It gives a smooth horizon criterion for the power-likelihood family but the inspected material does not state the Bernoulli first-passage staircase, a complete finite cell reduction, or the displayed exact optimizer plateau. Targeted semantic searches for flattened likelihood ratios, Bernoulli lattice thresholds, staircase type-II error, and horizon-optimal tilts returned no statement implying this result. The closest discrete-testing comparison concerns a differentially private binomial testing problem rather than a power-likelihood e-process.

Residual risk remains that the finite-cell mechanism has appeared under different terminology in discrete sequential likelihood-ratio work. This risk is disclosed and is not treated as disproved by failed search.

## Value
PASS. The object being optimized is the operational finite-horizon first-passage type-II probability of the sequential e-test. The result shows that a smooth horizon optimizer need not optimize that exact discrete sequential probability and quantifies a nontrivial gap in a concrete rational design. It also provides a finite exact algorithm for all tilt plateaus at any fixed Bernoulli horizon, so the result is more than a numerical example or a renaming of a standard binomial tail.

## Closest literature and limitations
Forré (2026), arXiv:2609.27765, supplies the flattened likelihood-ratio family and the smooth horizon comparison that motivates the question. Awan and Slavković (2018), arXiv:1805.09236, is a comparison point for exact finite-sample binomial testing under differential privacy, but its inspected abstract addresses a different constrained-testing problem. The theorem here is limited to simple Bernoulli hypotheses and fixed-in-advance \(\beta\); it does not optimize over arbitrary e-processes.

Same-model review: passed. Independent audit: not yet performed.
