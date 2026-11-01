---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For diffusion generator D∂xx+h∂x with rate-one reset at |x|>1 and D=αΓ^β, β>1, inspected the exact four-piece stationary Green-function density with Dk²+hk=1, Dℓ²−hℓ=1. Normalization and source jump are consistent with exterior resetting flux hC(1+r). Since D~αh^β on a low branch, δ=D/h→0, exponential e^{−1/δ}→0, and η=(h+√(h²+4D))/2→0. Interior density →1 on (0,1), total outside/negative mass O(h+δ), giving L1 uniform law and controlled polynomial moments. Continuity of Γ(D,h) yields small branch by sign-crossing near αh^β. Generator first moment and integrated interior density give for 1<β<2 mean correction −αh^{β−1}; β>2 +h/2; β=2 coefficient (1+√(1+4α)−4α)/4. At α=3/4, expansion of self-consistency c(h)=D/h²=3/4−9h/4+O(h²) gives exact +45h²/16. Independently numerically solved self-consistent branches in four regimes as h→0, including marginal ratio approaching 45/16, and independently checked rational expansion. Finite numbers corroborate but do not replace analytic small-parameter proof.

## originality

PASS

Bertin 2022 presents this exact resetting-rate-dependent diffusion model and D~α|h|^β branch but describes its weak-field mass as concentrated near the threshold. Examining the original explicit stationary resolvent and regeneration law gives a uniform interval profile instead, with additional α/β response crossover and marginal quadratic coefficient. General partial-reset or random-diffusivity models have different generators. The corrected uniform limit and exact coefficients are assessed additions beyond model premises, not claiming discovery of Bertin dynamics.

## value

PASS

Corrects a materially different weak-field physical conclusion (point localization vs uniform traversal occupation), and determines sharp response sign changes at β=2 and α=3/4 with a nontrivial marginal quadratic term. These directly matter for interpreting the self-consistent transition in the original physical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
