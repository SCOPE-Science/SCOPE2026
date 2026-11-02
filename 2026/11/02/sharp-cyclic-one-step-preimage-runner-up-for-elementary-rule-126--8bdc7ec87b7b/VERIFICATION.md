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

The mathematical proof in `RESULT.md` supplies the all-length result. The included `verify.py` independently enumerates every one-step input on cyclic binary rings of lengths 1 through 16 and compares all output fibers to the exact zero-gap formula. It also performs a second family of checks by building labeled four-state de Bruijn matrices and comparing every trace with the formula through length ten.

Execute `python3 verify.py`. Its terminal success marker is `VERIFY_OK`. Computations are exact integers without numerical tolerances. This finite replay is supporting evidence and does not prove the infinite-length claim. No independent mathematical audit has yet been performed. Historical priority remains qualified by possible unindexed exact extremal statements.
