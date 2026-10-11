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
# Verification and reproducibility

The general proof uses only the explicitly reconstructed dual Lipschitz polytope, averaging of positive quadratic forms, convexity at square corners, and weighted Cauchy--Schwarz on facets. The optimal parameter is \(a_0=4s^2/(1-2s^2)\) for \(s=t/2\), and both sides of the transition are optimized analytically in RESULT.md. This establishes every real \(0<t\leq1\); it does not rely on finite enumeration.

Run the included standard-library code with `python3 verify_ultrametric.py`. It performs 1,800 exact-rational checks on rational \(s\) values and quadratic parameters bracketing \(a_0\), including the endpoint \(s=1/2\). The expected and independently observed output is `FOUR_POINT_ULTRAMETRIC_EXACT_RATIONAL_OK 1800`.

No floating point approximation, opaque external library or external data file is needed. The computation checks sampled rational values only, not all real parameters or an arbitrary ellipsoid. Full-dimensional optimality follows instead from the finite symmetry averaging inequality in the proof.

No independent audit has been performed.
