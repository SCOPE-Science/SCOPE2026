---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Two-sided stochastic convolution conditionally Gaussian with V=2D∫_0^∞e^-2κt c^(2N_t)dt, 0<V<v*=D/κ, and synchronous contraction ensures unique invariant law. At latest Poisson age E, W=v*-V satisfies W=U(v*-c²V'), U=e^-2κE~Beta(θ,1), θ=rate/(2κ). Since v*(1-c²)≤v*-c²V'≤v*, exact P(W≤w)=Cw^θ for 0<w≤v*(1-c²). Stationary generator gives moments m_k=∏_{j≤k}2κj/[2κj+rate(1-c^(2j))], so C has convergent binomial series. Boundary Laplace integration of the Gaussian mixture gives density x^-2θ exp(-x²/2v*) with the specified Γ constant and right survival an additional v*/x. Critical E exp[X²/(2v*)] finite iff θ>1/2, i.e., rate>κ.

## originality

PASS

Best-of-knowledge PASS for *exact fixed-reset* OU invariant variance endpoint distribution, sharp Gaussian polynomial correction and critical square-exponential moment. Recent weak-reset approximation deliberately modifies tails; driftless partial-reset conditioned results do not supply unconditional OU stationary law.

## value

PASS

Sharp rare-event tails and moment integrability are natural quantities in reset diffusions, and the explicit disparity from the power-tailed weak-reset SDE is mathematically meaningful and relevant to approximation validity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
