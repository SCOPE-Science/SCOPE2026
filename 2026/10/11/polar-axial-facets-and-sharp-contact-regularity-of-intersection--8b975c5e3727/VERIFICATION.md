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

# Reproduction and verification

Run `python verify.py` with Python 3 and `mpmath` installed. The source file is embedded alongside this document and uses only its declared `mpmath` dependency and the standard Python runtime.

Observed output from the accompanying verifier:

`VERIFY_OK cases=266 max_slicing_relative_error=3.816723e-65 max_cap_coefficient_relative_error=0.00015736394`

It compares section-volume integrals, the cap deficit, the predicted leading coefficient, a distinct planar polar integral for three-dimensional sections, and the anisotropic coefficient for two ellipses and two directions each. The maximum cap-coefficient discrepancy comes from a deliberate positive-size approach to the limiting rim, not from a claimed exact identity at positive distance.

The proof uses an exact strip formula, the curvature-dependent cap asymptotic (locally proved by smooth Morse coordinates), its transfer to the facet rim, and the fact that a nonzero one-sided fractional/integer power has exactly the stated regularity. A finite test does not certify that proof for every convex base and dimension. No independent audit or external proof certification has been performed.
