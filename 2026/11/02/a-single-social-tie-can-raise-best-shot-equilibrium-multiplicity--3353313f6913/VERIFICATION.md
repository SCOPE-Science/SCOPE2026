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

# Reproducibility

Run `python3 check.py` from the directory containing that program. The check uses no external packages and reconstructs the best-shot game's binary best response directly by complete enumeration of configurations for all graph sizes from five through seventeen and all admissible new edges. It also tests the recurrence identities on large independent integer ranges and the limiting ratio numerically.

The replayed program printed `VERIFY_OK assertions=21353; exhaustive n=5..17; induction identity d=2..96,m=5..99` and returned exit status zero.

This is a finite regression and consistency certificate; it cannot replace the exact all-size proof in RESULT.md. No independent external audit has been conducted.
