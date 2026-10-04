# Review

## Correctness

PASS. The minimized pinball loss is exactly a positive linear functional of the adjacent support gaps, with coefficient
\[
\min\{(1-\tau)P_j,\tau(1-P_j)\}
\]
at cut \(j\). The centered support is the same gap combination of centered cut indicators. This yields the lower bound by the triangle inequality, with strictness for at least three distinct atoms and a one-dominant-gap sequence proving sharpness.

For the upper bound, the probability-cell average of the mean-zero quantile score has covariance with each cut indicator equal to the corresponding loss coefficient. Thus minimized loss is exactly a covariance with that projected score, and Cauchy--Schwarz gives the upper constant. Conditional variance gives the explicit projection deficit. The projected score has at most three levels, which proves the complete upper-attainment classification. Connectedness fills every interior value.

The embedded exact-rational replay independently checks all algebraic identities and endpoint mechanisms on generated finite profiles.

## Originality

PASS, with an explicit older convex-loss literature risk. The complete Gilat--Hill article was inspected. It defines the same quantile-locating asymmetric absolute functional and proves its minimizers are quantiles, but its sharp theorem concerns distance from the mean to a quantile in central-absolute-moment units, not the minimized loss in standard-deviation units at a fixed atom profile.

The complete Xue--Titterington author manuscript was inspected, including its empirical discrete discussion and its generalized weighted \(p\)-folded CDF section. Its weighted mean absolute deviation from a \(p\)-quantile is a constant multiple of the minimized check loss here, but the paper gives a CDF-area representation rather than a fixed-profile variance-normalized range.

Steinwart--Christmann is a potentially confusing broader pinball-loss source because it uses the phrase “variance bounds,” but its object is excess-loss variance for nonparametric learning. It does not compare the population minimum pinball risk with the response standard deviation.

Targeted semantic-database and literature searches did not locate the cut-ray lower endpoint, probability-cell projection upper endpoint, or complete attainment classification.

## Value

PASS. Minimum quantile loss is the canonical unconditional scale associated with quantile regression and asymmetric absolute-error risk. Standard deviation is the canonical quadratic scale. Their ratio is not determined by atom probabilities alone, but the theorem gives its entire possible range when those probabilities are fixed, including exact extremal mechanisms and a transparent loss-of-information term when the target quantile cuts through an atom cell.

At \(\tau=1/2\), the result becomes an exact fixed-frequency comparison between mean absolute deviation from a median and standard deviation, with simple closed forms for equally weighted supports.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK direct_checks=2500 covariance_checks=2500 lower_checks=2167 upper_checks=2500 formula_checks=2500 two_point_checks=333 three_attain_checks=1000 boundary_checks=4667`.
