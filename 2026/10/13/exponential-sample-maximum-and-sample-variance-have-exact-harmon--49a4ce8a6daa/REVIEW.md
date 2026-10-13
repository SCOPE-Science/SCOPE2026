# Review

## Correctness

PASS. The proof starts from the standard independent normalized spacings of exponential order statistics. It expresses the maximum as a linear form and the unbiased sample variance as a centered quadratic form in the same independent \(\operatorname{Exp}(1)\) variables.

The quadratic-form matrix is computed explicitly. Its row sums and diagonal entries reduce the mixed linear/quadratic covariance to harmonic sums, and the identity
\[
\sum_{r=1}^n\frac{H_r}{r}
=
\frac{H_n^2+H_n^{(2)}}2
\]
gives the stated closed form. The marginal variance of the maximum follows from independent spacings; the sample-variance marginal follows independently from the fourth-central-moment formula.

The packaged verifier recomputes the mixed raw moments directly from exact factorial moments of independent exponential spacings for small \(n\), rather than invoking the covariance shortcut used in the proof.

## Originality

PASS, with residual bibliographic risk. Vellaisamy--Zeleke is the strongest full primary source inspected because it supplies exactly the exponential spacing representation and harmonic maximum moments used in the proof. Its stated scope is exponential order statistics, spacings, and combinatorial identities, and the inspected manuscript does not state the maximum/sample-variance cross-covariance.

Targeted literature searches covered maximum, largest order statistic, sample variance, covariance, correlation, exponential samples, and harmonic-number formulations. Related range literature treats stochastic orders of exponential sample ranges rather than covariance with quadratic sample variance.

The closest own-ledger variance result concerns a normal-sample size bias and has neither exponential order spacings nor a sample maximum. A separate own result concerns midpoint/range structure for two observations and likewise does not determine the present mixed moment.

## Value

PASS. The sample maximum and sample variance are canonical but qualitatively different dispersion summaries: one is controlled by a single extreme observation, while the other aggregates quadratic deviations over the entire sample.

The exact covariance gives a finite-sample calibration of their dependence under the most basic skewed lifetime model. More structurally, the positive covariance shrinks slowly enough to carry a \((\log n)^2\) factor, yet the standardized correlation still vanishes at the explicit rate \((\log n)^2/\sqrt n\). This cleanly quantifies the separation of extreme and bulk quadratic dispersion.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK mean_checks=7 direct_covariance_checks=7 direct_variance_checks=7 row_sum_checks=35 asymptotic_checks=3 target=0.275664447711 last_ratio=0.307423361123`.
