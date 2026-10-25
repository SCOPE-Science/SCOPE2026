---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Each stationary scalar LQR plant term is J=(q+kᵀRk)g(a+bᵀk), g=(1−y²)⁻¹. Directional Hessian D²J=2z g+4u g′h+Q g″h², where u²≤zQ. Completing square yields D²J≥z(2g−4g′²/g″)=2z/(1+3y²)≥z/2. Summing gives Hess F≥Rbar/2 throughout convex joint stability slabs. Coercivity and blowup at finite stability boundaries ensure a unique interior minimum and PL inequality; explicit q_y=(1−y)^4, a_y=y(3+y²)/(1+3y²), k_y=y−a_y give Hess→1/2 from above, so sharp. Independent symbolic simplification and 400 random directional checks corroborate formulas; proof handles all dimensions of k but only scalar state.

## originality

PASS

Best-of-knowledge mathematical priority assessment: the primary work is credited for model, antecedent formulas and context; the stronger exact theorem is not shown to be explicitly stated or automatically implied by the read material. Inaccessible full texts and older equivalent formulations are recorded explicitly rather than turned into categorical exclusions. In absence of a full manuscript, cannot assert no hidden proof of this implication; on available evidence explicit data-independent sharp factor not established. A standard rational-function square completion is an ingredient, not automatically a cited applied classification.

## value

PASS

Domain-randomized LQR landscape analyses currently often impose similarity or PL assumptions. A heterogeneity-independent explicit Hessian modulus for an arbitrary finite mixture of scalar-state plants with multi-input shared feedback, plus exact sharpness and unique optimality, is a reusable rigorous benchmark for policy optimization rather than a textbook restatement of individual scalar feedback formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
