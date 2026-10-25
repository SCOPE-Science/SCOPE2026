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

The companion `verify.py` (SymPy 1.13 or newer) checks two independent stationary second-moment formulas, the exact comparison identity and its polynomial elimination, rational sign examples and root intervals. Running `python verify.py` on the packaged copy returned `VERIFY_OK 481 exact/symbolic/numeric assertions`.

The proof in `RESULT.md` supplies the infinite-parameter steps absent from finite tests: contraction of both affine branches, one-positive-root sign structure of the comparison cubic, a unique positive root of the quintic by strict convexity, and uniqueness of its interior maximizing probability. The numerical root approximations are descriptive only. No independent external audit has been performed.
