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

The standalone `verify_counts.py` enumerates bounded-run words via position/last-letter/run-length/signed-count states; it does not reuse the block rational generating function. It independently enumerates all words at lengths 1 through 7, exactly computes the length-48 unsymmetric and mirrored counts, and checks all stated asymptotic constants. The analytic proof, not finite experimentation, establishes the infinite-limit claims. Independent scientific validation has not been performed.
