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

Run `python3 verify.py` using the standard Python library. The checker recomputes the matrix powers, the four affine derivatives, and the quadratic coefficients, then tests the higher-coefficient divisibility bound for a generous finite range. It also enumerates complete pairs of consecutive recurrence values modulo powers of two, stopping only when the *state pair* repeats, and compares the resulting visited-value set with the claimed union of residue classes.

The script was executed successfully before packaging. The infinite claim is certified by the explicit proof in RESULT.md: the finite tests are independent consistency checks and do not supply the limiting argument. External independent assessment is not performed.
