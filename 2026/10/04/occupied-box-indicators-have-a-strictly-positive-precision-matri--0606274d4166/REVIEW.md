# Review

## Correctness

PASS. The diagonal and off-diagonal covariance formulas follow directly from emptiness probabilities and two-event inclusion--exclusion. The off-diagonal sign is strict for every positive category pair.

The covariance matrix is singular for one draw because the occupancy indicators sum to one, with no other null direction. For two or more draws, a zero-variance linear combination would have to take the same value on every singleton and pair occupancy pattern. Singleton patterns force all coefficients equal; pair patterns force that common coefficient to vanish. This proves positive definiteness without relying on numerical eigenvalue tests.

After diagonal normalization, the covariance matrix is \(I-B\) with \(B\) symmetric and strictly positive off the diagonal. Positive definiteness forces the spectral radius of \(B\) below one, so the inverse is the convergent nonnegative Neumann series \(\sum_{k\ge0}B^k\). The identity and first-order terms make every inverse entry strictly positive.

## Originality

PASS, with a residual risk from classical matrix and occupancy literature. Joag-Dev--Proschan establish multinomial negative association. Dubhashi--Ranjan's complete open report establishes negative association and negative regression for empty-bin indicators. Bogachev--Gnedin--Yakubovich give the exact fixed-sample cross-term appearing in the variance of the occupied-box count.

Those sources cover the pairwise covariance sign and its broader dependence setting. The inspected statements do not give the exact rank transition at two draws, strict positive definiteness for the whole indicator vector, entrywise positivity of the precision matrix, or the resulting full-order partial-correlation sign.

Searches using occupancy indicators, empty cells, precision matrices, inverse covariance, Stieltjes matrices, and nonsingular M-matrices did not locate that combined statement. Because the last step is an elementary matrix consequence once positive definiteness is proved, an older equivalent formulation remains a real residual risk.

## Value

PASS. Occupancy-indicator vectors occur in distinct-species counts, empty-cell statistics, coupon-collection problems, and balls-and-bins models. Negative association explains pairwise repulsion, but the inverse covariance controls linear conditioning and least-squares residual dependence. The theorem supplies a global covariance-geometry statement not contained in pairwise covariance signs: a sharp rank transition, nonsingularity from two draws onward, and a fully positive precision matrix.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK formula_checks=69126 offdiag_checks=46630 rank_one_draw_checks=3524 pd_minor_checks=19612 inverse_positive_checks=100838 partial_sign_checks=40613 enumeration_checks=4707`.
