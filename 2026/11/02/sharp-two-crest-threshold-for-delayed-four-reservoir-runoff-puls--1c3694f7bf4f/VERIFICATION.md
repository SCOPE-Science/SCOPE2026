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

The exact domain is two equal instantaneous inputs at a nonnegative lag through identical four-stage Nash linear-reservoir cascades of positive outflow rate. The analytic result is a one-crest versus two-crest phase classification for all nonnegative real lags, including the unique threshold and all boundary cases.

To replay the finite checks using only a standard Python 3 installation, run `python verify.py` alongside this file. The checker computes the critical root by Decimal arithmetic, tests the cubic discriminant formula by exact rational arithmetic, compares the physical derivative with an independently coded derivative, and verifies the root-count classification for fixed and seeded-random parameter selections. Its output is `VERIFY_OK assertions= 3491`, preceded by the approximately 80-digit critical-root value.

The universal proof is in RESULT.md. Finite root checks do not certify infinite cases. No direct empirical flood data, independent audit, external formal proof certification or claims about nonlinear hydrological routing are present. Numerical root-enclosure digits are not a claim of physical measurement precision.
