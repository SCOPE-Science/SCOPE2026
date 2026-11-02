---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS — Recomputed ordered-spacings Dirichlet reparameterization, mixed E[|X1-X2|Q] using U=X1/(X1+X2) uniform and beta splitting, yielding (2m+5)/(m(m+1)(m+2)); verifies covariance (m−1)/(2m(m+1)(m+2)). Rank-gradient representation gives Var G=(m−1)/(12m²); standard Dirichlet moments give Var Q=4(m−1)/((m+1)²(m+2)(m+3)). Direct expansion T=Q−G/m−constant yields the exact rational Var T, mean and correlation. For the CLT, checked exponential-normalization influence functions a(E)=(E−3)/2+2e^(−E), b(E)=E²−4E+2 with covariance matrix [[1/12,1/2],[1/2,4]], so Var(b−a)=37/12. The m=2 boundary is valid. Independently recomputed exact rational ordered-simplex moments m=2..9; analytic proofs, not finite extrapolation, give all m and limit.

## originality

PASS

PASS, qualified — Jammalamadaka–Goria 2004 already defines the ranked-spacing statistic and its Gini–Greenwood decomposition; those elements are prior, as the primary PDF p.183 shows. Tung–Jammalamadaka 2012 gives broad asymptotic U-statistic CLT machinery, so that method is prior too. Neither inspected theorem evaluates the exact finite-m G/Q covariance and nontrivial positive correlation or Var(T); the paper explicitly highlights dependence as a problem. Limit variance 37/12 is a specialization of known CLT framework. Unindexed finite-sample calculation remains possible.

## value

PASS

PASS — Finite-sample calibration for an already published goodness-of-fit test is a motivated exact statistical invariant: Gini and Greenwood remain strongly dependent (Corr→√3/2), and the mixed covariance corrects the test variance and its asymptotic constant from the independence-based incorrect 49/12 to 37/12. Exact m dependence and valid all-sample null mean/variance are useful even without a full density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
