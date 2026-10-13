# Scientific review: rank-two Nyström misalignment boundary

## Correctness — PASS

The identity follows from the exact rank-two Nyström eigendecomposition for the stated positive-definite three-by-three matrix and the normalization specified by Frangella–Tropp–Udell. The generalized eigenvalue polynomial and the location of the unaffected eigenvalue turn the condition-number comparison into one scalar trace/determinant inequality. Factoring its difference produces a strictly positive factor times the claimed cubic. The cubic's endpoint signs and strict convexity give a unique sharp transition. Exact rational arithmetic proves the three-by-three witness, and continuity yields a positive-measure Gaussian-sketch event. The included standalone checker verifies the critical finite algebraic certificates; it does not substitute enumeration for the proof. The minimal-dimension claim separately checks rank-one and full-rank preconditioning.

## Originality — PASS, with residual risk

The closest defining source is Frangella, Tropp, and Udell, *Randomized Nyström Preconditioning*, arXiv:2110.02820, equations (1.2)–(1.3), Proposition 5.3, and Theorem 5.1. Those give deterministic approximation-error and sufficiently-large-sketch expectation bounds, not the exact sign of conditioning change for a fixed rank-two orientation. Carson and Daužickaitė, *Single-Pass Nyström Approximation in Mixed Precision*, DOI:10.1137/22M154079X, sections 3–4, treat finite precision and numerical condition-number behavior but no matching threshold. Bock and Andersen, *Preconditioner Design via the Bregman Divergence*, arXiv:2304.12162, sections 2 and 5, use a different low-rank preconditioner and cannot imply the result by a parameter substitution. Published mathematical-record searches for Nyström rank-two deterioration, misalignment, condition-number amplification, and equivalent preconditioners produced no matching implication. This is not a proof that all literature has been indexed; potential obscure eigenvector-perturbation analyses remain a priority risk.

## Value — PASS

Nyström preconditioning is used precisely to improve spectral conditioning, yet the defining construction makes no per-realization no-worsening guarantee. The proved cubic provides an exact parameter-dependent design boundary rather than a generic observation that approximations may be poor: for every positive regularizer and spike contrast there is a robust deterioration region, and rank two in dimension three is minimal. The Gaussian positive-probability consequence shows relevance to the randomized method rather than to one pathological exact sketch. These facts sharpen interpretation of probabilistic large-sketch guarantees and identify which orientation failures they do not preclude. The analysis concerns condition-number surrogates, not individual PCG runtime or iteration monotonicity.

Self-review: passed. Independent audit: not yet performed.
