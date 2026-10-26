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

# Verification

Run `python check_path_green.py` with Python 3. It performs independent finite exact-rational matrix identities for every \(2\le n\le80\), checks the endpoint prefix-sum formula and records finite numerical comparisons with the analytic error bound. This is a cross-check, not a proof of asymptotic or uniqueness claims for all sizes.

The continuum derivative factorization, midpoint quadrature error, fixed-offset signed row comparison and eventual maximizer localization are proved in RESULT.md. All conclusions depend on the unweighted degree Laplacian convention, zero-mean Moore–Penrose inverse and counting \(\ell^p\) norms. No independent audit has been performed.
