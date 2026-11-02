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

The mathematical argument explicitly proves mixed factorial-moment convergence and the clean local-profile reduction for the pure successor/equality language. There is no reliance on a finite experiment to infer an infinite theorem.

Reproduction: execute `python3 checker.py` with Python 3 and standard library. The script enumerates all configurations of three independent orders of size three through five, fixing the first order by relabeling symmetry; it checks the two independently implemented collision-count routines and exact means. It also tests the canonical local profile on clean three-order structures and checks the cardinality expression. The recorded run printed `ALL_CHECKS_OK`.

Only finitary checks were executed. No independent audit, external theorem prover, exhaustive literature priority certification, or machine proof of asymptotic convergence was performed.
