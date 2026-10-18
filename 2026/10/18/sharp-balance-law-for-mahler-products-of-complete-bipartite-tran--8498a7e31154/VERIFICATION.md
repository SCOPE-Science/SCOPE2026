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

From the package directory run `python3 verify.py`. The program uses exact rational arithmetic in the standard library for all analytic finite comparisons. It checks 81 pairs by two independent rational primal-volume expressions and two Mahler normalizations, and 64 adjacent balancing pairs by the exact sign-change/Vandermonde certificate. Optional NumPy and SciPy support eight geometric convex-hull and halfspace-polytope volume calculations. The observed run reported: `PASS: 81 exact independent-volume identities, 64 strict-balancing certificates, 8 primal/polar hull checks`.

The analytical proof establishes all infinite-parameter assertions; finite checker cases test formulas and normalization only. Public h-star and Banach geometry references are cited in RESULT.md. Independent audit has not been performed.
