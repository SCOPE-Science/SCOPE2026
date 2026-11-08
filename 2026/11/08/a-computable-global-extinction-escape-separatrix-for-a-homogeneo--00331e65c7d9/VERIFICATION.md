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

# Verification and limits

The standalone `check.py` was executed successfully with Python's standard library. Its reported checks were `EXACT_HOMOGENEOUS_PROJECTIVE_FACTORISATION_OK`, `PROJECTIVE_CONTRACTION_AND_INVARIANT_THRESHOLD_OK`, `SYMMETRIC_THRESHOLD_CURVATURE_AND_EXTREMA_OK`, `LOG_RADIUS_TRICHOTOMY_HIGH_PRECISION_CHECKS_OK`, and `ALL_FINITE_CHECKS_PASSED`.

The rational checks compare the original quadratic polynomial with its factorization in dimensions three, four, and seven. Floating-point checks compare the invariant graph's functional identity, the projective spread, and the exact symmetric curvature coefficient for selected positive-parameter cases. Decimal checks at 180 digits examine decaying, critical, and expanding radial trajectories without floating overflow.

These experiments do not verify infinitely many dimensions, all parameter values, or the limiting asymptotics by enumeration. The proof is analytical: it uses a strict ratio contraction on the compact open simplex, a uniformly bounded geometric logarithmic tail, and an exact iteration identity. The explicit truncation error excludes implementation roundoff, which must be bounded separately for numerical certification.

No independent mathematical audit was conducted.
