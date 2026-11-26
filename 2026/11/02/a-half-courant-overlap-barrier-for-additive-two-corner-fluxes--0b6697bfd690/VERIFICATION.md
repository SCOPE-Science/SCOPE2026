---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the specified x-independent solution the normal derivative vanishes distributionally and the two contacts are transported at ±v. On the face each active set has length vt up to t=L/v and their intersection has length (2vt−L)_+. The four possible state values give an exact binary mixed-difference expansion for the flux; the two single-indicator terms agree with the independently isolated endpoint problems. Integrating the intersection length yields εv(H−L/(2v))_+²ΔΦ, including both endpoint horizons and equality at the threshold. If ΔΦ is nonzero the first derivative is continuous but the one-sided second derivatives differ by 2εvΔΦ. Vanishing on all subrectangles of the stated state domain gives Φ_pq=0 there (divide by area and shrink), hence separability and its converse. With positive-state tests this conclusion concerns the positive state rectangle; it does not determine unused negative states. For Φ=pq, diag(q,p) symmetrizes both Jacobians. A nonzero n_x gives a strictly positive discriminant contribution 4ε²n_x²pq, while n_x=0 gives the distinct speeds ±v. The symmetrized normal-direction x part has eigenvalues 0 and ε(p+q)n_x, and the y part has norm v|n_y|, so the uniform spectral bound is √29/5 in the example. The isolated value is 171/1000 and the hinge adds 16/1000; the squared full Courant bound is 2349/2500<1. The supplied rational checker was inspected, not run; the analytic derivation establishes the continuum claim for the explicit transported solution.

## originality

PASS

The supported distinct claim is an exact physical finite-face overlap defect for two independently transported contacts, with a sharp half-Courant transition, a separability criterion and a strictly hyperbolic sub-Courant-one witness. Published solvers furnish real face-plus-corner precedents, but do not by their inspected equations give the two isolated physical corrections or the resulting mixed-difference hinge. This is not a priority claim for inclusion-exclusion or corner transport generally.

## value

PASS

The explicit benchmark separates the onset of a missing physical interaction from ordinary full-speed CFL-one stability. Both corner predictions are exact in isolation, so the failure isolates the additive ansatz rather than quadrature or a limiter. The threshold, defect and zero condition give concrete tests for a class of corner-flux constructions without implying anything about the stability of an existing coupled solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
