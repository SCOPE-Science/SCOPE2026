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

For a fixed L and sup-rate bound M, integrate the cohort equation from birth and bound |η₀−c|≤η₀+κ. Grönwall bounds every cohort wealth path in absolute value by B=(|w₀|+L(η₀+κ))e^{ML}, and its a.e. derivative in absolute value by MB+η₀+κ. The birth-index integrand ρ(t−b)E[w_t^b] can be extended by zero outside b≤t≤b+L, with no jump because ρ vanishes at both endpoints. Its weak time derivative on the life interval is the product-rule sum; Fubini and the bounds permit integration in b, including for merely measurable bounded consumption. The derivative of aggregate wealth thus has essential-supremum bound B∫|ρ′|+MB+η₀+κ=3B/L+MB+η₀+κ. At equilibrium with a C¹ target the bound holds pointwise by continuity. Every sinusoid in the stated family has the same upper/lower range bounds and derivative norm ω/2, which can exceed that bound even on any fixed interval of positive length with a suitable phase. The v2 source hypotheses allow constant wealth at birth and deterministic constant income; Assumption 2.8 and optimal consumption (2.19) provide the cap, and (5.8)–(5.10) give the stationary density class on the moving support. The zero extension of the quadratic density is Lipschitz, not globally C¹; if global C¹ across both edges is imposed, the same proof applies to the normalized quartic density 30a²(L−a)²/L⁵ with derivative L¹ norm 15/(4L). The displayed bound is for the frozen quadratic on its natural support. This is an analytic replay, not an existence proof or a numerical search.

## originality

PASS

The proof in the primary work already displays K-level dependence for constant K; do not credit a generic observation of omitted K from the theorem's constants as new. The supported distinct result is the explicit derivative-based obstruction to uniformity across time-varying profiles, including uniformly bounded and uniformly positive profiles of identical range.

## value

PASS

The counterexample isolates a meaningful missing uniformity hypothesis in an equilibrium theorem: bounding the range of an exogenous capital supply cannot control the cohort aggregate's attainable time variation. The explicit primitive-dependent derivative ceiling identifies the kind of profile control needed, or why the constants must be permitted to depend on more than levels. This is a concrete use of an elementary estimate against a consequential quantifier, not presented as a new differential inequality method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
