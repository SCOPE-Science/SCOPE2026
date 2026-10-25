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

From the directory containing the attached program, run \(\texttt{python3 verify\_s3\_behavior.py}\). The script enumerates exactly all 162 possible modular signatures, computes reachable sets through length 18 by both appending letters, checks the exact profile, and verifies full coverage in every length from 13 through 18. It separately evaluates all 36 permutation assignments on every binary word through length eight, comparing behavioral and signature equivalence without relying on the transition recurrence.

Observed stdout:

```text
EXACT_PROFILE 2,4,8,15,26,41,60,84,108,133,148,159,162,162,162,162,162,162
ALL_162_SIGNATURES_REALIZED_IN_EACH_LENGTH_13_THROUGH_18
DIRECT_GROUP_BEHAVIOR_MATCHES_SIGNATURES_THROUGH_LENGTH_8
VERIFY_OK
```

The finite test alone does not prove the all-length statement. The exact semidirect-product derivation of the signature, its converse, and the six-zero padding proof are supplied in RESULT.md; they are required for completeness. No probabilistic approximation, external solver, or third-party code is used. The independently audited status remains unperformed.
