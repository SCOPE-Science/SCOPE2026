---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On either invariant cost face and at μ₁/(μ₁+μ₂)=q*, dividing the derivatives of 1/Q(x) and r away from x=q* yields a linear equation in 1/Q; the integrating factor is ((1−r)/r)^κ, κ=(N−1)c₀/μ. Direct differentiation of the resulting first integral proves conservation also at x=q*. Its Hessian at (q*,r*) is positive diagonal: Q has a nondegenerate maximum at q* and the r derivative of the bracket K−κ/(rQ) is positive at r*. The equilibrium is the only interior zero of the vector field. Thus its small Morse levels are closed regular orbits, and the linear frequency squared is μc₀q*(1−q*)(1−r*), giving the limiting period. Independently of the local construction, integrating the two log-odds derivatives over any open-face periodic orbit gives mean x=q* and mean rQ=c₀/b. Hence mean r−r*=mean[r(Q*−Q)]/Q*>0: equality would force x identically q* and then r identically r*. The bottom row of the full variational equation is purely normal along the face, with coefficient ±(α−β)g, so the transverse exponent is exactly its time average. Affinity of g and mean x=q* give the strict upward shift at β and downward shift at α; these are shifts relative to the equilibrium, not unconditional absolute signs. In the tuned example the equilibrium costs have g=0 and 3/8 with risk slope 15/8, giving opposite absolute signs. This is transverse stability, not attraction within the neutral planar annulus. The supplied verify.py and verification notes were inspected, not executed; their finite symbolic and numerical tests are ancillary to the exact check.

## originality

PASS

Neither the three-variable model, the fixed-cost subsystem, nor scalar Floquet integration is claimed as new. The supported distinction is an exact center at resonance and the nonperturbative strict risk surplus on its cost faces, combined with the opposed cycle-versus-equilibrium transverse shifts and tuned opposite absolute stability. The earlier published subsystem flags that resonance as a Hopf rather than proving a center; the earlier indexed same-model result controls strictly interior collapse, not normal stability of resonant face cycles. Later indexed planar results materially overlap the center and risk excess, but omit the dynamic cost coordinate and the transverse law.

## value

PASS

This distinguishes genuinely neutral in-face oscillations from apparent Hopf attraction and shows that oscillations maintaining equilibrium mean cooperation increase mean risk. The exact excess changes invasion in the cost direction and can destabilize every local cycle at a normally neutral equilibrium. That is useful stability information not captured by equilibrium-only or in-face analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
