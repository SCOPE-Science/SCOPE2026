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

The self-contained `verify.py` uses Python 3 and NumPy. Execute `python verify.py` from the directory containing this document and the result. The program checks exact rational budget constraints, every principal minor of the candidate PSD slack and its zero determinant, the polygon dual witness in the imbalanced regime, and the floating-point generalized eigenvalue. The recorded output from the embedded source is:

`VERIFY_OK 321 exact budget/PSD/duality cases, 114 imbalanced, numerical generalized eigenvalue checks`

The exact arithmetic cases use rational stationary masses and rational square roots of positive edge prices; numerical eigenvalues are verified within an explicit finite tolerance. The full proof for every admissible real instance is in `RESULT.md`; neither sampling nor numerical eigenvalues certify that universal claim. No external independent audit has been performed.
