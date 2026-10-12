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

Execute `python3 checker.py` from the directory containing this document and the provided program. The code uses Python's standard library only. Its exact-rational enumeration treats each magnitude as a continuously uniform factor within a separated scale and enumerates all finite sign and within-bin magnitude-rank cells. It validates the full \(3\times3\) mixed-indicator matrix, \(\mathbb E[R_3]\), \(\mathbb E[A_3]\), and the \(109/96-t/8\) covariance for five scale counts; it also checks the one- and two-step universal covariances and a sharpness lower bound. Expected final diagnostic: `EXACT_VERIFICATION_OK 73 identity_groups`.

The proof in RESULT.md establishes the statements for **every** symmetric atomless iid increment law; the enumerations do not purport to cover every law. No computational approximation or external proof assistant is used in the proof. No independent audit has been undertaken.
