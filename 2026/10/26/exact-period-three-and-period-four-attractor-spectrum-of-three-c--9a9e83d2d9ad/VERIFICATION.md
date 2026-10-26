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
# Reproducibility and verification

Run the included standalone `verify.py` with Python 3; it uses only the standard library and reads no external dependencies. Its output should match `verification_output.txt`.

The checker enumerates every one of the \(49\) nonempty ordered support pairs, independently identifies the recurrent support set, calculates the three support-depth matrices, and verifies the exact return permutations of all periodic support types. It then implements the original vertex-neighbour update without calling the support transition, enumerates \(24,606\) labeled configurations across \(22\) part-size pairs, and compares every orbit's transient depth and exact period with the closed formulas.

The all-size proof is the support-map factorization and the finite \(49\)-state classification; small full-state experiments only corroborate its use for labeled graphs. Verification does not establish novelty or replace external scientific review.
