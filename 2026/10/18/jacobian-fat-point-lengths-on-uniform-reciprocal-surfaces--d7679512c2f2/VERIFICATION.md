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

# Verification and limitations
The included `verify.py` was run using SymPy in exact arithmetic. It checked the standard rational-normal-curve Hankel Jacobian, its \((r-1)\)-minors, and that their images span all \(r(r-1)+1\) basis elements in degree \(r-1\) for \(r=2,3,4\). It checked that the selected triangular Jacobian determinant is the expected power of \(x_0\), that the reciprocal-binary-product sections give invertible change-of-basis matrices, and that the length formula agrees with the exact sum for \(2\le r<32\). Output ended `VERIFY_OK`.

The proof for all \(n\) depends on the exact algebraic chart change, the standard determinantal presentation, irreducibility of characteristic-zero symmetric powers, and the published generic reciprocal-plane singular-support theorem. Neither the finite tests nor a search with no exact matches proves that the claim is globally novel. No external or independent validation has been performed.
