---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: Minimizing the exact truncated affine loss plus quadratic regularizer and proximal term gives two continuous affine branches separated by the kink x=(1+x)/2, with threshold c=[α(2−λ)−1]/[α(2+λ)−1]. On the invariant interval [0,1], the branch-order differences factor with positive denominators under 0<λ<1/3 and α>4/(1−3λ). Substitution gives x₀=(α+3)/D, x₁=(α+3+2αλ)/D, x₂=(α+3+3αλ)/D, D=α+3+4αλ; the strict itinerary x₀<x₁<c<x₂<1 and the three map identities prove a primitive period-three orbit. The return multiplier is (1−α)/[4(1+αλ)], so the stated attracting condition follows. The continuous interval map satisfies the hypotheses of Li–Yorke’s period-three theorem. The exact-rational checker inspects 64 rational parameter pairs and 10,112 finite minimizations; it is corroborative only, not the universal proof.

## originality

PASS

Best-of-knowledge comparison supports non-coverage by inspected sources; source-specific evidence, implications and residual risks are recorded below. This is not a certification of independent priority.

## value

PASS

PASS: This is a motivated structural boundary for a named proximal optimization method, not a routine linear convergence-rate calculation. The exact attracting nonoptimal period-three orbit persists on an open parameter region and invokes a genuine interval-dynamics theorem to establish all periods and a scrambled set. It shows why a large constant step cap can create dynamics outside the method’s small-step convergence regime; the restriction to one-dimensional quadratics and large caps is explicit. The same-method literature-access risk remains material but does not by itself make the fact worthless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
