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

# Reproducibility and limits

Run `python verification/check_exact.py` with a Python 3 standard-library interpreter from the package root. This independently assembles the graph incidence data, the weighted grounded Laplacian and its exact rational inverse, and all absolute rows of the symmetrically rescaled edge projection. It checks all edge rows and a sign-vector extremizer in 24 test profiles, including 478 exact comparisons. It prints `PASS` when all assertions hold.

The infinite family is proved in `RESULT.md` by an explicit tensor resolvent and heat-kernel sign argument; finite exact checks do not replace that proof. The code does not enumerate every graph size, does not certify mathematical priority, and does not constitute independent review. Conductance optimality and its equality case follow analytically by AM--GM, not from exhaustive numerical optimization.
