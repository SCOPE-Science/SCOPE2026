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
# Verification record

To reproduce, place all embedded files in one directory, install the packages named in `requirements.txt`, and execute `python verify.py`. The script verifies two rational exact-matrix identities, 240 rational majorization/Jensen instances, 540 direct Gaussian reconstruction identities, 35,000 seeded Gaussian draws against beta-prime quantiles/mean, and 44 rational dimension/first-two-moment consistency identities. Random diagnostics are approximate; the arbitrary-matrix theorem, convex order and complete moment thresholds follow from the mathematical proof, not the finite run. Standard Wishart density normalization and the standard majorization characterization are identified explicitly in that proof. The matrix formulas are exact-arithmetic statements, not a finite-precision numerical guarantee.
