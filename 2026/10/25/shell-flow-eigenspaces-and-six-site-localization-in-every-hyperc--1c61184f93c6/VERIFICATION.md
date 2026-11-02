---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For each vertex v with zero coin-amplitude sum, Grover coin G=2J/d-I acts as -I. Restricting to edges of adjacent Hamming shells m,m+1, the forward/back amplitude equations are consistent exactly when µ²=p_m p_{m+1}=exp(-i(2m+1)π/d), giving both ± eigenvalues and an injective map from unsigned shell-edge incidence kernel. Shell bipartite graph is connected; its (signed) incidence rank is V-1, so r=(d-m)C(d,m)-C(d,m)-C(d,m+1)+1. Different shell pairs and eigenvalue signs yield distinct unitary eigenvalues, hence orthogonal subspaces. Summing ranks gives L_d=(d-4)2^d+2d+4, proportion tending to 1. A specific six-cycle has alternating ±1 edge values, zero sums at six vertices, two equal-norm directed components per site and normalized probability 1/6 on each of 6 sites. Independently checked d=3,4,5 every interior m, both signs and update/normalization. The theorem claims constructed subspaces only, not full eigenspace multiplicities or eigenvalue-one fixed points.

## originality

PASS

Statement- and implication-level primary-source and mathematical-index comparisons found no directly covering result in the material actually inspected; related ingredients and covered special cases are credited. Best-of-knowledge originality is qualified by the explicit residual risks; a negative search result is not novelty proof.

## value

PASS

The motivating phased-hypercube walk explicitly raises odd-dimensional localization beyond its even-dimensional eigenvalue-one examples. The construction demonstrates six-site stationary states for every odd and even dimension >=3, supplies exact shell-flow dimensions, and exhibits an asymptotically full fraction of position-coin mode space. Graph-cycle cancellation is known, but its exact Hamming-phase resonance and dimensions are nontrivial information on this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
