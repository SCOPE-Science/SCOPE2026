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

The source checker is `verification/degree10_shape_check.py`. It enumerates all 163 subsets \(S\subseteq\{2,\ldots,9\}\) with \(|S|\le4\), applies the necessary column-count inequalities for every pair \((n,k)\) whose product indexes a listed column, and asserts the exact survivor list. The checker uses only integer arithmetic and the Python standard library. Actual output:

```text
tested_shapes=163
survivors:
S=[]; T=[2, 3, 4, 5, 6, 7, 8, 9]
S=[4, 7]; T=[2, 3, 5, 6, 8, 9]
S=[4, 8]; T=[2, 3, 5, 6, 7, 9]
CHECK_OK
```

The code checks only the finite combinatorial elimination step; it is not used as a substitute for the proof. The floor/ceiling exclusions and the application of the González–Karu theorem are written out in RESULT.md. The independent-audit channel remains unperformed.
