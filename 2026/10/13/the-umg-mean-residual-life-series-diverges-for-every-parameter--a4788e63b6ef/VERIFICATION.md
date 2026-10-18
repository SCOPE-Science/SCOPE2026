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

Checked S_X(u)=(1+θu+θ²u²/(2(1+θ)))exp(−θu), ξ=y/(1−y), and the UMg MRL integral ∫_ξ^∞ S_X(u)/(1+u)^2 du. Expanding (1+u)^−2=Σ(k+1)(−1)^k u^k outside |u|<1 gives the source Eq. (3.5), whose incomplete-gamma k-term has positive Γ(k+3,θξ) contribution. Bounding this gamma integral below on [k+2,k+3] proves magnitude→∞ at every θ>0, 0<y<1. Polynomial division and three elementary exponential integrals yield the displayed E1 formula: exp(−θξ)[θ+(2−θ²)(1−y)]/[2(1+θ)]+θ³exp(θ)E1(θ/(1−y))/[2(1+θ)]. Independent symbolic differentiation checks the antiderivative and quadrature agrees; finite term values only illustrate the all-parameter term-test proof.

## originality

PASS

Ruidas et al. Eq. (3.5) directly claims an analytic series for the unit-transformed Mgamma MRL. Earlier parent-distribution MRL is a different integral without the (1+u)^−2 factor, so it does not correct the erroneous unit series. No model-specific E1 replacement or all-parameter term-test theorem was found in inspected original source.

## value

PASS

Every admissible parameter in the proposed UMg reliability model is affected: its printed mean-residual-life evaluation series diverges and cannot be numerically used. The globally valid E1 expression computes the corrected MRL exactly, a nontrivial source-specific practical correction to a standard reliability invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
