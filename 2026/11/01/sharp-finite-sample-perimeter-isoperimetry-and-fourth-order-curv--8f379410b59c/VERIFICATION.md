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

# Verification and scope

Run `python3 checker.py` with a standard Python 3 installation. The code evaluates 184 independent finite diagnostics: 72 direct beta-sine integral comparisons, 99 strict coefficient inequalities, 4 exact-rational and Fourier series square checks, 4 seeded unit-circle Monte Carlo checks, 3 asymptotic checks, and 2 ellipse curvature checks. Its console output reports PASS and the independent square expectation \(5/32\) for three points and \(5/16\) for four points.

The infinite-series identities, uniqueness for all planar convex bodies, and \(O_K(m^{-6})\) error are proved analytically in `RESULT.md`. Computation alone cannot establish those universal claims. The periodic \(C^4\) hypothesis is needed for the high-order remainder and no statement is made about nonsmooth asymptotic coefficients. Independent audit has not been performed.
