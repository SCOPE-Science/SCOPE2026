---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed marked Poisson point process after jump transform r=Gamma^(-1/alpha): direction-j mass tail w_n yields independent positive-alpha-stable R_n with Laplace exp(-w_n Gamma(1-alpha)t^alpha). For q in (0,alpha), E R_n^q=K w_n^(q/alpha), and geometric w_n<=C rho^n plus Markov and Borel-Cantelli gives almost-sure exponentially small R_n. For generic normals the support sum is unique; truncations take at most 2 sum_{k=0}^{d-1} binom(n-1,k) finite hyperplane chambers, and the finite CLOSED-ball covering passes to closure of exposed points and hence all extreme points by Straszewicz. Thus N_r<=C(1+log 1/r)^(d-1). Dense positive-mass directions ensure d-dimensional interior and injectivity of the exposed-point support map on a continuum of generic normals. Quantifiers, samplewise constants and all d>=2,0<alpha<1 checked; no finite approximation used as infinite proof.

## originality

PASS

The complete 2019 original study already covers finite directional support and planar universal Hausdorff bounds, and the 2026 Kukushkin abstract covers positive dimension for uniform diffuse directions. Neither gives the contrast of FULL TOPOLOGICAL SUPPORT with infinitely many dense atoms, continuum-many exposed points and zero upper-box/packing dimensions plus polylogarithmic entropy in every d. The 2025 universal upper bound alpha+d-2 is weaker. Actual Resultary semantic search mostly returned this same current record and unrelated geometric records; self-hit is not independent priority evidence. Full 2025/2026 same-object manuscripts not obtained; conditional best-of-knowledge originality with explicit access risk.

## value

PASS

Addresses a specific spectral-distribution dependence explicitly left open by the 2019 article: full topological support is insufficient to force positive extreme-point dimension, and the contrast with the positive uniform-direction dimension is mathematically sharp at the level of support regularity. Quantitative polylog entropy, all-dimensional argument and continuum exposed points distinguish this from the trivial finite-support polygon example. Useful boundary example for random convex geometry and anisotropic stable laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
