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

# Reproducibility

Run `python check.py` with Python 3 and SymPy installed. The script checks algebraically the exact identity for the Möbius logarithmic derivative, the sum-of-squares discriminant, and the tangency coordinates; it prints representative boundary measurements on both sides of the threshold.

The scientific proof is analytic, not computational: the Schur-function moment inequality is proved by integration by parts and Schwarz--Pick, the variability region by exact Taylor integral identities, and sharpness by an explicit quadratic family. Finite numerical samples establish neither universal containment nor originality. The full proof and its hypotheses appear in RESULT.md. No independent audit has been performed.
