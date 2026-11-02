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
# Reproducibility and checks

Execute `python3 verify.py` in an environment with Python 3 and SymPy. No other input is needed. The checker constructs exact rational-coordinate idempotents at the special ratio for nine dimensions, verifies the defining quadratic equations with rational arithmetic, and checks the closed count. It independently enumerates and tests candidates at 42 numerical parameter instances spanning generic, discriminant-collision and special ratios for dimensions 3 through 8; near-zero floating-point discriminants are snapped to zero solely in these finite tests. Finally, two SymPy Gröbner bases for dimension three verify the elimination factors at generic and exceptional ratios.

Expected output begins:
```
VERIFY_OK exact_r_equals_n_cases= 9 numeric_parameter_cases= 42 groebner_cases=2
```

The numerical fingerprints do not prove mathematical equality of arbitrary algebraic numbers. The all-dimensional theorem and all its complex-field quantifiers are established by the symbolic proof in `RESULT.md`, not by sample enumeration. Finite computations serve as independent consistency checks. No independent external audit has been performed.
