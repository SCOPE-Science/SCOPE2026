# Scientific review

## Correctness (C): PASS

The candidate vectors agree with the two original inverse-leading algorithms through the third step. The exact relation \(Av_2=(v_1-mAv_1)/\nu\) gives the local indicator ratio without approximation. A spectral-moment identity reduces the universal claim to a variational optimization over probability measures supported on the spectral interval. The first variation of the complementary moment functional is strictly concave in the spectral variable and consequently forces endpoint support. A one-variable polynomial with exactly one positive root, established by a one-sign-change coefficient argument, completes the sharp global optimization. Three-eigenvalue perturbations prove the sharp infimum while keeping the third step nonbreaking. The decoded exact-rational verifier reports 4,692 checks in four groups; finite computations support the algebra but do not prove the infinite result.

## Originality (O): PASS, subject to historical-priority risk

Lund and Schweitzer, arXiv:2610.21603v1, prove only the strict mixed-channel ordering of local indicators on positive-definite matrices; the analyzed Algorithms 1–2, Theorem 8 and Appendix A do not state this sharp condition-number envelope or its cubic spectral extremizer. Jagels–Reichel (2009) develops orthogonal Laurent recurrences, not the mixed/split local candidate normalization ratio. Rinelli–Vandebril (2026) gives broader spectral-measure machinery for block Krylov spaces, but does not imply the numerical sharp bound without additional optimization. A related accessible earlier claim concerns *indefinite* third-step breakdown and is not a positive-definite condition-only inequality. Published mathematical-record searches for equivalent language, formulas and variants yielded no directly covering record. Classical extremal moment inequalities and incomplete indexing create a genuine, explicitly retained priority risk.

## Mathematical value (V): PASS

The 2026 algorithm analysis establishes a qualitative local stability ordering. The new exact best condition-dependent guarantee quantifies how strongly the local predictors can separate, and shows an unexpectedly unbounded separation in the well-conditioned limit. Its structural endpoint law and cubic optimum identify the worst spectral profiles and clarify why a nonbreaking instance never attains equality. This is directly relevant to choosing an extended-Krylov basis construction, but it is not a prediction of actual rounding error or overall convergence. The result is restricted to the third candidate step and real SPD matrices.

## Closest literature and limitations

The principal source is Lund–Schweitzer (2026), particularly Algorithm 1, Algorithm 2, Theorem 8 and Appendix A. Jagels–Reichel (2009), Rinelli–Vandebril (2026), and Simoncini–Wang (2025) provide related recurrence, spectral, or orthogonalization context. The theorem does not extend its local guarantee to subsequent steps, inexact inverses, indefinite matrices, or global approximation accuracy. Historical uniqueness is not independently certified.

Self-review: passed. Independent audit: not yet performed.
