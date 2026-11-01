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

# Verification of the exact ball-slab asymmetry profile

The mathematical proof consists of independent necessary and sufficient inequalities: a unique zero of the increasing quadratic, exact reflected-ball containment at that zero, a lower-rim obstruction for all smaller dilations, rigidity of the minimizing center, and a strict completed-square optimization over the second cutting level. These are analytic proofs for every dimension at least two and every admissible clipping pair, not finite enumerations.

The standalone `check.py` uses Python, NumPy, SciPy and SymPy. Running it in the same directory as these files produced:

```
EXACT_QUADRATIC_AND_COMPLETED_SQUARE_IDENTITIES_PASSED
INDEPENDENT_POLYGONAL_MINKOWSKI_LP_CHECKS_PASSED 14
RIM_CONTACT_AND_STRICT_LOWER_SCALE_CERTIFICATES_PASSED 5
SHARP_FIXED_UPPER_CUT_ENVELOPE_AND_UNIQUE_OPTIMIZER_PASSED 6
GOLDEN_RATIO_CEILING_AND_ENDPOINT_PASSED
ALL_CHECKS_PASSED
```

Its symbolic factorization tests are exact. Its planar polygonal linear programs approximate the curved body and are not proofs in infinitely many parameter values or higher dimensions. They are corroboration only. Source comparison and historical priority are provisional; no independent audit or certification is claimed.
