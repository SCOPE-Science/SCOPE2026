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

# Verification and limits

Reproduce arithmetic assertions with `python3 nash_checker.py`. It checks exact monomial identities, semigroup gap lists, length and conductor formulas for odd integers from 3 through 41; output is `CHECK_OK`. The symbolic proof establishes the formulas for every odd integer at least 3, without relying on enumeration. The generic exceptional residue field is a rational function field; these are local lengths, not point counts. Independent mathematical audit has not been performed.
