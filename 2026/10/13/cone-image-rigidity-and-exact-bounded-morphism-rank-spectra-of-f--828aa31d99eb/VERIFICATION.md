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

The proof establishes the cone image equation for every bounded map and derives the recurrences by an exhaustive first-level decomposition. No numerical experiment is used to infer an infinite theorem.

The standalone script `CHECK.py` uses only the Python standard library. Execution from a clean package (`python3 CHECK.py`) returned:

```
d=2 h=0: endomorphism rank={1: 1}; idempotent rank={1: 1}; candidates=1
d=2 h=1: endomorphism rank={1: 2, 3: 2}; idempotent rank={1: 2, 3: 1}; candidates=27
d=2 h=2: endomorphism rank={1: 4, 3: 28, 7: 8}; idempotent rank={1: 4, 3: 8, 7: 1}; candidates=823543
d=3 h=0: endomorphism rank={1: 1}; idempotent rank={1: 1}; candidates=1
d=3 h=1: endomorphism rank={1: 3, 4: 6}; idempotent rank={1: 3, 4: 1}; candidates=256
d=4 h=1: endomorphism rank={1: 4, 5: 24}; idempotent rank={1: 4, 5: 1}; candidates=3125
VERIFY_OK independent brute 826953 function tables; 16 rank-structure cross-checks
```

In the brute routine, a map is tested by direct equality of the full image of each successor cone and the target cone of that vertex's image. This definition-based check is independent of the child recursion. Idempotence is tested pointwise by composition. Higher-height cross-checks concern rank extremes and automorphism counts only, not exhaustive function tables. The script's checks establish finite reproducibility and are not an independent mathematical audit.
