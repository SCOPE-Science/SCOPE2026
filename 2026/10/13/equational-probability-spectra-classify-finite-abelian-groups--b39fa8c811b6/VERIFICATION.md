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

# Verification and reproducibility

Execute `python3 verify.py` with the Python standard library and no external dependencies. The output recorded from execution of the packaged script is:

```
EXACT_GROUP_TYPES=516 EQUATION_CHECKS=604 VERIFY_OK
```

The script enumerates all isomorphism types of finite abelian groups of orders at most \(256\); for every type it computes the spectrum by exact rational arithmetic, applies the stated inverse reconstruction, checks the divisor-count formula, and tests for collisions. For selected small groups, it independently enumerates solutions of \(604\) two-variable linear equations instead of using the spectrum formula to count solutions. It also rejects a nonconcave primary profile and a missing coprime-primary combination.

These checks are exhaustive only in their explicitly bounded finite domains. No computation establishes all-dimension correctness, novelty, or independent validation. The general theorem is proved by homomorphism fibers, Bézout's identity, prime-primary decomposition and conjugate partitions. Literature equivalence risk is identified in REVIEW.md.
