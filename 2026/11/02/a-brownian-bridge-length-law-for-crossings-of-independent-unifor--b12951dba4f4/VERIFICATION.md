---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For a chord with minor arc W/2, crossing probability is W-W^2/2; W is iid U[0,1]. The centered Hoeffding projection g(W)=W-W^2/2-1/3 has variance 1/45; the canonical degenerate residual kernel has variance 8/45 and disjoint/shared-index terms are uncorrelated, giving exact finite variances and covariance -n(n-1)t(1-t)(2-t)/6. Differentiating t(1-t)(2-t)^2 yields unique interior maximizer (7-sqrt17)/8. Empirical Donsker for the W_i and exact integration-by-parts identity produce the joint bridge limit; scaled residual variance O(n^-1) vanishes. Independently verified symbolic g integrals/threshold polynomial, and the known exact chord-count variance matches Flajolet–Noy Theorem 3. The result is not a full nonlinear conditional expectation.

## originality

PASS

Uniform sorted endpoint matchings give the same marginal crossing law, but their abstract matching records lack actual angular spacings W_i. The new joint law with the length empirical process is not the known marginal CLT under a different name. Hoeffding U-statistic projection and Donsker theory imply a general mechanism, but applying it requires the explicit chord kernel and its first projection. Flajolet–Noy and Paguyo prove the marginal mean/variance/normality rather than this length-indexed joint process. Classical Touchard–Riordan tables encode crossing count distributions, not continuous geometric minor-arc-length empirical covariances; Resultary chord-related results treat unrelated central/random chord observables. The new theorem implies the marginal Gaussian limit and reproduces the exact variance already in Flajolet–Noy; the converse implications do not recover the joint Brownian-bridge representation or sharp length threshold.

## value

PASS

Natural geometric extension of random chord-diagram crossing theory: geometric lengths supply observable predictors not present in unlabeled matchings. Exact finite variance-explained fraction, optimal short-arc threshold and joint functional representation are precise, reusable stochastic-geometric invariants beyond the known marginal crossing CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
