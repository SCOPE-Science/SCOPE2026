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

The Python 3 standard-library `verify.py` enumerates the graph vertices explicitly and computes the minimum Hamming distance to every vertex of a canonical geodesic. It separately implements the claimed ballot polynomial and product formula, and tests their full coefficient arrays without calling the proof formula for the direct distances. It also enumerates every candidate unoriented geodesic in twelve small mixed products and compares optimal-path counts directly against the counting formula.

Recorded replay of the actual standalone program:

`VERIFY_OK binary_profiles=65 mixed_profiles=1474 exhaustive_optimal_geodesic_cases=12`

The binary checks range over dimensions one through ten; the mixed checks use alphabet sizes two, three, and four in dimensions up to four, and include changed-coordinate order reversals. Exhaustive counts include dimensions up to four and mixed alphabets. This finite computational evidence does not certify the theorem for unbounded parameters; the reflection-principle and coordinate decomposition provide the analytic proof.

The first-public-date evidence for the initiating source is the arXiv v1 submission on 2026-10-14, with time recorded as 18:17:58 UTC. Historical novelty is not guaranteed by search coverage.
