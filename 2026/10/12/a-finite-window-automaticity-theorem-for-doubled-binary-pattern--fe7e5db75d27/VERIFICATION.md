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

# Reproduction and proof boundaries

Run `python3 verify.py` with Python 3 and no third-party packages. The checker computes occurrence parity two ways and tests the exact append identity and bounded-window criterion over 57 nonzero terminal-zero blocks of lengths 2–6, 512 integers for each append test, and differences 1–159 for the criterion. It also checks two explicit small-pattern families to difference 1000.

Expected output: `VERIFY_OK positive_pattern_doubling_cases=9063 append_checks=29184 two_explicit_families=2000`.

These finite computations check implementation agreement, not infinite completeness. The all-positive-difference theorem is proved by the append-zero identity, least-congruence comparison, and regular-language construction in RESULT.md. No independently performed audit or human validation is claimed.
