---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify.py` from this directory. The checker enumerates all starters in increasing cardinality for each \(F_n(m)\) with \(1\le n\le6\), \(1\le m\le4\), and for the triangle with one leaf at each vertex. It uses synchronous forceability to compute closure; this yields the same forcing sets as sequential moves because extra forces can only fill white targets sooner. The full minimum set families, not only their cardinalities, are compared with the stated formulas and descriptions.

The script checks the algebraic table specializations for five power-of-two parameters and nine odd field sizes. The computations do not test ring realizability. The analytic proof in `RESULT.md` supplies both the general graph theorem and the ring restriction \(n=2^r\) in the two-leaf family, including \(K_3(2)\) at \(r=0\).

Replay output:

```text
VERIFY_OK fan_profiles=24 separate_leaf_profiles=1 even_field_substitutions=5 odd_field_sizes=9
```
