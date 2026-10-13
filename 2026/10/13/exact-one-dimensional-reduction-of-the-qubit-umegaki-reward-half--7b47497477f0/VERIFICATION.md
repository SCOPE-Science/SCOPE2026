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

The analytic proof establishes the reduction and uniqueness for every faithful noncommuting qubit arm and every admissible projector-reward threshold. It uses joint convexity of Umegaki relative entropy, the exact logarithm of a qubit density matrix, and strict operator convexity of \(-\log\).

The bundled `artifacts/verify.py` independently evaluates the scalar objective and derivative for the source's running instance, brackets the unique root, and checks the reported values of \(D_{\mathrm{inf}}\), \(K_{\mathrm{inf}}\), and the resulting coefficient reduction. Those finite calculations corroborate only the numerical specialization and do not replace the all-parameter proof.

The open collective-attainability question from the source is not resolved here.
