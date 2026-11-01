---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the Fréchet linearization at a curvature -1 hyperbolic geodesic sphere: delta W=-Hess(u)-u(W^2-I), delta F=-(alpha/n)(coth R-1)^(alpha-1)(Delta u+n csch^2(R)u), and the area-average variation cancels measure terms because F is constant. Spherical harmonic eigenvalues yield degree-zero/degree-one neutral modes and strictly negative all higher-degree eigenvalues; degree two gives the sharp gap. Differentiating its q=e^(-2R) closed form and inserting hyperbolic ball asymptotics yields monotonicity and the exact V^(-2alpha/n) coefficient for every n>=2, alpha>0, R>0. No nonlinear all-initial-data convergence is inferred.

## originality

PASS

Best-of-knowledge: the exact all-degree linearized spectrum and its radius-dependent sharp gap for the specified shifted-alpha Gauss flow are not covered by identified published results on other curvature speeds or other ambient geometries. The directly matching recent Zhang article was located but inaccessible in full, creating a significant explicit priority risk; its absence alone is not grounds to assert noncoverage or failure.

## value

PASS

The exact degree-resolved, all-parameter relaxation spectrum of the natural stationary solutions identifies neutral symmetries, the optimal local shape rate and its sharp deterioration with enclosed volume. These quantities can inform volume-sensitive nonlinear estimates; the claim does not require or promise such an estimate. This is a motivated analytic refinement of a global-flow problem, not a renamed convergence assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
