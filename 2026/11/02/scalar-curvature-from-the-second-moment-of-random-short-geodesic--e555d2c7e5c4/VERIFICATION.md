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

# Reproducible checks and proved scope

The complete proof and its dimensional hypotheses are in `RESULT.md`. Execute `python check_curvature.py` (requires NumPy). The program checks exact rational algebra in dimensions 2–20, and independently integrates the exact spherical and hyperbolic cosine laws under the correct volume-uniform radial densities in dimensions 2 and 3. The resulting fourth-order coefficients tend to the theoretical coefficients with decreasing radii, and the executable exits with `ALL_CHECKS_PASSED` on success. These tests corroborate constants/signs and are not an exhaustive check for all dimensions or metrics. The analytical proof supplies the general result. No independent audit or finite-sample consistency test was performed.
