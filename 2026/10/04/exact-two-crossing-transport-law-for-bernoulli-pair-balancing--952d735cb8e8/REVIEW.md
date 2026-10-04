# Review

## Correctness

PASS. The fixed-sum two-Bernoulli law depends affinely on the product, so the
difference between the two full probability mass functions is exactly a
second finite difference of the independent background. The generating
polynomial of that signed difference is
\[
(z-1)^2P(z).
\]
After deterministic shifts are removed, \(P\) has only negative real roots.
The real-rooted Descartes lemma therefore gives exactly two coefficient sign
changes, and positive endpoint coefficients force the \(+,-,+\) pattern.

Telescoping gives the CDF identity. Poisson-binomial log-concavity gives
unimodality, which reduces the integer \(W_1\) formula to twice the modal
background mass. Total variation, Kolmogorov distance, and stop-loss follow
without approximation.

## Originality

PASS, with a specific total-positivity residual risk. Hoeffding's full text
was inspected and already contains the general finite-difference machinery
for expectations under fixed-mean Bernoulli parameter changes; the classical
convex-order implication is therefore treated as prior coverage rather than
new content.

The inspected Wang paper proves Poisson-binomial unimodality, and the inspected
Roos paper develops finite-difference formulas for binomial approximation.
Neither states that a single balancing transfer has an exact \(+,-,+\)
probability-mass difference, a one-crossing CDF difference, or the exact
simultaneous formulas for total variation, Kolmogorov distance, \(W_1\), and
every stop-loss threshold.

Targeted searches for pair-transfer crossings, Wasserstein distance,
total-variation distance, peakedness, and majorization did not locate a
stronger statement implying the complete result.

## Value

PASS. Pair balancing is the elementary move underlying majorization arguments
for Poisson-binomial laws. The theorem upgrades the qualitative convex-order
effect of that move to an exact finite distributional calculus: where the mass
goes, how many crossings occur, the transport cost, and the stop-loss gain at
every threshold. The modal-mass coefficient in the \(W_1\) identity gives a
direct concentration-sensitive scale for one balancing operation.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK pmf_checks=125741 cdf_checks=161741 metric_checks=54000 stoploss_checks=197741 crossing_checks=18781 variation_checks=18781`.
