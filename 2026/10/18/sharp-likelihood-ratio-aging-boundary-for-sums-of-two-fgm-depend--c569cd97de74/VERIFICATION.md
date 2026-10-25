---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Differentiation and convolution of FGM survival copula give f=e^-s(s+theta[s-4+4(s+1)e^-s]). The log-curvature numerator is a quadratic in dependence theta. For negative theta, writing g as a convex combination of g_0 and g_- makes self-terms and mixed curvature strictly negative. For positive theta, set t=(1-theta)/theta; curvature sign equals sign(D(s)+t C(s)-t^2), C(s)<0 for all s. Existence of bounded nonempty D>0 domain follows limits D(0+)=-4, D(infinity)=-4 and a rational exponential bound at s=3/2; continuity yields the exact finite maximum and sharp iff threshold including equality. Independent symbolic differentiation verified all coefficients; bounded numerical optimize reproduced theta_c≈0.860258273097455 (not certified enclosure) and D(1.5)>0.

## originality

PASS

Best-of-knowledge statement/implication comparison against primary literature and Resultary; the genuinely distinct mathematical increment survives. Specific inaccessible full texts and historical-priority risks are recorded rather than counted as proof of novelty.

## value

PASS

Resolves sharp separation of density ILR versus hazard IFR aging in the exact classical dependent two-exponential model. Prior primary literature mistakenly infers ILR for theta=1 from a plotted log-density, while precise curvature produces counterexample and universal threshold. Mathematically substantive correction with lifetime-model interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
