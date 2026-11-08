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

# Verification record

Run `python verify.py` with Python 3, `sympy` and `mpmath`. The script checks two exact derivatives and boundary values, two symbolic asymptotic series, six numerical independent quadratures, and four scaled high-aspect comparisons. Successful output terminates in `VERIFY_OK primitive_derivatives=2 endpoint_values=2 symbolic_series=2 quadratures=6 asymptotic_checks=4`.

The analytic proof in `RESULT.md`, not the finite test run, establishes the exhaustive edge allocation and the all-real-aspect probability interval. The source-level checks do not constitute external or independent mathematical validation. The novelty comparison is limited by older full-text access and is not a certification of priority.
