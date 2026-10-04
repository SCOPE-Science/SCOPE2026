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

The claim is verified by two exact algebraic routes.

First, direct multiplication gives
\[
H_\gamma(U)^2=\operatorname{diag}(UU^T-\gamma^2I_m,\ U^TU-\gamma^2I_m).
\]
Both \(UU^T\) and \(U^TU\) have eigenvalues \(\sigma_j^2\), so every squared eigenvalue of \(H_\gamma(U)\) is \(\sigma_j^2-\gamma^2\) with doubled block accounting.

Second, an SVD \(U=P\Sigma Q^T\) gives an explicit orthogonal similarity to the matrix with off-diagonal block \(\Sigma\). Interlacing the two halves of the basis produces independent dimers \(B_j\). This route proves not only the eigenvalues but also the Jordan structure. When \(\gamma>0\) and \(\sigma_j=\gamma\), \(B_j^2=0\), \(B_j\ne0\), and \(\operatorname{rank}B_j=1\); therefore \(B_j\sim J_2(0)\). Repeated threshold singular values give independent copies and cannot create a larger Jordan block.

No numerical experiment, floating-point tolerance, external certificate, or unproved asymptotic is used in the proof. The literature comparison remains the only non-algebraic uncertainty: an equivalent model-specific observation could exist under terminology missed by the searches.
