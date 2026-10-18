---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Both quartics f=y^4−6y²z²+z^4 and g=(2√7/7)(f−(x^4−6x²z²+z^4)) are spherical degree-four harmonics. Equal exact sphere second moments 64/315 and zero cubic moments force identical exact volume and surface-area polynomials, while mean width=2 by zero average. Independent direct polynomial sphere moment computations verified Ef⁴=4096/36465, Eg⁴=241664/2501499 and gap 65536/4169165>0. Independent spherical-Hessian tensor identities verified ∫det(Aq)=−9∫q² and ∫qdet(Aq)=136∫q³ for these examples. Positivity of I+eps Aq for eps sufficiently small establishes smooth strict convexity. Width=2+2eps q then has different fourth centered moment, so laws differ.

## originality

PASS

Abas arXiv:2609.26202 full manuscript explicitly constructs centrally symmetric right PRISMS with same intrinsic volumes and distinct width/brightness distributions, and notes smooth strictly convex strengthening is open. Prisms are not smooth; equality after smoothing does not follow automatically since there are three exact intrinsic-volume constraints. The explicit harmonic pair here addresses the smooth WIDTH half, not simultaneous brightness. No previously covering smooth construction identified.

## value

PASS

Smooth versus polyhedral identifiability of width from all 3D intrinsic volumes is a concrete open regularity obstruction; exact matched smooth support perturbations with higher-moment separation provide a substantial partial resolution, not merely a normalization exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
