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

# Reproduction and limits

Run `python checker.py` with a standard CPython installation. The checker uses integer bucket sums for every quadratic-frequency point. It tests the exact criterion that all coefficients of the polynomial in the prime root of unity coincide; no float tolerances are involved. All nonzero three-level sign sequences in prime orders five and seven are exhausted. Another 10,000 seeded rational-integer vectors in prime order eleven are checked. The all-prime theorem is proved analytically in `RESULT.md`; finite diagnostics do not establish it and no external independent review is claimed.
