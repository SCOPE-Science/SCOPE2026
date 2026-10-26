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

# Mathematical verification

The analytical proof is in `RESULT.md`. It checks the domain of positive prices, positive edge weights and at least two leaves, all equality conditions, the normalized resistance-pair constraints, and the price threshold including equality.

`verify.py` is a reproducible supplementary computation. It uses seeded random prices and budgets to compare the formula with direct pairwise resistance diameters and with 8,100 arbitrary asymmetric budget-feasible competitors. It numerically solves the independent normalized convex optimization on 54 instances, verifies 21 effective resistances by exact inverse reduced graph Laplacians on rational test cases, and approaches the sharp factor-two comparison. Execute `python verify.py` in a directory containing this file. The expected check counts and floating-point tolerances are recorded in `verification_output.json`.

Finite tests cannot certify the all-real, all-size classification: the complete proof is the two-case normalized reciprocal-price minimization. An accessible full-text publication proves the underlying electrical tree-resistance identity, whereas its exact maximum-resistance design with heterogeneous prices is not addressed. No independent external mathematical audit or validation is claimed.
