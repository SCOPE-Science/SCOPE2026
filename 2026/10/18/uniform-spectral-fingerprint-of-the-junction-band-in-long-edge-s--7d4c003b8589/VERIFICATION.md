---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For λ>2 the Dirichlet path transfer has no poles, and its two endpoint-to-first-interior coefficients are U_(ℓ−2)/U_(ℓ−1) and 1/U_(ℓ−1), evaluated at λ/2. Inserting them at each degree-d junction gives the stated scalar map on the exact parent eigenspaces with equal multiplicities; an eigenvector vanishing on all junctions is zero. After λ=u+1/u, the transformed equation in RESULT.md lines 60–66 has derivative 2ρ+O_d(ℓρ^(−ℓ)) on |u−ρ|≤C_dρ^(−ℓ). The term −μ(u²−1)u^(−ℓ) is uniformly bounded for μ∈[−d,d], and choosing C_d sufficiently large brackets its perturbation of the simple root. Taylor expansion yields shift μ(d−2)ρ^(−ℓ)/(2ρ)+O_d(ℓρ^(−2ℓ)); multiplying by the derivative 1−ρ^(−2) gives the claimed c_d. Interlacing at the Dirichlet principal block gives at most n eigenvalues above 2, and the eigenspace extensions attain that count. Even for a non-spectral μ in the interval, the secular quotient λ−(dU_(ℓ−2)+μ)/U_(ℓ−1) is strictly increasing: the rational term is a nonnegative combination with weights (d±μ)/2 of the symmetric and antisymmetric endpoint resolvent forms, each nonincreasing above 2. This also rules out additional scalar roots for the continuum extension. The implicit μ derivative is positive, so the width is the difference of the two endpoint eigenvalues; μ_min=−d iff the connected parent is bipartite. All constants use only d and neither the maximum multiplicity nor parent order. The frozen verify.py, requirements and VERIFICATION.md document finite checks, inspected rather than executed. The proof is for the above-2 band, not the entire enlarged spectrum.

## originality

PASS

Credit the known junction energy, outside-band count in the fixed-parent asymptotic regime, exponential scale and elementary subdivision reduction. The distinct claim supported by the bounded search is the degree-only uniform, parent-resolved first-order splitting of the full junction band, including the graph-dependent sharp width. Neither the closest primary subdivision theorem nor the inspected inflation formulas have this information. The residual risk is earlier exact decimation or asymptotic perturbation coverage that the search did not locate.

## value

PASS

The common limiting junction energy loses all information about the parent spectrum. Resolving the first-order band with control independent of network order restores every parent eigenvalue at a specified resolution, and distinguishes bipartite and nonbipartite parents by the sharp degree-controlled bandwidth. Uniformity is useful when varying topology and size at fixed degree, beyond merely recalculating a junction energy or a single finite graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
