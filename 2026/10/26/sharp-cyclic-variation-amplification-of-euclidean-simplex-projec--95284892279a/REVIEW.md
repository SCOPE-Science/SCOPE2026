# Review of the cyclic-variation simplex modulus

## Correctness

The KKT characterization yields a continuous piecewise-affine map with local active-set centering matrices. A cyclic-gradient transport decomposition reduces every local variation operator norm to indicators of connected cyclic intervals. For an active support split into two arcs, the exact quotient is \((br+as)/(a+b)\); the required separator count is \(a+b+r+s\le n+2\). Two complementary integer inequalities give the claimed dimension formula, and alternating-run constructions realize equality by actual projected input pairs. The `checker.py` exact-rational diagnostics independently corroborate finite cases but are not relied upon to prove the universal claim.

## Originality

Wang and Carreira-Perpiñán (arXiv:1309.1541), Condat (HAL-01056171v1), and Duchi et al. (ICML 2008) describe the simplex projection algorithm, KKT threshold, and active-set structure rather than the cyclic-total-variation perturbation modulus. Lellmann et al. (SSVM 2009) consider spatial TV with simplex constraints rather than this stability map. The closest published same-map result, *Sharp \(\ell_4\) Stability of Metric Projection onto a Probability Simplex*, computes an \(\ell_4\) operator norm, not the cycle-gradient quotient. Its full proof was compared. A hidden equivalent result in the broader literature cannot be excluded.

## Mathematical value

The theorem supplies a natural sensitivity invariant for probability-vector projection when coordinates carry a cyclic adjacency geometry. It quantifies an otherwise misleading distinction: individual variation decreases while variation of a perturbation can grow without dimension-independent control. The exact arithmetic defect and constructive extremizers classify the sharp finite-dimensional behavior.

## Limits

The calculation is for real Euclidean simplex projection and equal-weight cycle edges, not weighted or general graph variations. It has not received independent scientific auditing.

Self-review: passed. Independent audit: not yet performed.
