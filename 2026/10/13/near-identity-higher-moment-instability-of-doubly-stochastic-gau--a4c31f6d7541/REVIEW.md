# Self-review

## Correctness — PASS

The statement is about one fully specified entry-weighted four-transition linear solver. Direct expansion of one coordinate update and summation with the exact weights gives the conditional squared-norm identity; the smallest singular value of the coefficient matrix then gives the uniform second-moment contraction. Markov and Borel–Cantelli imply almost-sure convergence. For the higher orders, retaining the two off-diagonal transitions, applying the two-coordinate power-mean inequality, and computing the smaller singular value of their shared updated-coordinate map gives the displayed lower factor. These inequalities iterate by conditional expectation for every initial vector. The factor diverges as the off-diagonal coefficient decreases for each fixed order above two. Exact rational matrix and path checks replay successfully, but finite tests are not used as infinite proofs. The derivation requires nonzero entries, independent index selection, and fixed relaxation strictly between zero and one.

## Originality — PASS, subject to priority risk

The closest source [1] establishes mean-square geometric convergence for this entry-weighted algorithm, not the failure of higher-moment control. Its Algorithm 1 and Theorem 1 were inspected directly. The block generalization [2] gives the same entry-level specialization with second-moment rather than order-above-two guarantees. Published broader expected-norm solver frameworks [3] do not provide this near-identity, every-initial-state higher-moment obstruction. General multiplicative-noise tail theory [4,5] provides thematic motivation, not this specific homogeneous-matrix assertion. Searches for aliases, exact matrix parameters, moment-order separation, and stronger implication did not identify coverage. Unindexed or differently worded equivalent work could exist; finite source inspection cannot establish absolute novelty.

## Value — PASS

This theorem isolates an important limitation of a standard, published mean-square convergence guarantee: even a nearly perfectly conditioned positive-definite system, at a recommended nonaggressive relaxation, can have unboundedly growing rare-event error moments. The arbitrary rate, any selected order above two, and uniformity over every nonzero starting state are structural aspects of the obstruction, not a numerical anomaly. It informs interpretation of high-confidence error bounds and of safeguards for division by small selected matrix entries. It does not claim practical divergence, finite-time moment infinity, or a new faster solver.

## Closest literature and limitations

Sources [1] and [2] are closest because they define precisely the studied selection and update. The extension from second-moment to higher-moment behavior is not a consequence of their second-moment theorems. Source [3] concerns broad expected-error convergence; [4,5] concern heavy tails, often with persistent additive noise or stationary laws. Priority beyond examined literature remains uncertain. All finite-time moments are finite. The higher-moment result requires selecting a sufficiently small off-diagonal parameter for the requested order, and no claim is made about fixed-parameter instability for every order above two.

Self-review: passed. Independent audit: not yet performed.
