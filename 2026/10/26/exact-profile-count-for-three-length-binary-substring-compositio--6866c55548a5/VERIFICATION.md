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

The standalone `verify_profiles.py` uses only the Python standard library and runs from any directory with `python3 verify_profiles.py`. It checks the rational sum over all endpoint-status cases through a **formal polynomial identity** with integer coefficients; no floating-point arithmetic is used. It verifies the period-four closed-form coefficients, independently generates every literal observation for all binary words of lengths three through fourteen, checks each run-statistic equality, and checks profile counts by a distinct prefix-extension DP through length thirty-five.

The polynomial identity certifies the displayed rational-function simplification after accepting the separately proved run-signature lemma; finite word enumeration is secondary validation. No check on a finite range by itself claims to prove equality at every length. The public source and its model are identified in RESULT.md. No independent audit has been performed.
