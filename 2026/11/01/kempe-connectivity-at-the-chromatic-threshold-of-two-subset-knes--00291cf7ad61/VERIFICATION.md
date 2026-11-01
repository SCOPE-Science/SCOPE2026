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

Run `python3 verify_bruteforce.py`, `python3 verify_components.py`, and `python3 verify_kempe.py` with Python 3.10 or later and no third-party dependencies. The direct search checks all canonically named optimum colourings for \(n=4,5,6,7\); the separate full labelled graph search checks component sizes at \(n=4,5,6\); the Kempe checker independently builds induced two-colour components and explores the complete Kempe graph at \(n=4,5,6\). All returned PASS on saved files. Finite runs do not certify the all-parameter statement, which follows from the constructive proof in `RESULT.md`. Independent audit has not been performed.
