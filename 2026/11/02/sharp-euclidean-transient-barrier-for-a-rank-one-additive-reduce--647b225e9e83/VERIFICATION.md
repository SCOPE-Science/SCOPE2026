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

The exact calculation is in `RESULT.md`; run `python verify_typeii.py` with Python 3, SymPy and NumPy installed. The verifier separately reconstructs the matrix and determinant identities, the discriminant and principal-angle equality, 25,904 non-boundary matrix-norm comparisons on rational coefficient cases, 48 exact sharpness families, and the rational \(\kappa=16\) witness.

Finite tests do not certify the continuous parameter ranges. The proof relies on a two-by-two positive-definiteness criterion, the exact concave determinant polynomial, an AM–GM upper bound, and a witness achieving its lower bound for every positive correction coefficient. No floating-point error bounds or independent review are claimed.
