# Review

## Correctness

PASS. The probability integral transform reduces every fully specified continuous null to iid uniforms. The proof writes the two statistics as quadratic forms of the same centered empirical-process sum: Cramér–von Mises uses the identity operator and Watson uses orthogonal projection away from constants.

An exact iid quadratic-form covariance identity separates a Gaussian pairing term from the one-observation fourth-cumulant correction. The Brownian-bridge covariance kernel gives the three needed traces by elementary double integration. At the one-observation level, the Watson quadratic form is exactly \(1/12\), so its variance and its covariance with the unprojected one-observation norm vanish. Substitution yields all three finite-\(n\) second moments and therefore the correlation formula.

The checker independently integrates the order-statistic computing formulas with exact rational arithmetic for \(1\le n\le8\), rather than reusing the operator derivation.

## Originality

PASS, subject to a small historical-access risk. Pearson and Stephens's 1962 paper is the strongest directly relevant full source inspected. It studies both statistics jointly in the same article, gives finite moments for the Cramér–von Mises statistic, Monte Carlo distributions for Watson's statistic, and a relation between cumulants of their asymptotic marginal laws. Its six pages do not state a finite-sample covariance, joint moment, or correlation.

Hwang and Kuriki's full public manuscript treats the classical Cramér–von Mises and Watson statistics and their explicit limiting eigenstructures, but text searches found no covariance or correlation between the two. Targeted web and semantic searches for the exact finite formulas likewise found no matching statement.

Watson's 1961 source could not be obtained in full after bounded access attempts. Because the later Pearson--Stephens paper explicitly defines the same two statistics and cites Watson's construction, this is a residual historical risk rather than a decisive unresolved comparison.

## Value

PASS. Cramér–von Mises and Watson are classical, widely used quadratic goodness-of-fit statistics. Their separate null distributions are extensively tabulated, while their exact redundancy is a natural quantity whenever the tests are compared, combined, simulated jointly, or used as benchmarks.

The result is not a routine restatement of marginal moments: it identifies a simple finite-sample joint law,
\[
\operatorname{Corr}(W_n^2,U_n^2)
=
\sqrt{\frac{2(n-1)}{4n-3}},
\]
and explains structurally why Watson centering removes exactly one component while leaving a persistent asymptotic correlation \(1/\sqrt2\).

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK sample_sizes=8 exact_moment_checks=40 exact_correlation_squared_checks=7`.
