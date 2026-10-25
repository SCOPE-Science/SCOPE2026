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

# Reproduction and limits

Run `python verify_groebner.py` with SymPy 1.10+ and `python verify_finite_fields.py` with Python 3; both scripts return exit status zero only if every asserted check passes. Their deterministic reference outputs are `groebner_output.txt` and `finite_field_output.txt`.

The Gröbner script performs 39 unit-ideal checks of dehomogenized cubic Jacobian systems over characteristic three and 3 unit-ideal checks of the base locus. The finite-field script independently tests all normalized rational members at every point of the projective planes over finite extensions of degrees 1, 2, 3; for a singular cubic one of those extensions must contain a singular point, by the component/normalization argument described in RESULT.md. Code and reference outputs are sufficient to reproduce the exact computations. This is not a check of every coefficient over every extension field; only thirteen rational coefficient members are claimed smooth.

Neither the source code nor this note constitutes an independent audit.
