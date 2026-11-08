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

For independently sampled coordinates with fixed positive steps, the exact scalar recursion is v_{t+1,i}=(1-p_i s_i(2-s_i)) v_{t,i}+p_i s_i^2 σ_i²/λ_i², where s_i=λ_iη_i. It yields stationary loss Σ w_i s_i/(2-s_i), w_i=σ_i²/(2λ_i), and sharp mean-square transient factor max_i(1-p_i s_i(2-s_i)), attained by a single-coordinate perturbation. Feasible prescribed deficit τ is exactly 0<τ<=1/d. Since loss rises in s_i, each feasible optimal step saturates p_i s_i(2-s_i)=τ on its small-step branch. The reduced probability objective is strictly convex, with derivative -w_iτ/[p_i²u_i(1+u_i)²], u_i=sqrt(1-τ/p_i), tending to -infinity at p_i=τ. Thus the unique interior KKT scalar k solves w_i(1-u_i)^2/u_i=k and Σ_i τ/(1-u_i²)=1; its monotonicity gives unique solution. Compactness and Cauchy–Schwarz prove slow-rate square-root weights, while uniform boundary-layer expansion gives fast-rate squared-weight excess. The τ=1/d endpoint uniquely forces p_i=1/d,s_i=1; τ>1/d is impossible. Independent scipy bounded minimization for d=2, λ=(1,1), σ=(1,3), τ=0.1 gave p1≈0.27777903565, stationary loss≈0.22314303956, matching claimed scalar optimum. Numerical check is not the general uniqueness proof.

## originality

PASS

Known random-coordinate methods optimize deterministic complexity or analyze noise with fixed/uniform sampling. Their separate conclusions do not give the joint noise-floor/rate Pareto frontier or its two endpoint laws. Primary comparison includes an older full paper on optimal sampling, not just abstract titles; equivalent general optimization may exist in noise-aware stochastic coordinate design.

## value

PASS

Selecting sampling probabilities and coordinate-specific steps jointly under an exact convergence-rate constraint is a natural noise-versus-speed Pareto design problem. The closed scalar solution and different square-root and squared-noise endpoint allocations give robust quantitative guidance and a nontrivial qualitative boundary-layer transition. No convergence claims outside diagonal quadratics or independent persistent finite-variance noise are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
