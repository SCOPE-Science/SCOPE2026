# Review

## Correctness

PASS. Both statistics are normalized degree-two \(U\)-statistics. Exact pair-overlap counting reduces their covariance to two quantities: the covariance of the two kernels on the same observation pair and the covariance of their first conditional projections when only one observation is shared.

For standard exponential sampling the same-pair term is \(2\). The conditional projections are
\[
a(x)=x-1+2e^{-x}
\]
and
\[
b(x)=x^2/2-x+1,
\]
and direct exponential integration gives
\[
\mathbb E[a(X)b(X)]=7/4,
\]
so the one-index term is \(3/4\). These values yield the stated covariance for every \(n\ge2\). The same decomposition independently gives the two marginal variances and hence the exact correlation.

A separate order-spacing computation in the packaged checker represents the Gini statistic as a linear form and the sample variance as a quadratic form of independent exponential spacings and reproduces the covariance exactly.

## Originality

PASS, with an explicit bibliographic residual risk. The strongest same-object source inspected in full is Čiginas and Pumputis: it directly compares Gini mean difference with empirical variance, writes both as degree-two \(U\)-statistics, and develops their separate variance decompositions and asymptotic theory. The full text contains no occurrence of “covariance” and does not state the mixed finite-sample correlation.

Gail and Gastwirth develop exact and asymptotic theory for an exponential Gini statistic, but the public article summary inspected does not state a joint law with sample variance. Hosking places Gini mean difference within \(L\)-moment theory and contrasts it with conventional moments, but the inspected summary and bibliography do not provide this exact cross-covariance.

The nearest exact exponential variance identities involving sample extrema do not imply the Gini result: a maximum or range is a single extreme-order functional, whereas the Gini mean difference is a weighted sum of every internal spacing. The accepted formula requires a distinct mixed projection calculation.

## Value

PASS. Gini mean difference and sample variance are canonical competing measures of scale, especially when robustness to outliers or departure from normality matters. Under exponential sampling, both target the model's natural scale up to squaring, and the exact correlation quantifies finite-sample redundancy between an order-based and a moment-based summary.

The nontrivial limit
\[
3\sqrt6/8
\]
shows that increasing sample size does not make the two statistics asymptotically equivalent or asymptotically independent. The monotone finite-\(n\) formula provides a precise calibration of their persistent alignment.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK conditional_exact=5 ustat_cov_checks=199 ustat_var_checks=398 spacing_checks=39 monotonicity_checks=199 limit_rho=0.9185586535436917`.
