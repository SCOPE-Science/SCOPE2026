---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducing the four covariance checkpoints

Run `python3 verify.py` using only the Python standard library. It sums integer weights over all ordered allocations at each of \(n=3,4,9,10\). It checks the total weight \(32^n\), the values of all four covariances as exact fractions, and their alternating nonzero signs. The summation over ordered allocations differs from the occupancy-triple calculation in `RESULT.md`. The two-box minimality argument for \(n\ge3\) is analytic.
