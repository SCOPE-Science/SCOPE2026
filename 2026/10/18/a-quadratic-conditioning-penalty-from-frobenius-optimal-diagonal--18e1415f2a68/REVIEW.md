# Scientific review

## Correctness
PASS. A positive-definite quadratic in the squared diagonal factors has one positive stationary point, which establishes the global Frobenius optimum without numerical optimization assumptions. Two original eigenvectors with identical diagonal-scaled norms certify the lower bound on condition number and characterize equality. The invariant two-dimensional spectral block yields the exact eigenvalue ratio, and the asymptotic follows by direct nonzero leading terms. The dimension-two equality case is calculated explicitly. The accompanying finite checks validate formulas but are not used to infer universal quantifiers.

## Originality
PASS under best-knowledge bibliographic comparison. Brarda et al. (arXiv:2606.22742) present the Frobenius congruence baseline and a spectral alternative but do not establish this globally optimized SPD-star example or the exact squared singular-limit coefficient. Qu et al. (arXiv:2209.00809) already develop optimal diagonal conditioning methods; Vandebril et al. (2005) establish tridiagonal unit-diagonal condition optimality, and Xu et al. (2012) document worsening of conditioning under different one-sided diagonal Frobenius-style preconditioning. These cover the general motivation or components, **not** the combined theorem about global Frobenius optimality, a sharp dimension boundary and a quadratic deterioration constant. Published mathematical-record and previous claim comparisons identified no equivalent; inaccessible/unindexed earlier specialized matrix-scaling calculations remain a real risk.

## Mathematical value
PASS. The 2026 spectral-value-selection work explicitly uses this Frobenius congruence objective as a baseline, while numerical SPD examples show relatively modest differences. The fully solved family proves a stronger structural distinction: optimally decreasing that actual loss can lead to a preconditioned SPD matrix that is quadratically more ill-conditioned than its already optimally diagonally scaled input. The threshold in dimension and precise coefficient make the diagnostic reproducible rather than an arbitrary numerical counterexample. This is a matrix-model result, not a universal claim about solver iteration counts.

## Scope and limitations
Real SPD stars, positive diagonal congruence, exact arithmetic, fixed integer dimension followed by a singular correlation limit. The proof is analytical; the numerical checker provides only finite reproducibility checks. Independent external validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
