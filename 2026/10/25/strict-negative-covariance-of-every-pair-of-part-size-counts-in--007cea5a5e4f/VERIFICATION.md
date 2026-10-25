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

# Verification

Run `python3 verify.py` from the extracted package directory, requiring no third-party dependencies. Actual execution: `PASS: 10716 exact integer/rational assertions, unrestricted theorem from the analytical proof; p(100)=190569292`.

The executable recomputes partition numbers by dynamic programming. It verifies 75 two/three-step inequalities at base points 1 through 25, the finite monotonicity and tail-ratio checks, every covariance numerator at integer sizes 2 through 32, and complete independent enumeration of partitions through size 12 for comparison with both marked-part formulas. It checks a sharp nonextension: positive covariance between part-size-presence indicators at size 3.

For all larger indices, the proof relies on the published strict log-concavity theorem [2] and the Bessenrodt–Ono partition-number product inequality [3], followed by finite telescoping identities. No finite execution certifies infinity, and no independent audit or formal proof assistant validation has occurred.
