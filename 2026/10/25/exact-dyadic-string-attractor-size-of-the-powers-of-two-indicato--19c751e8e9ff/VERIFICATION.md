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

Run `python3 checker.py` in the same directory as this file. No third-party packages, network access, or external data are needed.

The program constructs the binary powers-of-two prefixes directly, generates the explicit attractor positions and uniquely occurring factor intervals, and checks both the lower-bound certificates and actual factor coverage. It enumerates every distinct factor for \(2\le k\le9\); for \(k=10\) it checks only all unique-factor witnesses and disjointness. The final output line is `PASS: all tested construction and lower-certificate instances`.

Observed tests: \(k=2,\ldots,10\) produce certified cardinalities \(2,3,3,4,4,5,5,6,6\). The infinite result is the proof in RESULT.md. Brute-force verification over these finitely many values is not an exhaustive proof for all \(k\).
