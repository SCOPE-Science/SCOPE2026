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
The conditional exact order-statistic mean \(1/(m+1)\), all occupancy cases, two-variable polynomial integrals, threefold finite-difference identity, and majorization strictness were reconstructed algebraically. The thin-triangle limit uses the integrable domination \(\exp(-(s+t)/3)\) after the change of variables described in `RESULT.md`.

Run `python checks/triangle_boundary_hull_checker.py` in an environment with NumPy installed. Recorded output:

```
EXACT_MULTINOMIAL_VERSUS_INCLUSION_EXCLUSION_IDENTITIES_PASSED 6
SHARP_EQUALITY_FORMULAS_AND_ENDPOINT_CONSISTENCY_PASSED
INDEPENDENT_EUCLIDEAN_HULL_SIMULATIONS_PASSED 4
INDEPENDENT_CUBICAL_MOMENT_QUADRATURE_PASSED
ALL_CHECKS_PASSED
```

Finite exact-rational enumerations and numerical samples corroborate specified cases only; they are not an exhaustive proof. No independent audit or proof certification is claimed. The theorem does not apply to arbitrary convex polygonal bases or nonuniform boundary laws.
