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

# Reproducibility and scope

Run `python3 verify_geometric_period.py` in a directory containing this file and the script. It uses the standard library and computes the coefficients via a Stirling recurrence rather than via the proof's inclusion–exclusion identity. The check traverses every modulus from 2 through 100, tests the eventual coefficientwise period over a consecutive window, checks all strictly shorter period lengths, and checks sharpness of the starting index. A separate exact-integer comparison tests 630 inclusion–exclusion identities.

Observed output:

`VERIFY_OK moduli=99 period_pairs=6070 minimal_preperiod_checks=99 independent_coefficient_identities=630`

The universal assertions require the proof in `RESULT.md`. The finite verification is not exhaustive over indices and moduli. Self-review was conducted; independent validation was not performed.
