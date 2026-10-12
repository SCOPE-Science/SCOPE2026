# Scientific assessment

## Correctness — PASS

For curvatures one and six, the two-state conditional second-moment recurrence is exact. Its nonnegative transfer matrix gives necessity and sufficiency of a Perron-root test. For stay probability below one half, the determinant reduces to the displayed cubic with no omitted trace condition; the exact cubic discriminant and its concave critical factor classify the roots. For probability at least one half, a positive-semidefinite representation makes the top eigenvalue a convex function of stepsize and rules out reentrance. The proof treats both endpoints, unstable equality cases, and arbitrary deterministic initial modes. The standalone checker independently verifies the symbolic identities and 520 rational instances. These finite calculations are supporting checks, not the proof for all real parameters.

## Originality — PASS, qualified

General spectral-radius equivalences for Markov jump linear systems already cover the transfer-operator machinery; they do not state the specialized learning-rate interval topology, algebraic critical persistence or its double-root collision for this two-curvature gradient iteration. Source inspections included the relevant sections of the accessible 2012 and 2014 primary works and the dated 2014 preprint record, and claim-level comparisons with them. Searches also covered alternate names (switching gradient iteration, Markov jump scalar multiplier, periodic gradient descent and reentrant stepsize stability). The 2000 paper on scalar jump perturbations was found but not available in full text and may contain an unrecognized equivalent specialization. Absence of an indexed match is not a uniqueness proof.

## Value — PASS

Unlike a routine statement that a small matrix is Schur stable, this result classifies a nonmonotone *set* of admissible learning rates and its sharp topology-changing parameter. For a strongly convex objective, anti-persistent sampling allows a larger learning rate to restore mean-square convergence after an intervening unstable range. The result is a complete, independently reproducible algebraic benchmark for Markov-dependent stochastic optimization, not an unsupported general performance promise.

## Scope and remaining risks

Classical jump-system spectral methods supply the baseline; the new object is their sharp specialized parameter phase diagram. A potentially stronger older conference source was abstract-only, and an unlocated equivalent special case remains possible. Only this scalar two-component model is proved. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
