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

The analytical argument obtains finite-population factorial moments, transfers them through conditionally independent errors, derives a unique global inverse, and proves the sharp two-result ambiguity. It also establishes the exact population-moment feasibility condition for exchangeable binary triples.

Reproduce the independent enumerations by running `python verify.py` in the same directory as `certificate.json`. The Python standard library suffices. The script enumerates every ordered latent vector and reported bit vector with exact fractions. It checks 216 assay/population configurations and nine constructive two-result coincidences; output is the exact JSON certificate.

Computational checks establish finite examples, not the theorem for arbitrarily large populations. The mathematical proof supplies the all-\(N\) argument. No estimator, uncertainty interval, field validation, or external independent scientific audit has been performed.
