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

The analytic derivation in `RESULT.md` is the evidence for the all-size claim. It uses an exact Markov-generator equivalence, independent exponential thresholds, a uniform empirical-distribution bound, an explicit bound on the flooding horizon, and a late-stage susceptible-time integral to obtain the limiting terminal-class law. The exact balanced finite identity is proved by symmetry after the first forced infection into the opposite part.

`checker.py` was run with Python 3 in the same directory as the embedded file. It reported **PASS 3468 exact rational/transition assertions**, using forward and backward rational computations and all balanced graphs through part size twenty. It also printed a single seeded finite stochastic diagnostic, not used for proof or historical priority. The finite checks do not certify the asymptotic theorem. No external independent verification has been performed.
