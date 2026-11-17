---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The two opinion-count birth–death rates give exactly LZ=ε(1/2−Z), L(X−Y)=−(2−ε)(X−Y), Γ(Z)=s[ε/2+(1−ε)(x+y−2xy)]/4. Dynkin’s Ld² equation makes fast disagreement negligible in integrated rescaled drift, with jumps ≤1/(2 min(a,b)), so the martingale problem converges to Gf=λ(1/2−z)f′+z(1−z)f″/4 with absorbing λ=0 boundary. Stationary cross-spin W=c s/[2(1−c²)+c²s], same-part cW and Var(Z)=[s+(2+2c−cs)W]/16 follow by pair generator; λ>0 invariant Jacobi diffusion has Beta(2λ,2λ), while variance gives λ=0/infinity endpoints. Inspected verify.py exact rational finite-state checker; independently substituted (a,b,ε)=(1,1,1/3),(2,3,1/3),(4,6,1/3), producing positive variance and cross-covariance consistent with formula. Finite checks do not prove the process limit.

## originality

PASS

The stationary common Beta law and stationary finite correlation equations are already in a stronger October/November published two-scale Beta–Gaussian study after rate conversion θ=ε/(1−ε). The new independently surviving theorem is path-space Wright–Fisher convergence from arbitrary initial densities under a_n,b_n→∞ with unrestricted imbalance, including instantaneous synchronization. Earlier published Resultary source proves only stationary joint limit, not dynamic path convergence; general noisy-voter and unnoised-density literature may reduce this novelty and is a residual risk.

## value

PASS

The arbitrary-part-size-ratio fast/slow synchronization principle and critical dynamic diffusion on a natural dense bipartite graph complement the known stationary Beta–Gaussian law. It distinguishes genuinely asynchronous common noise from synchronous independent shores, clarifies time scaling and boundaries; a nontrivial process theorem remains beyond a cosmetic reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
