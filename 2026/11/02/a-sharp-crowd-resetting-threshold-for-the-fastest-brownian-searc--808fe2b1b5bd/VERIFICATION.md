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

The standalone `verify.py` uses the Python standard library and completes 209 numerical consistency assertions. It checks the exact Brownian hitting-time Laplace transform, its finite-horizon complementary-error-function representation, subcritical rate-function roots, and normalized discounted probabilities.

Run `python verify.py` from a directory containing the extracted artifacts. The proof of the asymptotic regime classification is contained in `RESULT.md`; the computational checks are finite and supplementary. Analytical claims involving all \(N\) are not inferred from finite samples.

The published finite-size renewal formula is an important predecessor, and independent publication-priority and mathematical audits have not been performed.
