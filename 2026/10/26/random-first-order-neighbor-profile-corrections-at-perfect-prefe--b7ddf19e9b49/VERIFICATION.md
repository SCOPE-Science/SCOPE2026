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

At exact off-origin relocation probability one, only the origin and m=2d neighbors are visited. With K=n+1, b_n=1-(1-xi0)*J_n and C_n=#origin visits, q0=b_n*C_n/K and qj=b_n*N_j/K+(1-xi0)*J_n/m. f=C/K is nonnegative supermartingale tending 0. Log C drift/variance yield C_n>=K^eta and then log C/log K->1. For Q=K/C, E Delta Q=(1-xi0)*J_n/C_n+summable remainder and conditional variances summable after C_n>=K^3/4, proving C_n log K/K->1/(1-xi0). D_j=N_j-(K-C)/m and R_j=D_j/C have E Delta R=b_n*R/[K(C+1)] and summable drift/variance, hence finite R_j,infty almost surely. Conditional on autonomous binary origin path, the first new neighbor U is uniform, and positive convergent random multipliers of the neighbor-label martingale give nondegenerate conditional means; sum_j R_j=0. Independent rational checks tested q and drift identity across many finite count vectors and xi0 choices, not the a.s. limit.

## originality

PASS

Armfield–Mailler 2026 prove occupation localization for off-origin parameter xi<1 in an open neighborhood below the perfect endpoint, not at xi=1 or with random order-1/log n directional corrections. Boyer et al. predict the leading equal-neighbor profile but not this random first-order pathwise effect. Full Armfield thesis was inaccessible, so possible prior endpoint development is a concrete priority risk, not ignored or automatic failure.

## value

PASS

At the natural singular perfect-resetting boundary, the first-order logarithmic correction is genuinely random and distinct from deterministic origin-mass loss. Its precise pathwise normalization and nondegeneracy refine the established leading occupation profile in a way useful for fluctuations of memory walks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
