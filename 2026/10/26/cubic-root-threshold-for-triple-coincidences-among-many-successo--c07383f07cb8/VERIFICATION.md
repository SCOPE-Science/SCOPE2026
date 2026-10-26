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

# Verification record

Execute `python3 check.py` in this directory using Python 3 with only the standard library. The checker exhaustively tests the exact linear-order contraction count for each prescribed set of one, two, or three directed arcs over domains of sizes two through five, then enumerates all ordered tuples of successor paths in four small cases and checks the exact first and second factorial moments using rational arithmetic. No random-number sampling is needed.

Observed output:

```text
ORDER_ARC_CONTRACTION_CHECK_OK 1692
TRIPLE_COLLISION_EXACT_MOMENTS_OK 3 3 216 2/9 1/18
TRIPLE_COLLISION_EXACT_MOMENTS_OK 3 4 1296 8/9 14/9
TRIPLE_COLLISION_EXACT_MOMENTS_OK 4 3 13824 3/16 1/24
TRIPLE_COLLISION_EXACT_MOMENTS_OK 4 4 331776 3/4 53/48
TRIPLE_SUCCESSOR_CHECK_OK
```

The tests are finite identity checks. The limiting Poisson law, isolation, and sharp supercritical threshold are proved by the symbolic factorial-moment and variance arguments of `RESULT.md`; they are not inferred from this finite computation. No independent audit has been performed.
