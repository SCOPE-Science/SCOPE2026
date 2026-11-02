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

Execute `python3 check.py` using the Python standard library. The check runs on the exact standalone code embedded with this package; it has no network dependency and does not use external files. It tests the analytical transition equations, counts distinct roots, confirms the exact Euler-product identity in 4,000 deterministic random trials, numerically approximates the unique propagated-profile median, and checks the strictly contracting/strictly positive profile perturbations and particle-coupling identities. It also reports the approximate threshold and median values for independent comparison.

The decisive proof is mathematical rather than experimental: a quadratic equation and convexity classify the exact meshes for all positive curvature parameters; concavity, Jensen's inequality and elementary constants give the strict median gap; the implicit-function theorem proves persistence for all sufficiently small positive perturbations. The numerical checks do not establish an exhaustive search or infinite-parameter verification. No independent audit has been performed.
