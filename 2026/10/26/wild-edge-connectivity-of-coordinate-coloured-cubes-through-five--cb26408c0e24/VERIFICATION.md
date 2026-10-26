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

Run `python3 verify.py` beside `certificate.json`. This verifies the existence side of the exact four-cube value and the stated five-cube upper bound, by checking graph connectivity after perfect-matching contractions in all four input dimensions. The proof supplies the separate unrestricted counting lower bound. The recorded execution is embedded as `verification_output.txt`. The lower bound in dimension five is nineteen, and twenty is **only an upper bound**. No exhaustive search for smaller fifth-dimensional wild sets is claimed. The certificate lists are actual edge pairs, not a solver-status assertion. Independent review has not been performed.
