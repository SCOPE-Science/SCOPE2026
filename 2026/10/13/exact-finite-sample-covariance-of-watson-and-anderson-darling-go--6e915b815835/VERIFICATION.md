---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For all n>=1 under a fully specified continuous simple null, the Watson kernel h(x,y)=1/12-|x-y|/2+|x-y|^2/2 is canonical and has constant diagonal 1/12; the Anderson-Darling kernel a(x,y)=integral Y_xY_y/[t(1-t)]dt is canonical. Thus only matching unordered off-diagonal pairs contribute to covariance, giving 2(n-1)/n E[ha]. Independent symbolic Brownian-bridge integration reduced its inner product to integral_0^1 s(1-s)/12 ds=1/72, yielding Cov=(n-1)/(36n). The variances Var(U)= (n-1)/(360n) and Var(A)=[4-pi^2/3+2(n-1)(pi^2/3-3)]/n then give stated monotone correlation and n=1 undefined correlation. Hypotheses exclude parameter estimation.

## originality

PASS

The classical Watson and Anderson–Darling marginals and spectral decompositions are known; the submission gives the exact cross-statistic finite-n covariance and correlation. The inspected primary Stephens 1974 full work decomposes the separate statistics rather than evaluating this cross finite-sample kernel inner product. A possible older joint-component calculation remains a genuine risk.

## value

PASS

The exact cross covariance quantifies dependence between two canonical omnibus goodness-of-fit statistics for every sample size, directly relevant to interpreting joint/combined testing even though it does not itself calibrate joint tails. This is a motivated cross-statistic invariant not supplied by separate marginal moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
