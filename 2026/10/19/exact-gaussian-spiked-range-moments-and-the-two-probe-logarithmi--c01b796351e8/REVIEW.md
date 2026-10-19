# Scientific assessment

## Correctness — PASS
The proof derives the inverse-Gram Schur complement for a Gaussian one-spike subspace, identifies independent chi-square variables by Gaussian rotational invariance, and computes the exact beta-transformed squared-error law. Gamma density arguments prove the sharp moment regime split and fixed-threshold tail, including the logarithmic boundary. The embedded verifier passed 957 algebraic/high-precision checks. Finite checks corroborate rather than prove the quantifiers; the formal mathematics is given in `RESULT.md`.

## Originality — PASS (residual priority risk)
Palitta and Portaro define the standard and row-aware random subspaces and give expectation-norm bounds under their specified rank/oversampling assumptions. Saibaba, Gu, and Diouane and collaborators establish broad randomized iteration/error estimates; classical Gaussian inverse-Wishart facts explain the ingredients. The contribution assessed is the **exact all-probe left-range loss distribution, full positive moment spectrum, two-probe critical logarithm, and finite-threshold rare-event constant** on the natural equal-tail spike family. The isolated one-probe heavy-tail mechanism and the two-pass algorithm are established phenomena and are not asserted as new. Equivalent specialized computations in other literature may exist and priority is not independently certified.

## Value — PASS
The two-probe boundary is the smallest oversampled left sketch for a rank-one spike, and the sharp phase laws distinguish high-probability accuracy from rare-event-dominated mean loss. The explicit comparison of one versus two matrix-power passes gives a benchmark for selecting sketch width and measuring expected Frobenius quality.

## Scope and limitations
Only fixed-dimensional real Gaussian left-range projections, exact arithmetic, the diagonal equal-tail spike and fixed moment order are proved. This is not a result about the optional final rank-one SVD truncation or a general-spectrum guarantee.

Self-review: passed. Independent audit: not yet performed.
