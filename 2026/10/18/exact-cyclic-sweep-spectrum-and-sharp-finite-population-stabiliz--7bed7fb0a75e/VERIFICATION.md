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

# Reproducibility and verification

Execute `python verify.py` with Python 3 and SymPy installed. The checker builds all coordinate-update Jacobians as exact matrices, multiplies them in sweep order, and compares exact characteristic polynomials and determinants. It tests dimensions \(1\) through \(8\), several rational values of \(\alpha\), and the complete matrix identities \(M^{N+1}=I\) and \(\sum_{j=0}^{N}M^j=0\) at criticality. Observed output ended in `VERIFY_OK`.

The exhaustive finite checker is not a proof for unbounded \(N\); the general theorem is established by the direct determinant calculation, the strict root inequality, and the determinant argument in `RESULT.md`. The characteristic polynomial is independent of the chosen fixed site order only because the complete mean is invariant under site relabeling. No numerical conclusion is asserted about nonlinear stability at \(\alpha=N\), arbitrary couplings, or randomized site selection.
