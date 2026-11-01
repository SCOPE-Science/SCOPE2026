---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The Fock monomial basis e_j=(pi^j/j!)^1/2*z^j diagonalizes the disk localization operator with lambda_j=integral_0^s t^j e^-t/j!dt and gap lambda_j-lambda_{j+1}=p_{j+1}>0. Moving radial boundary s+epsilon*h(theta) is twice trace-norm differentiable for s>0. Direct differentiations give M_jk_prime=sqrt(p_j p_k) hhat_{k-j} and M_jj_double=p_j(j/s-1)*mean(h^2). Isolated-cluster eigenvalue perturbation cancels internal-block terms; cross-gap terms sum with denominators sum_{r=j+1}^{j+m}p_r. Telescoping sum_{j<N}p_j(j/s-1)=-p_{N-1}, and Parseval for real mean-zero h, yield exactly sum_{m>=1}kappa_{N,m}|hhat_m|^2 deficit. m=1 cancels, m=2 gives positive p_{N-1}(N+2s+1)/[(N+s)(N+s+1)] including N=1; high m limit p_{N-1}. Abreu global inequality forces nonnegativity, not the actual formula. Independent Fraction checks of 21 (N,s) pairs validate these exact identities; smooth fixed-parameter perturbation proof is essential.

## originality

PASS

Exact area-preserving angular Hessian and closed elliptic coefficient for arbitrary Ky Fan rank differ from global disk optimality, radial rearrangement and first-eigenvalue stability. The observed Fourier multiplier family depends jointly on rank, Poisson weight and boundary-crossing spectral gap.

## value

PASS

Disk Ky Fan maximization is a natural sharp time-frequency inequality; the exact angular Hessian supplies all local curvature multipliers and a strictly positive elliptic cost for every fixed rank and area. This is an independently useful rank-dependent local invariant beyond a sign assertion or textbook eigenvalue formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
