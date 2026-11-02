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

Run `python3 verify.py` with Python 3 standard library. The script regenerates every SSPRK3 modal polynomial with exact rational coefficients, checks cell-average mass conservation, verifies all low-mesh Bernstein enclosures and all stage wave-speed trace bounds, and tests the three explicit overshoot formulas on the appropriate grids. A successful run prints `CERTIFICATE_OK`. The infinite-family step follows mathematically from the radius-three stencil argument, not from finite computation. Independent validation has not been performed.
