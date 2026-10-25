---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

At every binary level, fair sum/min gives P(root>0)=r exactly, since (2r-r²+r²)/2=r. Conditioning on positivity gives μ_{m+1}=(1−r)μ_m+(r/2)(μ_m*μ_m+Min₂ μ_m)=μ_m+r(μ_m*μ_m−Max₂ μ_m)/2. Independent coupling gives 2-Lipschitz ℓ¹ vector field and ||Φ||₁≤1, hence global probability-simplex flow ν_t and Euler TV error ≤r(e^{2mr}−1)/4. Stochastic monotonicity of the update from δ₁, explicit U₁(t)=2/(t+2) and U_k′=[P(Y+Y′≤k)−U_k²]/2 force finite-set escape as t→∞. The comparison at m=⌊T/r_N⌋ proves the large-clock regime without falsely extending the finite-time error to unbounded times; TV δ₁ and ν_λ cover the other regimes. Exact check of original rational full/conditional update for finite depths was independently replayed, not used as universal proof.

## originality

PASS

The exact conditional Euler representation uses the known zero-mass conservation but yields a three-regime conditional limit not established by the inspected prior recursive-tree papers; generic Banach-valued ODE Euler theory supplies a method, not an automatic determination of the model-specific vector field and t=Nr threshold.

## value

PASS

The Bernoulli-positive-leaf endpoint is a natural unresolved density regime of the fair critical min-plus recursion. The dimensionless depth×density clock yields a nontrivial infinite-state conditional kinetic evolution with sharp total-variation finite-clock control and a complete fixed-finite-set escape classification, not a routine isolated probability evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
