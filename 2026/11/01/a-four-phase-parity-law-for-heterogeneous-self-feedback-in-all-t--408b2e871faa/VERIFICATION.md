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

## Verification record

The embedded `verify.py` uses direct neighbor-list summation, not the analytic proof's characteristic polynomial or block construction, for its exhaustive trajectory checks. It also performs independent binary Gaussian elimination on matrix powers and compares the resulting kernel dimensions with those implied by the claimed Jordan forms.

The verified recorded execution of this script returned:

```
HETEROGENEOUS_COMPLETE_XOR_VERIFY_OK matrix_pairs= 169 binary_pairs= 24 binary_states= 11280 GF4_pairs= 8 GF4_states= 47360 assertions= 2235
```

Checks cover ordered class sizes from two through fourteen for binary matrix powers, plus the indicated finite binary and four-element-field exhaustive cases. The all-size proof, not the finite ranges, supplies the universal statement. This record is not independent audit evidence.
