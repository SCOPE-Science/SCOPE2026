# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The exact modal probability was checked from the equiprobable multinomial pmf. The covariance determinant and inverse for the first \(m-1\) coordinates are
\[
\det\Sigma_m=m^{-m},
\qquad
\Sigma_m^{-1}=m(I+\mathbf1\mathbf1^\top),
\]
and the modal Mahalanobis exponent is
\(-m^2\theta(1-\theta)/(2N)\).

The growing-category expansion follows from the standard shifted log-Gamma expansion with a remainder uniform for shifts in a compact interval. At a mode the shifts lie in \([-\theta,1-\theta]\), so the denominator remainders sum to
\(O_K(m^{K+2}/N^{K+1})\). The first two phase averages were checked algebraically:
\[
A_2(\theta)=1/6+\theta(1-\theta),
\qquad
A_3(\theta)=\tfrac12\theta(1-\theta)(5-4\theta).
\]
These identities produce the Gaussian exponent, the universal
\(-(m^2-1)/(12N)\) mismatch, and the next phase-dependent term.

For the continuity-corrected cell, dividing the Gaussian integral by its density at the modal center gives an exact expectation over an iid uniform cube. The linear term has variance at most \(m^3/(12N^2)\), which vanishes when \(m^2/N\) is bounded. The quadratic term converges to \(c(1+Z^2)/24\) by the law of large numbers and central limit theorem. Boundedness of the cell exponent in the critical regime justifies passage to expectations and yields
\(e^{-c/24}(1+c/12)^{-1/2}\).

Numerical evaluations of the exact factorial formula at several nondivisible and divisible parameter pairs were consistent with the first-, second-, and higher-order displayed corrections. These checks support but are not used in place of the analytic proof.

## Originality

**PASS, to the best of our knowledge.**

Elezović (arXiv:2609.20229) was inspected in full-text HTML. It proves a complete local Bernoulli-polynomial expansion for bounded displacement with a fixed multinomial probability vector and explicitly discusses the symmetric central multinomial specialization. It also states that its all-orders result trades a fixed local range for completeness. No growing-number-of-categories uniform remainder, critical \(m\asymp\sqrt N\) distortion, correction hierarchy, or Gaussian-cell critical profile was located there.

Ouimet (arXiv:2001.08512; J. Statist. Plann. Inference 2021) was inspected around the local limit theorem, the Gaussian comparison, and the jittered unit-cell construction. Its local error notation permits dependence on the fixed dimension and probability vector. Its jittered total-variation bound and discussion of continuity correction are closely related context, but no modal relative-error transition or \(m^2/N\to c\) cell profile was located.

Searches using combinations of `multinomial`, `growing dimension`, `growing number of categories/cells`, `local limit theorem`, `central multinomial coefficient`, `normal approximation`, and `continuity correction` located the fixed-dimensional results above and general random-allocation/high-dimensional multinomial literature, but no source stating the package proved here.

The principal residual originality risk is older lattice local-expansion literature, including Bikyalis (1969), Lazakovičius (1969), and Bhattacharya--Ranga Rao, together with classical factorial asymptotics for central multinomial coefficients. These sources can recover ingredients and special cases; their full texts were not all inspected. The divisible symmetric first correction is elementary and is not claimed as a new standalone formula. The originality claim is restricted to the uniform growing-category modal expansion with explicit phase control, the resulting hierarchy of dimension thresholds, and the critical unit-cell profile.

## Value

**PASS.**

The result turns a recent fixed-category all-orders expansion into a growing-dimensional phase diagram. It identifies the exact failure factor of the naive Gaussian local approximation at \(m\asymp\sqrt N\), shows how successive explicit corrections push relative accuracy to \(N^{2/3},N^{3/4},\ldots\), and quantifies what the standard multivariate continuity correction does at the first critical scale. These statements give sharp local diagnostics for high-dimensional multinomial normal approximations rather than only sufficient error bounds.

## Scientific limitations retained

The analysis is restricted to equiprobable cells, divergent expected occupancy \(N/m\), and modal local probabilities. It does not establish a global distributional approximation threshold, does not treat sparse occupancy, and does not optimize the shape of the continuity-correction cell. Older lattice-expansion literature remains a residual originality risk.
