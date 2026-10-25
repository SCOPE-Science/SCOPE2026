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

# Reproducibility and scope

Run `python3 verify.py` from the same directory. The checker uses Python's standard library and integer arithmetic. It enumerates all matchings of sizes \(n=2,3,4,5,6,7\) (respectively 3, 15, 105, 945, 10395, and 135135 objects); for every size it verifies the exact short-chord factorial deletion transform for \(0\le k\le n\), then verifies the deterministic single-chord crossing-loss bound for all eligible anchors of lengths at most three.

Observed completion:

```
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 2 3 k=0..2 j<=3
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 3 15 k=0..3 j<=3
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 4 105 k=0..4 j<=3
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 5 945 k=0..5 j<=3
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 6 10395 k=0..6 j<=3
EXHAUSTIVE_DELETE_AND_FACTORIAL_PASS 7 135135 k=0..7 j<=3
VERIFY_OK total matchings 146598
```

These finite tests do not prove the asymptotic claims. The rigorous argument requires the uniform deletion coupling, the known Gaussian approximation for random chord crossing numbers, and the mixed factorial-moment uniqueness argument stated in RESULT.md. Reproduction does not constitute independent scientific auditing.
