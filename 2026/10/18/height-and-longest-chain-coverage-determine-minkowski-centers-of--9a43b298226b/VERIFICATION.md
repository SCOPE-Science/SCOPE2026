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

## Reproducibility

Run `python verify.py` using Python 3. The program requires only the Python standard library. It deterministically enumerates all choices of directed upper-triangular edges on up to five labeled vertices, takes transitive closures, and tests every partition into chain and order variables. The result is 33,866 poset/partition instances (transitive closures can repeat) and 175,583 compressed-path inequalities.

All checks are integer arithmetic: explicit zero-one support witnesses, the integer-rescaled canonical center, and positive-slack witnesses for every noncritical coordinate/arc. The script verifies the finite certificates but does not establish the arbitrary-size theorem. The written proof addresses the infinite family. No independent audit or external certification has been performed.
