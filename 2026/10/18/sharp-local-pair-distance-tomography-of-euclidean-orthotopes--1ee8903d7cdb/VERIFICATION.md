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

# Reproducibility and limits

The ordinary Python 3 standard-library script `verify.py`, embedded alongside this manuscript, was executed and printed `VERIFY_OK`. It evaluates the small-distance law against numerical ball-volume integration of the independent coordinate displacement density in dimensions three, four, and five; checks the prescribed top symmetric coefficient and inversion formulas; and independently simulates point pairs in a three-dimensional box. The finite checks establish agreement within the documented floating-point tolerances for those cases, not an exhaustive proof. The all-dimensional statements, precise Hölder exponent, and minimal observation count follow from the analytic arguments in `RESULT.md`.

No external audit, independent certificate, or automated theorem proving is represented by these checks. The results are subject to the scientific scope and bibliography limitations stated in the manuscript.
