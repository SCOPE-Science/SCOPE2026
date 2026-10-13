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

The included `artifacts/verify.py` independently constructs \(S_m(\ell)^k\) from graph distances and constructs the certificate matrix from the proof using exact integer arithmetic. It checks that the off-diagonal support agrees exactly with the graph and that the nullity is \((m-1)k\).

For every tested profile of order at most \(13\), it also enumerates initial vertex sets in increasing cardinality and simulates the standard zero-forcing color-change rule directly, confirming that the first feasible cardinality is \((m-1)k\). A larger constructive sweep checks the matrix support and nullity without brute-force zero forcing.

Recorded output:

```text
ALL CHECKS PASSED
bruteforce_profiles=18
matrix_profiles_small=18
constructive_profiles=100
small_order_limit=13
```

These finite checks are only stress tests. The universal result rests on the symbolic rank, support, kernel-dimension, and squeeze argument in `RESULT.md`.
