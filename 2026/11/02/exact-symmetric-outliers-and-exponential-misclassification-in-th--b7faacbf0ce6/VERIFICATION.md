---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The packaged `verify.py` uses the Python standard library and requires Python 3.10 or later for `int.bit_count`. The recorded output is:

`VERIFY_OK low_profiles=120 parameter_sizes=40 exhaustive_m5=32768 errors_m5=1`

It checks the complete profiles at the exceptional scores 59, 60, and 61, the margins of the two stated surrogates outside that interval, the resulting one-profile errors, their orbit sizes, and all labelled coalitions in the 15-voter case. The four-profile obstruction and the orbit-size comparison establish symmetric optimality in the small-class regime, including the tie; the averaging argument rules out unrestricted zero error. Finite checks corroborate these arguments, not optimization over arbitrary real weights by enumeration.
