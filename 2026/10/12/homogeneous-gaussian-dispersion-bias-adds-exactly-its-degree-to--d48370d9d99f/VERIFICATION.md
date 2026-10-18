---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For σ²>0, n≥2 and admissible T=h(Y), centered Gaussian Y lives on a d=n−1-dimensional isotropic subspace, so Y=σ R U with independent R~χ_d and uniform direction U. Positive q-homogeneity gives h(Y)=σ^q R^q h(U); under size bias the joint law still factorizes. The χ_d radial density r^{d−1}e^(−r²/2) is multiplied by r^q and becomes exactly χ_{d+q}, including noninteger q. Hence dS²/σ²=R² is χ²_{d+q} under the biased law; the Laplace and gamma-moment formulas follow. Its first moment gives Cov(T,S²)=q σ² ET/d. Sample range and Gini difference depend only on Y and are nonnegative degree one. The proof works without smoothness, even for d=1 and q=0. Finite source code checks integer and fractional gamma moments but does not supply the universal factorization.

## originality

PASS

The general homogeneous-statistic size-biased *radial* chi-square law and universal covariance consequence are not statements of the inspected normal-characterization literature. This is a distinct joint-law result from sample-mean independence, although the Gaussian polar decomposition and gamma power tilt are classical.

## value

PASS

Provides an exact universal sampling law under a natural weighting operation, not only one new correlation: every χ² mixed moment under bias follows simultaneously for nonsmooth, nonparametric angular statistics. The covariance identity for sample range and Gini difference is an immediately useful, precisely motivated consequence; it is not presented as a new gamma-tilt method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
