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

# Reproducibility and proof checks

Run `python checker.py` using Python 3 and SymPy. The checker was executed successfully and verifies, by exact symbolic algebra rather than floating-point evaluation, both affine branch inverse identities and Jacobian determinants, triangle area and moments, Perron images, all first 24 lag matrices, the limiting covariance rank and null vector, and the pointwise coboundary identity on both branches. No symbolic experiment is asserted to certify an infinite family of lags or a limit distribution; these are proved by the transfer-operator recursion, summability and bounded reverse-martingale limit argument in `RESULT.md`.

A separate domain check confirms the all-orbit uniform bound \(2\) is sharp at \((2,0)\) for a single step. The 2024 source-date evidence is its arXiv v1 record, 2024-09-27, not its later journal publication. The 2015 and 2025 related works remain incompletely accessible for publication-priority assessment. Independent audit is not performed.
