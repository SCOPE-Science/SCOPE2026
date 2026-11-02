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

# Verification summary

Execute `python3 verify_density.py` in this directory. This verifier rebuilds every local divisor sum from scratch, checks each of the 7,676,370 exponent vectors using integer cross-products, and recomputes the exact density coefficient. A separate `verify_density.cpp` program gives an independent implementation with Boost.Multiprecision and checks the same aggregate certificate. Both were successfully replayed from the finalized package.

Observed Python output:

```
VERIFY_OK patterns=7676370 good=2837267 equal=6
coefficient=12117705984441349391635228560689/1593139205846841220399104000000
certified_density_greater_than=0.77
```

The symbolic CRT/squarefree Euler-product argument handles the infinite density; finite enumeration alone would not prove the claim. Only a lower bound is proved. A separate independent mathematical audit has not been performed.
