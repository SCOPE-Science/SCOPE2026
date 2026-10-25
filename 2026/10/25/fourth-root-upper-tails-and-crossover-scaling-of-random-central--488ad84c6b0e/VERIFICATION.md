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

# Reproducibility and verification

Extract `checker.py` from the same finding package and run `python3 checker.py` (Python standard library only).

The checker independently evaluates the area integral by integrating the disk-chord geometry over \(600\) orientations; compares six analytic maximizers against grids of \(3001\) directional values; tests the quartic flatness, the optimizer-shift coefficient, the maximal-area gain, the critical \(\varepsilon^{1/4}\) tail, and the two-branch crossover at five parameter values and two scales. The reference thresholds, error tolerances, and numerical methods are printed or present in the source.

All these checks executed successfully in the current package. They constitute finite, approximate corroboration rather than certification of the asymptotic limit. Universal correctness rests on the integral identity, Taylor expansion, monotone derivative factorization, strict-maximizer localization, and polynomial sublevel-set argument in `RESULT.md`. No independent audit has been performed.
