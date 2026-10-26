# Scientific review

## Correctness — PASS
The SPD leading minors, unique least-squares normal equations, exact minimizers, singularity, squared residual gap and perturbed determinant are derived explicitly in `RESULT.md`. Minimality in dimensions one and two uses positivity of diagonal entries of \(A\) and \(A^{-1}\). The limiting condition number follows from rank two at the limit, continuity of two positive singular values, and an exactly linear determinant zero. A standalone exact-rational replay independently checks the core identities. Risks: no finite-precision robustness or adaptive selection assertion is made.

## Originality — PASS (self-review)
A 2022 SPAI-GMRES iterative-refinement source [1] uses this classical Frobenius objective, and earlier source [2] documents one-entry pattern enlargement; review [3] notes that an unfactored SPAI of an SPD matrix need not be SPD. These do not themselves state the stronger **one-entry rank-collapse and unbounded conditioning degradation despite objective decrease**. Published semantic record searches returned other approximate-inverse and incomplete-factorization results but no matching claim. Risks: full-text access to the 1997 foundational paper [4] was unavailable, so an unlocated equivalent case remains possible; searches cannot establish global priority.

## Mathematical value — PASS
Nonsingularity of the preconditioner matters for equivalence and conditioning of preconditioned linear systems. The finding supplies a minimal-dimension construction and a uniformly SPD, uniformly conditioned perturbation family showing that a strictly improved Frobenius objective by itself does not safeguard this property. This identifies a precise structural limit of a method used in iterative-refinement research. It does not assert an adaptive SPAI routine will select the added index, nor imply failure under stronger residual-norm safeguards.

Self-review: passed. Independent audit: not yet performed.
