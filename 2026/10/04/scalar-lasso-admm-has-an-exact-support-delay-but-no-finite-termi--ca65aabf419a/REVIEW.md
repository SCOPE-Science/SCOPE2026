# Review

## Correctness
PASS. The proof starts from the exact scaled ADMM update for scalar Lasso, handles the strict soft-threshold boundary, derives the first activation index, proves the active sign persists, and solves the resulting affine recurrence for all subsequent iterations. The nonzero geometric factor establishes nontermination for every finite \(\rho>0\) under the stated initialization. Exact-rational replay is supplemental only.

## Originality
PASS. The closest general literature proves eventual activity identification and local linear convergence. The directly relevant 2016 source instead states finite whole-algorithm convergence for the \(K=I\) anisotropic case. The scalar recurrence gives the opposite conclusion and an exact onset formula. Targeted searches over Lasso/ADMM, finite identification, finite convergence, soft thresholding, and the named source found no implication-equivalent correction.

## Value
PASS. The scalar model is the irreducible one-coordinate Lasso instance, not an arbitrary parameter slice. Separating finite support identification from finite iterate termination corrects a mathematically substantive claim and yields an exact penalty tradeoff between earlier identification and slower active-phase contraction.

## Closest literature and limitations
The closest inspected sources are arXiv:1412.6858, DOI 10.1109/ICASSP.2016.7472579, and arXiv:1606.02116. The claim is limited to \(b>\lambda>0\), zero split/dual initialization, fixed finite penalty, and standard unrelaxed scaled ADMM; arbitrary initializations and multivariate designs are not classified. An unindexed correction or note could contain the same scalar observation.

Same-model review: passed. Independent audit: not yet performed.
