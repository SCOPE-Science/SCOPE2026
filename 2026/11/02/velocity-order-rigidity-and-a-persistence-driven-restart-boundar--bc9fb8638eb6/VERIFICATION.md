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

# Reproduction and scope of verification

Run `python3 verify.py` in this directory, using Python 3 and the standard library. It reports `PASS: 1226 finite checks` when successful. The test constructs independent finite-difference mixed-boundary solutions, compares killed-resolvent formulas with exact drifted-Brownian transforms, verifies both local restart-threshold limits, checks renewal-response signs and checks ordered trajectories using common discrete noise. A test is not an infinite proof, so positivity of the Green kernel, the continuous-time comparison, the unique passive root and the two persistence limits are established in the written derivation.

The checks do not establish a unique crossover persistence, finite-activity phase-boundary uniqueness, or nonrenewing resetting dynamics. Neither independent audit nor independent validation has been performed.
