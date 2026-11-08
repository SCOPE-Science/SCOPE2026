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

For unweighted one-hub G=K1 join disjoint clique blades K_{d_i}, k=sum d_i, s=min d_i, combinatorial L=D-A and H_t=e^-tL, the complete eigenspace decomposition has eigenvalues 0,k+1,1,d_i+1. With a=e^-t,b_i=e^-(d_i+1)t,c=e^-(k+1)t, signed heat-row difference has single definite positive mass at hub/other blades and deficits in the selected blade by monotonicity of (1-e^-xt)/x. Explicit optimal couplings and 1-Lipschitz dual potentials yield exact W1: within blade b_i, across blades 2a, hub to blade c+2(k-d_i)(a-c)/k. Edge W1 duality yields sharp Lip(H_t)=c+2(k-s)(a-c)/k. Calculus proves strict contraction for all t>0 iff k<=2s+1 when m>=2, else one positive-time peak; for m=1 formula collapses to e^-(k+1)t. Independent numerical matrix exponential and Kantorovich dual linear programs checked all pairs and relevant edge norms on profiles (1),(1,2),(2,3),(3,3),(1,1,4),(2,2,2) and t=0,.4,1.6, with no mismatches. Arbitrary integer profiles/all real t follow analytically, not by extrapolation.

## originality

PASS

Ollivier and Münch–Wojciechowski supply general Wasserstein/Lipschitz duality and curvature bounds; the previously known star case and infinitesimal clique-bouquet threshold are acknowledged. Neither implies the full three-orbit W1 equalities or identical full-time norm after repartitioning every nonminimal clique. Jost–Mulas–Zhang treat normalized spectral gaps on petal/book graphs, not the present combinatorial all-time W1; specialized unpublished graph transport calculations remain possible.

## value

PASS

The exact all-time heat-metric transport profile of a natural block-graph family and smallest-petal-only rigidity under nontrivial internal edge changes are mathematically motivated structural invariants, including a sharp contraction-vs-amplification transition useful in Markov semigroup curvature and metric mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
