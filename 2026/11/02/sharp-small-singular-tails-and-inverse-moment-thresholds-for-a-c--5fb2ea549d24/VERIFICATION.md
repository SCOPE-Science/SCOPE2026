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

# Reproducibility checks

Run `python verifier.py` with Python 3.10 or later. The script uses only the Python standard library and a fixed random seed. It checks the closed-form \(L=2\) CDF, two exact first constants, direct Gram and condition-number algebra on seeded phase samples, the second-order local expansion at shrinking scales, and a Monte Carlo comparison with the theorem's coefficient. The script prints the actual counts of assertions and draws; the Monte Carlo checks are corroborative and are not a proof of the limiting theorem. The analytic proof in RESULT.md supplies the all-sample-count small-ball limit, the moment-integrability criterion including its borderline, and the Gaussian comparison.

The proofs assume exact arithmetic and independent continuous uniform phases. No verification is asserted for general high-dimensional target operators or for finite-precision code execution. Independent audit has not been performed.
