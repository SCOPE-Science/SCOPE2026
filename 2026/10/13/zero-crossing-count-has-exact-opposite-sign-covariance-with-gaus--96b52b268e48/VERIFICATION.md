---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For correlated standard Gaussian adjacent pair (Z0,Z1), p=P(Z0Z1<0)=acos(rho)/pi and direct conditional-normal integration by parts yields E[Z0^2 I]=p-rho sqrt(1-rho^2)/pi. After multiplying sigma^2, endpoint covariance follows. Gaussian AR1 Markov property gives E[X_j^2-sigma^2|X_i]=rho^(2(i-j))(X_i^2-sigma^2) for j<=i and time-reverse analog to right, yielding local kernel. For edge i, j-site kernel sums two finite geometric series; summing i gives claimed closed covariance and opposite sign. Independent scipy high-tolerance Gaussian integrals for rho=-.8,-.4,0,.4,.8 and finite n=2,5,11 edge sums agreed; analytic proof covers all n and |rho|<1.

## originality

PASS

Best-of-knowledge comparison to exact-object foundational sources, stronger possible general theorems, and Resultary mathematical records finds no decisive implication-equivalent published theorem; the four explicit scientific comparisons and source-reading limitations below retain uncertainty. Search uses 'energy covariance', 'quadratic amplitude', 'sign-crossing count', 'Gaussian AR(1)' aliases. Related crossing-crossing covariance is not equivalent to crossing-square covariance; no full-Sinn-paper absence claim because access was blocked.

## value

PASS

Crossing count and quadratic energy are canonical complementary sign-activity and amplitude summaries. The exact edge-to-site kernel and finite-n law reveal a dependence absent in the iid case and a sign asymmetry that crossing-count variance alone cannot reveal; a structural time-series covariance fact, not a gratuitous specialized decimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
