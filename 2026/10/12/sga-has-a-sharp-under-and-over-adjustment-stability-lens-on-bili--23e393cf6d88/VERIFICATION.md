---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

With J skew symmetric, the actual source SGA adjusted field is (I−τJ)Jz. Singular-vector orthogonal coordinates split the Euler matrix into (1−ητσ²)I−ησR with R²=−I, whose exact squared norm factor is (1−ητσ²)²+η²σ². Solving r²<1 gives η<2τ/(1+τ²σ²), tightest at σ=L; equality has norm-one top block, above expands, establishing both directions. Let s=ηL and u=τL; the sharp inequality s(1+u²)<2u has maximum allowed s=1 at u=1 and adjustment window u±=(1±sqrt(1−s²))/s, product 1. Comparison of exact ceiling with Vater et al general sufficient step τμ²/((1+τ²L²)L²) yields 2(L/μ)². Original independent rational modal/block checks corroborate algebra, not substitute for it.

## originality

PASS

Balduzzi/Letcher/Gemp introduced Hamiltonian gradient correction and its radial effect on bilinear games; Vater–Foglia–Colao–Borzì give a sufficient general quadratic-game step bound. Their inspected result does not state the necessary-and-sufficient full-spectrum discrete step threshold or fixed-step reciprocal overadjustment window. The novelty is not the SGA algorithm or its skew decomposition but a sharp optimization-parameter boundary; the familiar spectral-calculus derivation is acknowledged.

## value

PASS

The exact threshold gives an actionable answer to whether increasing adjustment always helps and quantifies both under- and overadjustment; its comparison shows a sufficient general theorem loses a condition-number-squared factor on a canonical test class. These boundaries matter for explicit numerical algorithm stability and clarify an otherwise misleading tuning tradeoff, even though the proof is short linear algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
