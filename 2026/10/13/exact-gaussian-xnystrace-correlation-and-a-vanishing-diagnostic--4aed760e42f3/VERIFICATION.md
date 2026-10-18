---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For unnormalized Nystrom leave-one-out on A=I_n and 2<=m<=n, each B_j=m-1+Y_j, with Y_j~chi-square_nu and nu=n-m+1. Conditioning on other m-2 columns leaves two independent d=nu+1 Gaussian residual vectors whose independent radii share one sin^2 angle with Beta((d-1)/2,1/2) law. Its first and second beta moments yield Cov(B_i,B_j)=2nu/(nu+3) and correlation 1/(nu+3), not independent basic estimates. Exchangeability then gives Var(T_m)=2nu(n+3)/(m(nu+3)), E J_m=2nu(nu+2)/(m(nu+3)) and ratio (n+3)/(nu+2). At m=n, true absolute-error variance approaches 1/2 while J_m tends to zero in probability. Bounding fourth moment by 848 and Cauchy–Schwarz yields liminf event probability >=1/13568; m>=n+1 gives exact identity projector via pseudoinverse. Independent exact rational beta/variance checks passed; finite checks do not prove the limit.

## originality

PASS

Published XTrace/XNysTrace describes the leave-one-out estimator and general covariance-diagnostic identity, but the candidate computes exact identity-Gaussian pairwise correlation and a sharp absolute-error diagnostic failure at full sketch rank, plus one-extra-probe exactness. Best-of-knowledge original specialization; narrow domain explicitly respected.

## value

PASS

The exact covariance and squared-error diagnostic mismatch provide a meaningful estimator-calibration boundary: the reported mean-square error proxy can vanish while the true absolute estimator error does not concentrate, even on the identity matrix. An additional sketch restores exactness, pinpointing a natural dimension/rank transition for an established method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
