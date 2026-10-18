# Scientific self-review

## Correctness — PASS
The update matrix follows from two coordinate-overwrite equations. At unit relaxation the exact scalar product determines both rates. At overrelaxation the sampled matrices, characteristic discriminants, strict common-in-expectation Lyapunov witness \(H\), and positive covariance growth witness \(Q\) were independently reconstructed with exact rational arithmetic from the packaged `verify.py`. Positive definiteness certificates and the covariance/dual identities imply opposite mean-square behaviors for every-time dynamics. The open-neighborhood claim follows from strict inequalities and eigenvalue continuity. The exact model is homogeneous and has independent sweep draws, and no actual floating-point assertion is made.

## Originality — PASS (same-model, residual risk)
Published work on roundoff and general stochastic matrix splitting contains important ingredients, but the primary materials inspected do not identify the exact dependence reversal between two joint coefficient laws having the same marginals. In particular, the 2021 stochastic-rounding theory uses mean-independent errors whereas opposite within-sweep coupling violates that conditional assumption, and the published two-coordinate delay law concerns a different random operation. This is not merely a renamed scalar iid product: the overrelaxed matrices are full-rank and noncommuting, and the counterexample requires distinct exact covariance and Lyapunov certificates. The 2026 motivating manuscript was accessible only as an abstract and remains the most important unresolved source-comparison risk. General switched-system theory could contain an equivalent specialized example; independent review is still needed.

## Value — PASS
This is a robust motivated boundary to a common correlation-design intuition for imprecise linear iterations: negative dependence improves unit-relaxation contraction but can destroy second-moment stability at overrelaxation even though the individual matrices remain Schur-stable. The same marginal cost/precision is held fixed. The exact witnesses distinguish random-product stability from deterministic single-sweep spectral tests and can inform cautious selection of dependence models. It does not claim hardware superiority or a universal SOR phase diagram.

## Limitations and closest literature
Connolly–Higham–Mary (2021) addresses ordinary stochastic rounding and conditional mean independence; Fox–Parker (2017) treats stochastic Gibbs equivalents of matrix splittings; Richtárik–Takáč (2019) gives general stochastic linear-system formulations. The new theorem is a specific exact-arithmetic joint-coefficient counterexample, not an analysis of those algorithms' full assumptions. Full text of Lindquist et al. (2026) was unavailable. Published generic random-product results remain a source of possible indirect overlap.

Self-review: passed. Independent audit: not yet performed.
