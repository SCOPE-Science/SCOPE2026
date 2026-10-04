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

The analytic proof is self-contained in `RESULT.md`. The bundled script `artifacts/verify_widest_quadrilateral.py` provides an independent finite consistency check using only the Python standard library.

Run:

`python3 artifacts/verify_widest_quadrilateral.py`

A successful replay prints `VERIFY_OK widest inscribed quadrilateral`. The script checks the exact side/diagonal width formulas against direct support-width calculations for \(30000\) randomly generated cyclic quadrilaterals, verifies that the sampled widths do not exceed \(4\sqrt3/9\), checks eleven points across the equality family, and checks the displayed deltoid coordinates.

Finite sampling is not used as proof of the universal inequality. The universal claim and equality characterization rest on the analytic reduction and one-variable maximization in `RESULT.md`.
