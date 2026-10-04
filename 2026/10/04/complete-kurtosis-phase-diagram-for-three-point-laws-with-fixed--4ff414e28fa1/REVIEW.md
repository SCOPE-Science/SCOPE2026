# Review

## Correctness

PASS. Positive-affine invariance reduces every ordered three-point support to
\[
(0,t,1),
\qquad
0<t<1.
\]
The fourth standardized moment has the exact derivative
\[
\kappa'(t)
=
\frac{4abc\,t(1-t)}{V(t)^3}
\left[(3b-1)t+(3c-1)\right].
\]
Since the prefactor is positive, one affine bracket gives the complete classification. Its root is interior exactly when the two endpoint masses lie on the same strict side of \(1/3\). The sign change distinguishes minimum from maximum. Direct substitution gives the closed stationary kurtosis, while the two boundary limits are ordinary Bernoulli kurtoses. Continuity gives the complete attainable sets.

The embedded checker independently differentiates through the central moments with exact fractions and reproduces the factorization and all phase cases.

## Originality

PASS, with a residual older moment-space risk. The full five-page Móri--Rohatgi--Székely paper was inspected. It proves general sharp skewness--kurtosis inequalities and special distributional results, but does not formulate a fixed three-mass support optimization.

The Sharma--Bhandari archive preprint is directly relevant to moment inequalities and supplies the exact archive date. Only its abstract and publication metadata were accessible through the search path used, so it is retained as a residual-access risk rather than treated as a whole-document noncoverage certificate.

The full open Jammalamadaka--Taufer--Terdik article was inspected through its introduction and kurtosis section. It systematically treats cumulant-based kurtosis measures and parametric families, but not this fixed-probability three-point coding problem.

Targeted database and web searches for three-point, weighted-three-value, fixed-probability, categorical-score, and standardized-fourth-moment formulations did not locate the phase diagram or stationary formula.

## Value

PASS. Three-level ordinal and categorical variables frequently have fixed category frequencies but noncanonical numerical scores. Kurtosis can therefore change solely because of the coding. The theorem gives the entire coding-induced range and a sharp qualitative transition at the natural mass \(1/3\), including a unique support geometry when an interior extremum exists. This is a complete structural classification rather than a numerical table.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK derivative_checks=30000 boundary_checks=60000 uniform_checks=55 stationary_checks=23630 phase_checks=9701 monotone_checks=20286`.
