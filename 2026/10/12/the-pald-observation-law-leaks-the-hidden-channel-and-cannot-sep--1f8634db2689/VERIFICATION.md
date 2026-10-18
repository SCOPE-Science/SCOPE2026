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

PASS: With 0<K<n and orthonormal [G B], Gaussian convolution of X=G eta+B xi (xi|eta~N(0,I)), r|X~N(X,sc²I), Z|r~N(r,sb²I) gives Z|eta~N(G eta,(sb²+sc²)I+BB^T) with eigenvalues s and s+1. The paper Eq.(2.5) instead says a scalar covariance. Since B^T Z=xi+isotropic Gaussian noise, Cov(B^T Z,xi|eta)=I and mutual information=(n-K)/2 log(1+1/s). Conditional survival likelihood depends only on X, so integrating r yields p(Z,t,delta|X)=p(t,delta|X)phi(Z;X,sI); any positive variance pair summing to s induces the same joint observed likelihood after integrating X. Boundary K=0 or K=n excluded and different observation mechanisms excluded. Independent verification checks the Gaussian covariance eigenvalues [2,3,3] and singular two-scale information; proof is analytic.

## originality

PASS

PASS: The 2026 source already has Gaussian convolution p(Z|X)=N(X,Sigma_b+Sigma_c), a standard result; it does NOT assert that its two isotropic variance parameters are inseparable in the observed likelihood or prove the implicit-coordinate mutual information; instead it suggests orthogonality identifies representation loss. The source-specific simultaneous incompatibility of Eq. (2.5) with Eqs. (2.6)-(2.8) and continuous noise-allocation likelihood ridge is not covered by standard convolution alone. Resultary correlated-noise and identifiability hits use different models.

## value

PASS

PASS: Distinguishing whether hidden geometric channels are actually measured and whether two process/measurement variance components are likelihood-identifiable is central to the model’s stated scientific purpose. The exact Gaussian mutual information and continuous observational equivalence class identify an information-theoretic defect with direct impact on interpretation of posterior uncertainty and requirement of external measurements or nonproportional covariance templates. This is not just a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
