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

# Verification notes

The proof derives the exact return-time ceiling and normalized first-return coordinate from the two branches of the map. Its first nonstandard step is a uniform lower bound on the first image over the entire normalized section. Subsequent limiting statements use a fixed shrinking-parameter phase; the only excluded initial points form a countable measure-zero resonance set. The shifted exponential change of variables is exact, and conditional densities are computed by an explicit Jacobian. A one-dimensional implicit-function expansion yields the signed first correction; a geometric left-tail bound justifies exchanging the limit and mean.

The standalone `verification.py` runs only with Python's standard library. It checks exact rational direct orbits for a square-root specialization at multiple shrinking parameters, exact normalization and first moment of the closed-form limiting distribution, and finite-parameter tail corrections by floating-point bisection. The expected success string is `EXACT_GRAZING_RETURN_CHECK_OK`. Results for these finitely many cases are consistency tests only; the analytical proof establishes the general claims. No independent audit or validation has been performed.
