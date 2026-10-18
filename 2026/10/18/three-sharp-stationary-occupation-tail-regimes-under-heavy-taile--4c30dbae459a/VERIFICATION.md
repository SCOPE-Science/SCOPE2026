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

Run `python verify.py` with Python 3.9 or later and SciPy 1.9 or later. The checker differentiates the derived probability generating function numerically for three dynamical regimes; integrates the subcritical relative point mass; integrates the critical geometric survival using an exact change of variables; and tests the supercritical geometric survival against the proposed logarithmic equivalent. All three quadratures use the exact stationary renewal-age density, not simulation of renewal trajectories.

An execution on the supplied program completed with `PASS: 53 independent finite consistency checks (analytic proof required separately)`.

These are finite, floating-point diagnostic calculations, without certified interval errors or a proof of an infinite limit. The analytic argument is in `RESULT.md`, including its conditions and boundary cases. There is no independent external validation or audit.
