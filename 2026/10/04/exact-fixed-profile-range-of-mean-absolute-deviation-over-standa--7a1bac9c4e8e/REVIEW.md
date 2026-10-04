# Review

## Correctness

PASS. After centering, write the common positive and negative first moment as
\[
A=\mathbb E(Y_+)=\mathbb E((-Y)_+).
\]
The pointwise bounds
\[
y^2\le a(-y)
\]
on the negative side and
\[
y^2\le by
\]
on the positive side give
\[
\sigma^2\le A(a+b).
\]
The endpoint masses force
\[
a\le A/p_1,
\qquad
b\le A/p_m,
\]
which yields the stated lower constant and its equality conditions.

For the upper constant, the indicator of lying above the mean has covariance \(A\) with the centered variable. Cauchy--Schwarz gives exactly the cumulative-cut constant. Equality would force a two-level support, so the upper endpoint is unattained for three or more distinct atoms.

Connectedness of the strict support cone supplies all intermediate values. Exact-rational replay checks the inequalities and endpoint constructions.

## Originality

PASS, with a residual older finite-population literature risk. Korwar's complete primary paper was inspected through its discrete mean-absolute-deviation section and characterization results. It gives a different function-of-a-random-variable inequality and does not optimize the MAD-to-standard-deviation ratio over support geometry at fixed atom masses.

The complete MAD section of Aghili-Ashtiani was inspected. It conditions on how many observations lie below or above the mean and proves range-based upper bounds. It does not give the lower endpoint-mass bound, the cumulative-mass upper ratio, or the exact attainable-set classification for arbitrary unequal probability profiles.

Berend--Kontorovich is a close named-family source because it sharply compares binomial MAD with standard deviation. Its model fixes both the support and the probability structure and therefore does not imply the support-geometry theorem.

Targeted database and web searches for equivalent fixed-profile, frequency-profile, and support-optimization formulations did not locate a dominating result.

## Value

PASS. The ratio of mean absolute deviation to standard deviation is a standard scale-free comparison of two dispersion measures. Once the atom probabilities are fixed, the theorem gives its complete geometric freedom rather than a one-sided universal estimate. The endpoint-mass lower barrier quantifies how much a fixed amount of probability at the support extremes prevents standard deviation from dominating MAD, while the upper formula identifies exactly when the classical bound \(D\le\sigma\) can be approached.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK random_lower_checks=30000 random_upper_checks=25620 two_point_checks=4380 three_point_endpoint_checks=8000 equal_weight_checks=198 lower_path_checks=6000 upper_path_checks=6000`.
