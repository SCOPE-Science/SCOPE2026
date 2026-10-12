# Scientific assessment

## Correctness — PASS

The derivation is self-contained: after fixing one row, two residual-line projectors satisfy the exact identity \(TUT=zT\), giving closed formulas for the one- and two-step minimax mean-squared errors. The integer matrix has determinant \(17\); the exact rational Gram parameters and square-root bounds certify all strict order reversals. A positive two-state transfer operator yields the asymptotic factor. The exact-rational checker constructs the original projected operators rather than merely replaying listed values. Minimality follows because the remaining equation in a nonsingular two-row system solves the one-dimensional feasible error in one step.

## Originality — PASS, with residual risk

The SCRK algorithm and its norm-proportional projected-row sampling are due to Lok and Rebrova, arXiv:2309.04889. Sun, Qi, Han, and Xie, arXiv:2605.29304v1, Section 3.2, address fixed-block selection via convergence bounds and surrogates, not distinct exact finite-horizon minimax rankings. Agaskar, Wang, and Lu (2014) provide a broad, exact mean-square operator identity; it can reproduce the special-case matrix calculations, so the identity and calculation method are not new. The strict existence of a **horizon-dependent reversal in which equation is held exact**, together with its minimal dimension and persistence, is not asserted or implied as an existence theorem by the inspected work. Searches did not identify the same counterexample; unknown unindexed equivalents are a residual risk, and lack of search results alone does not prove novelty.

## Value — PASS

The fixed subsystem is chosen before repeated stochastic updates, often by an asymptotic contraction surrogate. The witness shows why an exactly best short-horizon hard-row choice need not remain best even one iteration later, while asymptotic optimization selects a different row. That is a nontrivial policy-selection distinction involving different feasible subspaces rather than tuning probabilities within one subspace; its dimension-minimal and open-set character rules out a singular or isolated numerical coincidence.

## Limits

The comparison is minimax over each hard row's unit feasible-error subspace, not a comparison using one common right-hand side and start. It concerns unrelaxed, independently sampled projected Kaczmarz in exact arithmetic. The overarching randomized-moment formalism was known. Novelty is provisional until external independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
