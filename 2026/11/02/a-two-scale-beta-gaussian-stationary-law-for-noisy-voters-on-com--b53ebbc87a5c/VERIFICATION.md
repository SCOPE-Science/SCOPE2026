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

PASS: Exact stationary pair-generator equations for distinct A/A and B/B vertices yield x_A=x_B=x=z/(1+θ); cross-pair copying one endpoint contributes 1/a+1/b=h and all other copied spins contribute (2-h)x, giving x=h/(h+2θ(2+θ)), z=(1+θ)x, and E(P_A-P_B)^2=θz/2. I independently substituted rational parameters (a,b,θ)=(3,4,1/5),(5,8,1/20),(100,200,3/400) to verify z>x and both variance expressions, not from the source checker. The exact lumped chain drift is LU=θ(1/2-U), LV=-(2+θ)V with Γ(U)=h(Q+θ/2)/4, Γ(V/sqrt h)=Q+θ/2. On θ/h->λ/2, stationary moment recursion for U identifies Beta(λ,λ) via compact Hausdorff moments. O(sqrt h) jump and mixed remainders uniformly hold without a/b ratio restriction, and the conditional characteristic-function equation 2ψ'_p+t p(1-p)ψ_p=0 uniquely gives W|P=p Gaussian of variance p(1-p)/2. Beta integrals give Var W=λ/[4(2λ+1)] and strictly positive excess kurtosis 3/[λ(2λ+3)]. Finite rational checks do not prove the diffusion limit; the source stationary generator calculation supplies it.

## originality

PASS

Generic noisy-voter Gaussian/Bernoulli limits and complete-graph beta regimes are known; Mori et al use a distinct multi-node social-influence diffusion with approximated Gaussian cross-node correlation. The exact K_{a,b} finite pair correlation and ANY-ratio critical Beta-mixed conditional Gaussian disagreement is not supplied by these published primary statements. Best-of-knowledge PASS, with multiscale general-theorem risk.

## value

PASS

PASS: The joint stationary limit resolves how noisy voters on unbalanced complete bipartite graphs split into a slow Beta consensus and a fast conditional Gaussian disagreement, without assuming a/b approaches a constant. Its explicit non-Gaussian kurtosis and counterintuitive cross-greater-than-within correlation are natural stochastic-network invariants useful to future comparison and inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
