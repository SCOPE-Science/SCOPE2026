---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Under exact SPD Lanczos and beta_m*beta_(m+1)>0, the exact conditioned covariance R_m=A^-1-Q_m T_m^-1 Q_m^T has m-dimensional nullspace A range(Q_m) and rank d-m. Let B be the positive Schur-complement inverse, p_j=e1^T B^j e1, v=Q_perp Be1 and a=beta_m Q_m T_m^-1 e_m. On the orthogonal plane span(a,v), the analytic trace-matched approximation has 2x2 determinant ||a||²(p1 p3-p2²)/p2. Strict Cauchy–Schwarz holds since the next Lanczos coefficient makes e1 a non-eigenvector of S, hence of B; the remaining r-1 complement directions have positive isotropic coefficient omega. Rank is 2+(r-1)=d-m+1, with exact support rank d-m, so same-mean Gaussians are mutually singular and both KL directions infinite. Auditor-written exact rational reconstructions for epsilon in {1/40,1/7,1/2,1,6/5} recover the 3x3 certificate determinant epsilon²/[2(3-epsilon²)(4+epsilon²)²], observed-direction spurious variance 4epsilon²/(4+epsilon²)², exact covariance null vector, and rank mismatch. At epsilon->0 the covariance entries converge to the same matrix while support ranks differ, an analytic continuity argument rather than inference from tests. Limits: exact trace, not Monte Carlo; nontermination and complement size >=2; residual covariance not full inverse reconstruction.

## originality

PASS

Fifen–Karambal–Hennig 2026 precisely define the target and rank-one-boundary-plus-isotropic covariance construction. Section 4.3 Proposition 14 bounds the matrix approximation error, while Section 4.4 Proposition 16 explicitly proves rank d-m of the EXACT conditional covariance, not of the approximating covariance. The source distinguishes full inverse covariance from residual computational-uncertainty covariance. Classical Bayesian CG conditional nullspaces do not give positivity of this specific approximant boundary plane. The audited strict next-beta moment condition and generic rank-plus-one phenomenon are not stated in the compared primary theorems, though generic support mismatch is a known possibility and broad Gaussian-conditioning literature remains a risk.

## value

PASS

The additional positive eigenvalue and observed-direction variance are an exact calibration pathology of an explicitly proposed matrix-free uncertainty construction; the Gaussian measures become mutually singular even as operator-norm covariance error vanishes. This is a generic model-wide structural limitation, not a numerical tolerance artifact or arbitrarily chosen small matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
