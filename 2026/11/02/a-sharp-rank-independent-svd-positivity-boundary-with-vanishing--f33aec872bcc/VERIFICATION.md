---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For real α,β>0 and n≥3, A=αI+βuuᵀ, u=1/√n, the entire Frobenius-best rank-r set for 2≤r≤n−1 is (α+β)uuᵀ+αP for rank-(r−1) orthoprojectors P on u⊥. From 0≤P≤I, P_ij≥−1/2 for i≠j and P_ii≥0. Rank-(r−1) projector vvᵀ+R_S with v=(e1−e2)/√2 attains P_12=−1/2 for every r. Thus min across all entries and minimizers equals (α+β)/n−α/2, giving β≥(n−2)α/2 iff all minimizers are nonnegative. Group partition projector Q=ZD⁻¹Zᵀ yields strictly positive nonnegative-factorizable C=αQ+βuuᵀ with exact unconstrained error α√(n−r), for every r=1..n. In strict subthreshold region Aε=A+εP stays entrywise positive for 0<ε≤β/n, has unique truncation with (1,2)=−δ−ε/2 and optimum α√(n−r), while the closed feasible rank-r nonnegative set has strictly larger minimum and the NNF infimum excess is ≤ε√(r−1). Independently verified projector identities, all intermediate ranks n=3..7 with exact SymPy arithmetic, perturbation spectral separation, and the exact n=3 witness. Infinite-n claims come from algebra, not finite experiments.

## originality

PASS

Qualified PASS for the combined sharp all-optimal-SVD sign threshold, its rank independence, existence of positive nonnegative-factorizable exact optimum and robust vanishing-penalty unique-negative-SVD perturbation. Eckart–Young and projector geometry are standard; consulted low-rank NMF and singular-value perturbation primary literature studies general algorithms and sufficient nonnegativity preservation, not the exact compound-symmetric envelope.

## value

PASS

The sign of a truncated SVD and the true cost of a nonnegative low-rank constraint differ sharply, even under arbitrarily small perturbations removing the spectral tie. The rank-independent threshold and vanishing-penalty separation are a natural exact benchmark for nonnegative low-rank approximation, not merely reapplication of Eckart–Young.

The dated certificate retains the supplied scientific assessment, sources and limitations.
