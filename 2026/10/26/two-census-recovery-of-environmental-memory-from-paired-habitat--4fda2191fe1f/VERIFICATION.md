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

For environmental S_t∈{±1} with E S_t S_{t+h}=ρ^h, conditional patch means p+M_t satisfy M_t=λ M_{t−1}+(1−λ)aS_t. Conditional independence yields C0=a²(1−λ)(1+λρ)/((1+λ)(1−λρ))>0, C1/C0=(λ+ρ)/(1+λρ), and A1−C1=λ[p(1−p)−C0]. The bracket is E Var(X|entire S)>0 since 0<p−a<p+a<1; all inversion denominators therefore nonzero for specified λ∈[0,1), ρ∈(−1,1). This proves p=m and unique global reconstruction of λ,ρ,a. Independently exact-rational solved the stationary eight-state environment-and-patch Markov transition law in three cases and verified moments; the two distinct one-date models (a,λ,ρ)=(1/5,1/2,−2/7), (1/10,0,0) both give p=1/2, C0=1/100 and identical complete one-date two-bit law. Thus two dates are necessary and sufficient for two patches.

## originality

PASS

A simple exact algebraic inversion for two site observations under one shared temporally correlated hidden binary Markov environment was not found in inspected Moran-effect occupancy/detection or stochastic-factor work. More general dynamic latent-factor identifiability results may imply the formulas as a special case; this is retained as a material originality risk rather than declared disproved.

## value

PASS

Sharp minimal temporal sampling for a natural shared-environment binary occupancy model, with explicit exact recovery of environmental persistence separately from local retention and constructive one-date nonidentifiability. This is a meaningful structural identification result for ecology and time-series observation design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
