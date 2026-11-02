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

For any tree n≥3 with hub cone, grounded Laplacian M=diag(a)+∑x_e(e_u−e_v)(e_u−e_v)^T and det M equals the weighted spanning-tree count. The weight-to-M map is injective on a tree; logdet is strictly concave and KKT is globally sufficient. Tree distance correlation Cρ(u,v)=ρ^{dist_T(u,v)} is positive definite with determinant (1−ρ²)^(n−1) and inverse edge entry −ρ/(1−ρ²), diagonal [1+(d_v−1)ρ²]/(1−ρ²). Set ρ=1−t/2 for t≤2, M*=(B/n)Cρ^-1; comparing entries gives x=(B/n)ρ/(1−ρ²), a_v=(B/n)[1−(d_v−1)ρ]/(1+ρ), feasible iff t≥t0=2(Δ−2)/(Δ−1) for Δ≥3 (otherwise t0=0). KKT derivatives all n/B on spokes and tn/B on tree edges, yielding unique optimum and det=(B/n)^n[t(4−t)/4]^−(n−1). For t≥2 star-only is KKT-optimal. If t<t0 and all spokes positive, zero tree edge would have derivative 2n/B>tn/B, so all edges positive; Gaussian tree Markov forces Cρ and then negative spoke at degree Δ, contradiction. Independent 4-fold matrix/cost/inverse/determinant checks on 3 tree families of orders3..9 and feasible prices corroborated the argument.

## originality

PASS

Khosoussi et al. full 2016 original covers general maximum weighted spanning-tree network design and determinant submodularity, not this closed-form independently priced all-tree cone optimum. Malioutov et al. provide Gaussian Markov tree covariance, not optimal allocation. Earlier theta-network path/star subcases for equal prices are genuinely known and are not counted as novel. The arbitrary-tree degree threshold and topology-independent determinant appear not to be prior corollaries of inspected work; Cheng 1981 original inaccessible.

## value

PASS

A natural weighted spanning-tree reliability/design functional on arbitrary cones has a unique asymmetric-edge optimal allocation with explicit support phase boundary governed only by maximum tree degree, and a shape-independent optimum in an entire cost regime. This resolves a family-wide graph-design problem rather than a routine logdet KKT rephrasing; low-cost unfinished branch is stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
