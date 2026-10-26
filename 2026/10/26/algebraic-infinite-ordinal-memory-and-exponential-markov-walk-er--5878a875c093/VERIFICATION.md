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

# Reproducibility checks

Run `python checker.py` using Python 3 and its standard library only. It reconstructs the exact rational four-cell Markov transition matrix by affine cell intersections; separately calculates the preimage-interval probability of an all-rise word for lengths 1–9; verifies all-rise probabilities from the hidden two-state Jordan restriction for lengths 1–20; and checks the conditional probabilities and the surrogate eigenvalue. Expected output is preserved in `checker_output.txt`. The infinite run-length identity, exclusion of every finite Markov order, and asymptotic overprediction require the analytical proof in `RESULT.md`; finite verification is not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
