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

# Verification of the homothetic-frustum Makai-volume law

The proof in `RESULT.md` verifies the exact primal-volume formula by Cavalieri integration and the polar difference-body volume by evaluating its one-dimensional fibers. The central identity is the polar fiber length \((2-(1+t)h_{B-B}(u))/(1-t)\) for \(u\) in \((B-B)^\circ\), and zero otherwise. The gauge integral over the polar base is exactly \((d-1)/d\) of its volume. Multiplying produces the base-independent formula for every dimension and convex base, without smoothness assumptions.

The exact polynomial identities \(F_d'(t)=2(1-t)\sum_{j=0}^{d-2}\binom{j+2}{2}t^j\) and \(2d-F_d(t)=(1-t)^2\sum_{j=0}^{d-2}(j+1)(d-1-j)t^j\) give strict monotonicity and the sharp quadratic gap. The dimension-three inequality uses the published planar Eggleston result and its triangle equality characterization. No unproved all-dimensional Makai lower bound is assumed.

The standalone `verify.py` ran successfully on the actual scientific files and printed `VERIFY_OK symbolic_dimensions=2..39 numeric_cases= 16`. It compares symbolic polynomials and direct convex-hull/halfspace volumes of representative nonsymmetric frusta in dimensions three and four. Such finite checks are supplementary and do not establish the quantified theorem by enumeration. The endpoint \(t=1\) is interpreted only after affine normalization, since the displayed unnormalized body is dimension deficient there. No independent scientific audit or external certification is asserted.
