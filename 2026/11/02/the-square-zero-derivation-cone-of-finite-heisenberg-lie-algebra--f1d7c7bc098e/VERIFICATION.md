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

# Reproducibility record

The standalone `verify.py` directly enumerates matrices over the specified finite fields and checks the original Heisenberg Lie Leibniz equations and composition square, with no external package dependencies. It separately enumerates the requisite nonsingular symmetric matrix factors. Run `python3 verify.py` from the folder containing this document and the checker.

The executed result was:

```text
Heisenberg dimension 3 over GF(2): direct [1, 9] = formula [1, 9]
Heisenberg dimension 3 over GF(3): direct [1, 32] = formula [1, 32]
Heisenberg dimension 3 over GF(4): direct [1, 75] = formula [1, 75]
Heisenberg dimension 5 over GF(2): direct [1, 45, 330] = formula [1, 45, 330]; quotient-derivation possibilities 2048
HEISENBERG_SQZERO_DERIVATION_RANK_OK: 4 direct derivation spectra and 9 symmetric-matrix comparisons
```

Exhaustive finite enumeration checks the particular cases, not the general theorems over all fields. The arbitrary-characteristic geometry and formulas are supported by the symbolic mathematical proof in `RESULT.md`. This package supplies no independent audit or certification.
