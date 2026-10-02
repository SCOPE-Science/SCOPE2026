# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **PASSED**.

## Final claim

For every integer refinement factor \(r\ge2\) and every Richardson depth \(d\), the generalized Romberg rule obtained from nested composite trapezoid grids has strictly positive final sample weights, exactness through degree \(2d+1\), and total absolute weight \(b-a\); its largest weight is \(H\prod_{j=1}^d(1-r^{-2j})^{-1}\), so the collected rule is optimally conditioned for bounded absolute sample errors.

## Correctness — PASS

The closed Richardson coefficients solve the Vandermonde cancellation equations. After collecting the nested trapezoid grids, a finest-grid node receives an alternating tail of level contributions. Writing the contribution magnitudes as \(A_k=|c_{d,k}|r^{-k}\), direct division gives \(A_{k+1}/A_k=r^{-1}q^{k+1}(q^{d-k}-1)/(q^{k+1}-1)>r-r^{-1}>1\) for \(q=r^2\), so every alternating tail has the sign of its final term and every collected weight is positive. Positivity plus exact integration of constants gives total absolute weight \(b-a\), hence optimal bounded-absolute-noise amplification. Euler–Maclaurin cancellation gives degree \(2d+1\) exactness. Independent exact-rational checks over \(2\le r\le7\) and \(1\le d\le5\) reproduced positivity, normalization and all polynomial moments through degree \(2d+1\).

## Originality — PASS

Generalized Richardson extrapolation on geometric meshes and generalized Romberg applications are classical, but the inspected Sidi material does not state positivity of the final collected nested-trapezoid sample weights for every integer refinement factor, nor the resulting exact \(\ell_\infty\) noise norm. Farzi's positive-weight statement concerns a different extrapolation construction for nonlinear Fredholm equations. No earlier published-record hit was found for the audited all-integer-refinement positivity theorem.

## Scientific value — PASS

Positive final weights remove cancellation in the implemented quadrature rule and give an exact stability constant while retaining arbitrarily high Richardson order. Extending this property from the familiar dyadic case to every integer refinement factor is a natural numerical-analysis question with direct conditioning consequences.

## Residual risks and limits

- The complete Sidi (1997) theorem text could not be inspected after the author-hosted PDF fetch timed out; an older equivalent collected-weight statement remains a concrete historical risk.
- The theorem concerns nested uniform trapezoid grids with integer refinement only.
- It analyzes exact final aggregation, not floating-point cancellation inside an extrapolation tableau.
- The complete Sidi (1997) theorem text was not obtained, leaving a historical-equivalence risk.

This is a mathematical review, not formal proof-assistant verification or external certification.
