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

The symbolic proof in `RESULT.md` proves the infinite family for all positive integers \(p,q\), using the principal-upset equality and case decomposition. The included `checker.py` enumerates all functions on each labelled carrier with \(1\le p,q\le3\), verifies order preservation and openness separately, and checks the predicted cardinalities. The checks have completed with `CHECK_OK`. Finite tests are supplementary, not a general proof. Full priority assessment of older finite-space endomorphism semigroups remains outside this verification.
