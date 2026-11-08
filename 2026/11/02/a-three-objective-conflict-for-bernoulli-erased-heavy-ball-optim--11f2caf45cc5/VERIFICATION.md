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

PASS. For iid Bernoulli p, A_n=[[1+β−γB_n/p,−β],[1,0]], the deterministic mean is a=1+β−γ and Var(a_n)=γ²(1−p)/p. Recomputed E[AᵀPA]−P=−D diag(1,0) for P=[[1,−βa/(1+β)],[-βa/(1+β),β²]] and D=2γ(1−β)−γ²[(1−β)/(1+β)+(1−p)/p]. For β>0, D>0 gives P positive definite and 2-step observability yields geometric mean-square decay; at D=0 P-energy conserved and at D<0 forced stationary variance would give D m=σ²>0 contradiction. At β=0 exact scalar factor 1−D. Derivatives of Γ_p(β)=2p(1−β²)/(1+β−2pβ) and D at fixed γ yield the threshold p=1/2, β_capacity=(sqrt p−sqrt(1−p))/(sqrt p+sqrt(1−p)) when p>1/2, and β_noise=0 for γ≤1, sqrtγ−1 otherwise. For zero velocity X_-1=X_0, event all n gradients erased has probability (1−p)^n and final X_n=X_0; path patterns with final hit then hit/erasure prove equality at n≥2 forces γ=p,β=0. Exact independent finite-path rational enumeration and symbolic matrix identity agreed. σ² is per-update noise, not gradient variance.

## originality

PASS

PASS at best knowledge for the combined three-objective exact classification, not for the general linear-two-step stability method, additive-noise Lyapunov equations or qualitative observations that stochastic momentum need not accelerate.

## value

PASS

PASS. On one natural stochastic heavy-ball benchmark, exact stability capacity, stationary additive-update-noise minimization and finite-horizon performance select genuinely different algorithm parameters. The strong all-horizon no-acceleration optimum is motivated by gradient dropout rather than an arbitrary normalized statistic and exposes a practical distinction between stable step capacity and best time-horizon error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
