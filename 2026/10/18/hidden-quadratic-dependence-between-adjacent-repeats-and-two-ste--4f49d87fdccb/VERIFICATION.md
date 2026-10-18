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

# Verification of word coincidence regression

Running `python verify.py` from a directory containing this file and the accompanying standalone program checks exact joint counts of all words in 18 finite parameter cases, for alphabet sizes from two through five and word lengths from three through the selected finite upper bounds. The program checks both binomial marginal distributions, zero covariance, every conditional mean, its quadratic representation, the explained-variance fraction and the mixed centered moment using `fractions.Fraction`.

The finite checker passed all included identities. It provides no exhaustive verification outside those 18 finite instances; the general theorem is established by the proof in RESULT.md. Historical priority has not been independently established. No external validation has been performed.
