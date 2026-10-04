---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof has two independent algebraic checkpoints. First, exact multivariate polynomial expansion verifies
\[
\det(z_j^{m_i})_{m_i\in\{0,1,2,4\}}
=
\prod_{i<j}(z_j-z_i)(z_1+z_2+z_3+z_4).
\]
Second, the checker constructs \(\Phi_N\) by exact integer polynomial division and tests whether a four-term root-of-unity sum vanishes by exact reduction modulo \(\Phi_N\). Exhausting all four-column subsets for \(5\le N\le40\) gives

`VERIFY_OK N_max=40 subsets=749397 singular=1329 determinant_identity=exact`

The computation uses no floating-point decisions. It confirms the theorem on a finite range but is not the proof for arbitrary \(N\); the infinite statement follows from the determinant factorization and the even-polynomial antipodal argument in RESULT.md.
