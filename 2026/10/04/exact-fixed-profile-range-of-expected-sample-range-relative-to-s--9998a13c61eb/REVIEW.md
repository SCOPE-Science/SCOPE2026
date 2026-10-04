# Review

## Correctness

PASS. The expected sample range is exactly the positive gap sum
\[
\sum_j
\left[
1-P_j^N-(1-P_j)^N
\right]d_j.
\]
The centered parent variable is the same positive gap combination of centered cumulative-cut indicators. Their \(L^2\) norms produce the lower cut constant through the triangle inequality, with strictness for at least three atoms and sharpness under one-dominant-gap collapse.

For the upper side, the exact maximum and minimum mass functions turn the expected range into a covariance with the cellwise secant slopes of
\[
u^N+(1-u)^N.
\]
Strict convexity makes those scores strictly increasing, so the Cauchy--Schwarz equality support is admissible and unique up to positive affine change. Connectedness gives every intermediate value.

## Originality

PASS, with a residual projection-literature risk. Papadatos's complete 2014 arXiv article was inspected through its introduction, classical iid range bound, formulation of the general dependent range extremal problem, and main bounding setup. It optimizes under mean--variance information rather than a prescribed finite probability vector.

Goroncy--Rychlik's complete open article was inspected through its literature review, general projection framework, and spacing section. It develops standardized expectation bounds for unrestricted or shape-restricted parent classes but does not state the fixed-probability support-shape interval here.

The closest published-record finding concerns correlation between sample minimum and maximum on a three-point parent as the probability weights vary. The current theorem instead fixes the probability vector, varies all ordered support locations, and optimizes the expected range itself relative to the parent standard deviation.

## Value

PASS. The sample range is a classical scale statistic, and sharp bounds in standard-deviation units have been studied since the 1940s. In categorical, rounded, or finite-support models the parent category probabilities can be known or estimated independently of the numerical spacing assigned to categories. The theorem gives the complete efficiency envelope created by that extra information, including an explicit best scoring system and a sharp worst-cut limit.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK gap_checks=18000 extreme_checks=18000 covariance_checks=18000 lower_checks=18000 upper_checks=18000 score_order_checks=18000 upper_equality_checks=18000 lower_strict_checks=15048 boundary_checks=15048 direct_enum_checks=600 binary_checks=2952`.
