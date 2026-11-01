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

# Verification and limits

A standalone standard-library rational checker is included as `verify_biclique.py`; run `python3 verify_biclique.py`. It enumerates all metric balls for each representative indicator occupancy on balanced bicliques of sizes \(2\le r\le8\), independently computes the uncentered maximal transform, and compares its edge variation with the four-orbit analytic expression. It then checks all admissible occupancy counts for \(2\le r\le45\) against the claimed sharp constant and verifies the two exact symbolic-comparison identities by integer substitution. The completed run reported 280 direct-ball comparisons, 33,418 cut-count comparisons, and 11,480 polynomial substitutions, all successful.

These checks do not certify infinitely many graph orders. The infinite statement is proved by the explicit ball classification and two polynomial identities in `RESULT.md`, which can be independently verified by expansion. The package does not address non-indicator inputs, unbalanced bicliques, weighted graphs, or independent review.
