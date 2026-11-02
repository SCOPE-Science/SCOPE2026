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

Run `python verify.py` with Python 3.9+ from the extracted package directory. No network access, external libraries, or data files are required. The run reported:

`VERIFY_OK exact_profile_checks=206077 sharp_witnesses=520`

The checker implements the singleton-ballot characterization of reciprocal JR with exact fractions. It exhausts all four-candidate nonempty approval profiles with two or three voters over a three-level rational quality grid, checks deterministic profile tests at four and five voters, and verifies sharp witnesses for integer electorates up to forty voters. These finite computations corroborate the statement but are not exhaustive over all real qualities or all electorate sizes. The universal claim is supported by the analytical proof in `RESULT.md`; no independent scientific audit or external certification has been performed.
