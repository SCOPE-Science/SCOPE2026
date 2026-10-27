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

The analytic claim is proved by algebraic elimination, not by finite testing. The file `verify.py` uses Python standard-library exact rational arithmetic on the logarithmically normalized concentration exponent. It checks the exact two-triple witness (three matching readings, fourth differing), the critical continuous family, positive-geometry uniqueness, and four-corner parameter recovery on randomized rational profiles. Execute with `python3 verify.py` after extracting the package.

The checks do not address finite-precision stability, environmental boundary conditions, unknown injection time/location, noisy observations, or unverified general inverse results. Independent validation has not been performed.
