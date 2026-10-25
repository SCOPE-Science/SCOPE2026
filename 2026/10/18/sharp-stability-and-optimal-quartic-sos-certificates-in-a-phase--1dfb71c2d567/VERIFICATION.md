---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact polar decomposition has dr/dt=r^3[-a+gamma cos(4theta)] and dtheta/dt=r^2[omega-gamma sin(4theta)]. For 0<=omega<=gamma an invariant ray of positive cosine gives equilibrium at a=sqrt(gamma^2-omega^2) and outward flow below it, proving necessity. For a above the threshold, D=a^2+omega^2>gamma^2; with t=-gamma omega/D the quartic V=r^4+2t(x^2-y^2)(2xy) has positive SOS decomposition (1±t)/2 (A±B)^2. Independently verified its exact symbolic negative Lie derivative -dot V=4r^2 [A,B]M[A,B]^T and eigenvalue condition a(1±gamma/sqrt(D))>0. Proper strict V proves GAS including degenerate omega=gamma. Z4 averaging shows no strict quadratic if a<=gamma, while odd total degree cannot globally be positive; hence minimum strict polynomial Lyapunov degree 4 versus 2, with algebraic decay upper bound.

## originality

PASS

Ahmadi–Parrilo provides generic existence of SOS transformations of polynomial Lyapunov functions and Shevchenko et al. a general angular GAS criterion. Neither accessible statement determines an explicit sharp quartic and its minimum strict degree for this 3-parameter Z4 phase-locked family. A previous result for gamma<omega has rotating angular dynamics and cannot directly cover 0<=omega<=gamma. Priority risk remains for older planar equivariant homogeneous cubic classifications.

## value

PASS

The angular-locked sector of the canonical 1:4-resonant cubic normal form has invariant rays, a sharp sink-to-neutral/outward threshold, and a uniform explicit low-degree SOS certificate even where ordinary radial energy initially grows. The degree-2/4 sharp transition is a substantive stability/certification invariant within a natural symmetry family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
