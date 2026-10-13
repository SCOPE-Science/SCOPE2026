# Scientific review

## Correctness — PASS

Exact diagonalization of the symmetric two-by-two inverse-diagonal residual yields one positive and one negative eigenvalue, with explicitly computed magnitudes. A rank-one update has one unchanged eigenvalue and one normal-to-signed-quadratic ratio; integrating its sign interval under the absolute Cauchy density proves the probability formula. The unique maximum follows from a monotone quartic. A simple pole and a positive-density transverse zero set respectively establish the unregularized sharp tail and the positive-ridge infinite first moment. An exact rational witness and the standalone standard-library verifier check key arithmetic. The two-dimensional scope, a.s. nonzero core, strict inequalities, and exact-arithmetic assumptions are explicit. Remaining risk: none identified in the algebra; finite Monte Carlo experiments cannot by themselves certify asymptotic behavior.

## Originality — PASS, with a specifically stated residual literature risk

The new quantitative claim is an exact Gaussian positivity-loss law and its global supremum for an SPD double-saddle-point Schur family, together with an exact heavy-tail constant and a proof that fixed positive signed-core ridge regularization still gives positive failure probability and infinite unconditional mean. Liang–Huang 2026 provides exactly the underlying update and conditional error bounds, but its inspected full Section 3 contains no equivalent unconditional probability, global envelope or ridge-integrability theorem. Nakatsukasa–Park 2023 already demonstrates deterministic unbounded instability for general indefinite Nyström, so that known generic fact is expressly excluded from novelty. The newer Chen–Nakatsukasa–Narendran–Park 2026 paper uses a different core-selection algorithm; only its abstract could be accessed, leaving a real risk that its full text or other older probability literature contains a stronger equivalent consequence. Searches do not prove uniqueness, and no independent review is claimed.

## Value — PASS

A Schur approximant must be SPD to meet the hypotheses of the motivating preconditioned eigenvalue analysis. The theorem quantifies the probability that a one-probe Gaussian correction violates that necessary hypothesis even when every exact block matrix is SPD, the other Schur term is computed exactly, and the entire exact Schur complement is SPD. The nonzero failure risk is not merely a fragile deterministic example: it has a closed-form probability, an exact global extremal risk, and infinite expected norm both with and without a fixed positive core ridge. This differentiates probabilistic reliability from conditional approximation-error guarantees and identifies a concrete limitation of positive scalar shifts applied to indefinite random cores.

## Closest literature and limitations

Liang and Huang, arXiv:2609.01031v1, Section 3, Algorithm 1 and (3.3), supplies the signed core; the high-probability error bound is conditional. Nakatsukasa and Park, arXiv:2212.01127, Section 1.1, already covers deterministic indefinite Nyström blow-up. The accessible abstract of Chen et al., arXiv:2608.20531, concerns a distinct two-sided sketched least-squares core but the full text was inaccessible, a substantive residual originality risk. The theorem does not address higher ranks, sparse probes, finite precision, adaptive algorithms or stabilized alternatives. Independent audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
