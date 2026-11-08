---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The derivative of a single logistic component is f_θ'(p)=[1+(1-p)exp(p-θ)]/(1+exp(p-θ))², bounded absolutely by 1+p/4 independent of θ on fixed witness prices; tends to 1 as θ→infinity at fixed p and is eventually strictly negative for any fixed θ. Inductively keep signs at previous 2m witness prices by adding sufficiently small ε>0; choose u>last negative witness where prior derivative lies in (-ε/4,0), and a sufficiently large new θ>u so new component derivative at u exceeds 1/2, while at θ+1 both old and new derivatives are negative. Appends a disjoint positive-to-negative interval. Each such interval contains an interior strict maximum: real-analytic nonconstant function has isolated stationary zeros, hence no flat interval; negative-to-positive gaps similarly give strict minima. Positive scaling yields unit total shares; open strict signs imply relatively open parameter region. Independent rational enclosure checked explicit valuation/weight prefixes m=1..4 at all 2m windows, finite corroboration only. No upper bound on maximum count or comparative global maximum is claimed.

## originality

PASS

Published Li/Webster/Mason/Kempf show loss of one-product revenue quasiconcavity even at a common price coefficient for two segments. Van de Geer/den Boer 2022 full author-hosted paper finds local optima and a global approximation scheme with exponential dependence on segment count. Its inspected introduction/methods/algorithm do not entail ≥m separated strict local maxima for *each* m in the one-product same-slope model. The constructive sign-preserving induction adds an additional strict mode at each segment.

## value

PASS

Establishes arbitrarily high univariate multimodality solely from market heterogeneity in a canonical common-price-coefficient logit model. Exact open-set robustness separates a structural counterexample from fragile isolated parametric coincidences; informs nonconcave global-pricing analysis, with explicit restriction to population expected revenue and no complexity lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
