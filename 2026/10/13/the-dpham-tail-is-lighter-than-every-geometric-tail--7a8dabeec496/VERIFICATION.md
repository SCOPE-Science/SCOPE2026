---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Telescoping the published PMF gives the inclusive survival. With L=log(mu)>0, the derivative of exp(L x^alpha) has logarithm L x^alpha+(alpha−1)log(x)+log(alpha L), which tends to infinity even when alpha<1. The mean-value theorem therefore gives a divergent adjacent increment and a vanishing tail ratio. Since exp(L n^alpha)/n tends to infinity, the survival is o(exp(−cn)) for every c>0, and the PMF is bounded above by a survival with any desired eventual geometric decay. This proves finiteness of every positive exponential moment and hazard limit one. The stated ceiling is exact for the left generalized inverse, including exact jumps, since F(n)>=1−q iff n+1 reaches the continuous inverse threshold. For maxima, take rounded thresholds n±=(1±epsilon)a_m+O(1); then mu^(n±^alpha)=(log m)^((1±epsilon)^alpha+o(1)). The upper union bound and lower bound via P(M_m<n−)≤exp(−m S(n−)) yield the asserted convergence. No finite check is relied upon for these limits.

## originality

PASS

The distinct result is the explicit all-parameter asymptotic correction for the DPham law, particularly the opposite-to-long-tailed adjacent ratio, the all-positive-exponential-moment classification, and the leading iid maximum law. The PMF, unrounded quantile inversion, and finite-sample order-statistic formulas are not original here.

## value

PASS

The short proof settles a substantive modeling distinction raised by the article's wording: arbitrarily slow-looking pre-asymptotic behavior of the fitted family cannot yield conventional heavy or long tails for any admissible fixed parameters. The maximum scale and hazard limit give concrete consequences, rather than only a terminology objection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
