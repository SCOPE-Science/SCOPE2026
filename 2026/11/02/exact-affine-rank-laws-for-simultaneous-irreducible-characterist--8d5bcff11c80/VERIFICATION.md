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

Run `python verify_artin_schreier.py` using standard Python 3 with no external packages. The verifier constructs the fields of orders \(3\), \(9\), and \(27\) using irreducible polynomials, verifies the field-unit property directly, and computes cubic roots for all \((b,c)\). It compares that independent count to both the affine-rank inclusion-exclusion formula and the linear-functional projection formula, and checks the three-offset and extremal classifications.

Actual successful output:

```
FIELD_OK q=3 checked_offset_sets=7
FIELD_OK q=9 checked_offset_sets=511
FIELD_OK q=27 checked_offset_sets=14
VERIFY_OK checked_offset_sets=532 triple_classifications=89 independent_direct_polynomial_root_tests=True
```

For the first two field sizes all nonempty distinct-offset subsets are tested; for order \(27\), fourteen representative and extremal cases are tested. The scripts establish no general claim from finite enumerations: the mathematical proof is the additive-kernel/trace identity followed by exact finite-vector-space counting. No external or independent audit has been conducted.
