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

The proof gives the exact finite-sample perimeter decomposition whenever all edges receive samples, the explicit joint exponential endpoint-gap survival limit, moment uniform integrability, the Gamma/Uniform factorization of the Laplace transform, and direct evaluation of its first two derivatives at zero.

Run `python3 checker.py` using Python 3's standard library. The checker performs 70 random direct hull decompositions in each of three polygons, five-angle numerical moment quadratures, nine Laplace integral evaluations, and three 60,000-sample exponential comparisons. Numerical experiments do not establish the all-polygon theorem; the analytic argument in `RESULT.md` does.

No external or independent audit has been performed. The full law is established only for a fixed convex polygon as the sample size diverges.
