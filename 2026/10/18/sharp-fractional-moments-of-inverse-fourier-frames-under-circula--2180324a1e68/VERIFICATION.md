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
The analytic argument supplies universal quantifiers and the precise endpoint. Companion `verify.py` uses only Python's standard library and completed 70 exact or supplementary checks: finite-order cofactor orthogonality, exact two-node even-parameter moment ratios, and direct numerical comparison of two independent formulas for the inverse-Gram trace.

To reproduce, run `python3 verify.py`; the expected final line begins `VERIFY_OK 70 exact/supplementary Fourier checks`.

The program does **not** certify the full infinite family of repulsion exponents or matrix sizes. Those are proved by the integrability estimate and the pair-collision lower bound in `RESULT.md`. There has been no independent scientific audit.
