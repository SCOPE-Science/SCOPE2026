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

# Verification

The mathematical proof of the all-parameter capacity identity uses a heavy-symbol injection, constant-word replacement, and a matching design construction. It is independent of computational enumeration.

The included `verify.py` checks 16 finite parameter pairs using two independently formulated integer linear programs, one over all size-\(n\) multiplicity vectors with conflict edges whenever their overlap is at least two, the other over \(n\)-element subsets with pair-capacity constraints. The programs were solved to verified zero mixed-integer optimization gap and returned the identical optimum in each case; see `verify_output.txt`.

Run with Python 3, NumPy and SciPy:

```text
python verify.py
```

No enumeration of infinitely many parameter values is claimed. The closed length-three residue-class formula invokes classical maximum partial triple-system existence results. Independent mathematical audit has not been performed.
