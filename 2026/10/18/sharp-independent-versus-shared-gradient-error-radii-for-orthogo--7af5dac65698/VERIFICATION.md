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

# Verification and reproducibility

Run `python verify.py` from this directory with Python 3.8 or newer; there are no third-party dependencies. The executed script returned `PASS 12983 exact-rational assertions/cases`.

The script checks the closed-segment Euclidean projection using exact rational arithmetic, exhausts rational perturbation grids strictly inside the independent and shared robustness radii, checks threshold equality witnesses for unequal and equal norms, and checks explicit strict-ascent cases beyond the independent radius. The shared-radius threshold is also verified by exact translation of the noiseless projected point to zero.

This test is not an infinite certificate: it covers a finite rational grid. The proof of the two universal safety implications, all real parameter values, and the sharpness constructions appears in RESULT.md. No third-party authorship, external validation, or numerical floating-point certification is asserted.
