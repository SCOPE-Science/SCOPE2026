# Review

## Correctness

PASS. Centering splits the mean absolute deviation equally between the positive and negative first moments. The negative-side second moment is bounded by the endpoint magnitude times its first moment, and the endpoint mass bounds that magnitude; the upper side is identical. This gives the exact endpoint-mass lower floor.

For the upper side, the mean cut turns half the mean absolute deviation into a covariance with a Bernoulli threshold indicator. Cauchy--Schwarz yields the cumulative-cut ceiling. Equality forces a two-level support, so strict supports with at least three atoms cannot attain the ceiling. The lower equality conditions force every interior atom to equal the mean, which is possible only for at most one interior atom. Explicit collapsing sequences prove sharpness of both unattained endpoints, and connectedness yields the full intervals.

## Originality

PASS, with explicit residual risks. Goroncy's 2009 paper is a close inequality source because it treats central absolute-moment scale units and identifies mean absolute deviation as exceptional, but its accessible statement concerns lower bounds for \(L\)-statistics over parent distributions rather than a fixed atom profile.

El Amir's work supplies the covariance viewpoint for mean absolute deviation; the accessible abstract does not state the fixed-profile standard-deviation comparison. Choulakian--Abou-Samra's complete arXiv text was inspected through its definition of mean absolute deviation, the classical \(D\le\sigma\) inequality, and the cut-norm representation. It does not give the endpoint-mass lower floor or cumulative-cut upper ceiling.

Berend--Kontorovich study a fixed binomial family and derive sharp estimates for its mean absolute deviation, not an extremal support-shape problem at arbitrary prescribed masses.

## Value

PASS. Mean absolute deviation and standard deviation are standard competing measures of dispersion. Once category frequencies are fixed, the classical inequality \(D\le\sigma\) leaves substantial information unused. The theorem gives the exact range created by that information, identifies which parts of the frequency profile govern the two endpoints, and supplies simple equal-frequency benchmarks.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK balance_checks=48000 lower_checks=24000 upper_checks=24000 strict_lower_checks=17034 strict_upper_checks=20503 binary_checks=3497 triple_equality_checks=24000 lower_approach_checks=8000 upper_approach_checks=8000 equal_mass_checks=198`.
