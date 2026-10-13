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

The exact-rational test `verify_exact.py` reconstructs a strongly monotone affine system, first successful line search, projection, source secant guard, Case-I coefficient and ascent. Run with `python3 verify_exact.py`; the program prints `VERIFY_OK` if every rational identity passes. The general sharp coefficient is established analytically in `RESULT.md`, not by checking finite samples. No independent audit has been performed.
