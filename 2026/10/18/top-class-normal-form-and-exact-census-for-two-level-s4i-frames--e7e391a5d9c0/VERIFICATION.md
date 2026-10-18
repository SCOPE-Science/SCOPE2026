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

# Reproducibility and limits

Run `python3 verify.py` with ordinary Python 3 and no installed dependencies. The script enumerates each labelled preorder on at most five elements by exhaustive off-diagonal bitmasks, tests transitivity literally, computes all predecessor-closed sets and each greatest modal equivalence class, and obtains the four aggregate statistics. It then independently enumerates all preorders on up to five total worlds in eight small two-level shapes, evaluates the two confluence clauses by direct quantifiers, constructs the normal-form family separately, and asserts equality of the **entire sets** of admissible relations. It checks the reported larger numerical counts through the exact formula. A successful execution ends in `VERIFY_OK`.

The literal entire-relation comparisons cover \((p,q)=(1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(2,3),(3,2)\). Counts at larger sizes are certified here only as arithmetic consequences of the mathematical formula, which is proved independently of enumeration in RESULT.md. There is no machine-checked proof of the unbounded theorem, and no independent external audit has been performed.
