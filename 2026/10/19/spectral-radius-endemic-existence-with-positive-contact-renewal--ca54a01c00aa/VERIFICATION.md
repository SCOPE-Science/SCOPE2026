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

For every permitted edge, the stationary quotient is positive and continuous on the compact box K=∏[0,bᵢ/(δᵢ+bᵢ)], which excludes saturation and itself contains any stationary prevalence in the state cube. Substitution gives a continuous map T:K→K. Continuity of the quotient, multiplied by prevalence, gives T(y)=D⁻¹My+o(‖y‖₁) from within K without response differentiability. A positive left Perron vector turns the strict spectral inequality into uniform weighted outward expansion near zero. Perturbing by a convex mixture with a fixed positive point yields Brouwer fixed points bounded away from zero for small perturbations; compactness and continuity give a nonzero fixed point of T. A zero coordinate would force all incoming neighbors to vanish and hence the whole vector by strong connectivity. This guarantees 0<yᵢ<1 and 0<zᵢⱼ≤1 on permitted edges, not zᵢⱼ<1. Independent exact substitution in the two-node witness gave the claimed stationary derivatives, ρ=√12 and minimum sum 2/7.

## originality

PASS

The inspected original model paper states the spectral condition as Conjecture 6 and proves a different minimum-sum condition in Theorem 5. The supported contribution is the spectral implication for strictly positive creation on nonsaturated inputs, allowing failure of stationary link elimination at a saturated input and not requiring monotone responses. The strongest inspected indexed matches have genuine theorem overlap but are later-dated and impose extra closed-cube positivity conditions; neither demonstrates earlier or coextensive coverage of this finding.

## value

PASS

The result answers an explicit model-specific spectral-threshold question in a natural positive-renewal regime. It handles strongly heterogeneous networks missed by the minimum-sum test, without imposing response monotonicity or regularity beyond continuity. The distinction between a nonsaturated compact box and the full state cube also avoids an unnecessary boundary assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
