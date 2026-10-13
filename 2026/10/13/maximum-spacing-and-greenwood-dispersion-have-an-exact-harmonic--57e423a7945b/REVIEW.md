# Review

## Correctness

PASS. On the event that any fixed \(k\) selected spacings exceed \(t\), translating those coordinates leaves a simplex of mass \(1-kt\); because the Dirichlet parameter is \(1\), the density is constant and the event probability is exactly \((1-kt)^{m-1}\). Conditional quadratic moments are then standard Dirichlet moments.

Inclusion-exclusion gives the exact truncated mixed expectation, and integrating it reduces to two beta integrals. The resulting binomial sums are the standard first- and second-order harmonic identities. The covariance, variance, and correlation formulas follow by exact algebra.

The checker independently expands and integrates every finite polynomial term with rational arithmetic through \(m=80\), rather than inserting the closed integral formula as an assumption.

## Originality

PASS, with a concrete residual risk from classical spacing literature. The closest full public source, Royen, gives exact distributional representations for Greenwood's statistic and its general Dirichlet analogue. The inspected manuscript does not introduce the maximum spacing in the Greenwood analysis or state a mixed covariance.

The closest maximal-spacing source inspected in full, Aaron--Cholaquidis--Fraiman, reviews maximal-spacing theory and statistical applications but contains no Greenwood statistic.

Pyke's 1965 review is broader and is therefore a genuine risk. Its accessible publisher summary covers distribution theory and limiting laws for functions of spacings, but the full PDF was not available through open sources or the authorized institutional retrieval path during this review. No claim of whole-document noncoverage is made for that paper.

## Value

PASS. Maximum spacing and Greenwood dispersion are canonical but qualitatively different spacing diagnostics: one isolates the single largest gap, while the other aggregates quadratic concentration over all gaps. They are commonly treated as separate uniformity statistics.

The exact finite covariance and correlation quantify how much information these diagnostics share under the null. The result is not merely a sign computation: it gives a closed harmonic mixed moment and shows that a strong finite dependence becomes asymptotically negligible at the explicit rate \((\log m)^2/\sqrt m\).

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK term_integrals=3239 mixed_moments=79 harmonic_identities=158 marginal_checks=316 covariance_checks=79 positivity_checks=79 correlation_checks=79 asymptotic_checks=3`.
