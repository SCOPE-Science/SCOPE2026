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

The mathematical proof is given in `RESULT.md`. Its critical ingredients are the exact zero-position shift under iteration, the preservation of prefix-zero dominance, and the count of zero-prefix boundaries in the irrational mechanical-word partition.

Standalone reproduction: run `python3 verify_tortoise.py`. The script tests every coprime numerator for six rational denominators below the period threshold and compares two independent finite transformations. It checks 114,832 parameter tuples over \(k=1,\ldots,8\); a separate long-period Fibonacci-slope approximation is also checked. Observed outputs: `VERIFY_OK rational_cycles=114832 q_values=6 k_range=1..8 n<36` and `FIBONACCI_APPROX_OK`.

The rational checks probe the local combinatorial mechanism under exact integer arithmetic; they cannot certify the theorem for all irrational slopes or all factor lengths. Those ranges are established by the proof, with no external or independent scientific audit claimed.
