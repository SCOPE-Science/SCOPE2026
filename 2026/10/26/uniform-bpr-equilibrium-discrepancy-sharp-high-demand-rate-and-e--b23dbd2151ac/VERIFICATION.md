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

The Beckmann objective is strictly convex in loads on the same compact convex load polytope. Adding the two minimizer inequalities with their displayed signs and using (u^p-v^p)(u-v)>=|u-v|^(p+1) for u,v>=0 gives the uniform bound by Hölder, also when the difference vanishes. Homogeneity follows by scaling flows. Every resource available to an active singleton commodity has positive limiting homogeneous load, since an unused resource would beat any used resource in that commodity's menu. After rescaling, t>=2C/eta keeps both load vectors on those coordinates above eta/2, and the scalar derivative lower bound yields the claimed Euclidean constant and factor t^(1-p). The two-link binomial equation gives the stated nonzero leading coefficient, including a constant difference for p=1 and the stated cubic for p=4. In the stability proof the base complementarity constraints by themselves allow slack multipliers for zero-demand commodities. For the pair being projected, however, c_s=lambda_h together with all c_{s'}>=lambda_h forces precisely the minimum condition; conversely one may choose the minimum for every multiplier. Thus the projected integer-power semialgebraic set is exact even at zero demand, and its finite union of points and intervals is eventually constant. No path-flow uniqueness or multidimensional boundary asymptote is inferred. The supplied SciPy script was inspected, not executed; the all-demand results follow analytically, not from the bounded test grid.

## originality

PASS

The reviewed package concerns an explicit additive all-demand load comparison between two games at the same demand, its sharp fixed-ray singleton exponent, and eventual stability of the entire set of cost-minimizing strategies on each ray. Credit the classical potential, monotonicity, strong-convexity and projection tools, and the affine breakpoint and existing cost-class results. The strongest inspected statements use different perturbations or give narrower regime claims; no verified broader result was found that supplies this package. Status is bounded by the identified sources, not a priority certification.

## value

PASS

The common-power benchmark yields a topology-independent absolute error at every demand. The result also identifies when high demand produces much smaller absolute error and shows the exponent cannot be strengthened, while separating tie-set stability from the stronger boundary-geometry conjecture. These are concrete load and regime predictions, not merely a reformulation of convex optimality or a fixed-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
