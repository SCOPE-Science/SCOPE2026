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

The standalone `verify.py` script uses only the Python standard library and high-precision `Decimal` arithmetic. Run `python3 verify.py` from the folder containing this file and RESULT.md. It checks 10,000 log-spaced informed-initialization cases, 13 specified additional cases, 199 positive small-step starts against the exact product hitting rule, and a strict positive post-reset comparison. The script reports `VERIFY_OK` on success.

The proof in RESULT.md, rather than the finite checks, establishes every continuum assertion, sharp irrational switching boundary, and golden-ratio asymptotic. Decimal values approximate irrational boundaries, so the exact equality statements at those boundaries are algebraically proved in the manuscript and are not presented as certified by numerical tests. At extreme startup scales binary floating point can spuriously produce an earlier zero due to rounding of a positive gap; no floating-point implementation guarantee is claimed.
