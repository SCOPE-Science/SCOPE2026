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

# Exact certificate checks

Run `python verify_hardy.py` with both JSON files in the same folder. The code uses only standard-library integers and `fractions.Fraction`, regenerates all signed-permutation partitions and all 18 nearest-neighbor incidences, checks 191 positive residuals at radius 11, and evaluates the exact rational energy defect for the 264-orbit radius-12 witness.

Actual check: `R11_orbits 191 smallest_exact_positive_residual 1458`; `R12_orbits 264 four_times_energy_minus_49_times_Hardy -168023799157855578188041899511220364510317/66816567612546192522086437300`; `EXACT_CERTIFICATES_PASS`. This exhausts all orbit residual checks for the provided finite supports. It is not an infinite search, a full spectrum computation, or independent scientific validation.
