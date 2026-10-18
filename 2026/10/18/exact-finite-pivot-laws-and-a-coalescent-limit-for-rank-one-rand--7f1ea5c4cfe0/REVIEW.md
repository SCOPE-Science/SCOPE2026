# Review of rank-one randomized Jacobi absorption law

## Correctness — PASS

The orthogonal-similarity invariant retains a scalar identity plus one rank-one term. A genuine Jacobi pivot must eliminate one, and only one, active rank-one coordinate, while a zero pivot leaves support unchanged. The support-size transition probability is exactly the ratio of active unordered pairs to all pairs. Independent pivot samples give independent geometric holding times. Means, variance, probability-generating function, the exponential limit with uniform tail expectation, and the block hypergeometric recursion have complete proofs in RESULT.md. Exact rational recurrence checks and direct matrix identities agree with the derivation. Finite simulations are not used as infinite proofs.

## Originality — PASS within inspected evidence, not a uniqueness certificate

Detherage and Shah's recent uniform-pivot analysis gives algorithmic convergence guarantees but does not state the exact rank-one support-count death chain and its sampled-step law in the relevant inspected sections. Möhle and Pitters establish the pre-existing coalescent law; the contribution here is its precise Jacobi stopping-time representation and the block recurrence. Targeted searches for equivalent rank-one Jacobi, coalescent, stopping-time, and generalized pivot claims did not reveal implication by another inspected theorem. Residual risk: classical rank-one eigensolver and less-indexed Jacobi sources may treat the same special benchmark. The source comparisons are not exhaustive.

## Value — PASS

Uniform random pivoting is an actively studied design for Jacobi eigenvalue algorithms, and a scalar-identity rank-one perturbation is a canonical completely solvable spectral model. This result obtains the entire stopping-time law for arbitrary support/dimension, its quadratic expected pivot cost and nondegenerate limit, and the exact effect of increasing block size. It quantitatively distinguishes uniform blind selection from always selecting an active off-diagonal (\(n-1\) successful pair pivots). These are motivated spectral-algorithm cost facts, not an arbitrary scalar substitution or a purely numerical observation.

## Scope and residual risks

Exact arithmetic, rank one, and independent uniform samples are essential. The coalescent distribution itself is established prior work; only its randomized-Jacobi identification and explicit block stopping law are assessed here. Unindexed equivalent sources remain possible; mathematical correctness does not imply an independent novelty certificate.

Self-review: passed. Independent audit: not yet performed.
