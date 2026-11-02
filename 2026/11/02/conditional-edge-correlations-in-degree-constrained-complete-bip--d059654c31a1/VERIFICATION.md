---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

**Exact mathematical check.** The weighted cofactor determinant for product conductances is \(\prod_i x_i\prod_j y_j(\sum_i x_i)^{b-1}(\sum_j y_j)^{a-1}\). Coefficient extraction at a prescribed full labeled degree vector produces factorial-moment factors \(u_i,U_{ik},v_j,V_{jl}\). The transfer-current identity for pairs gives the exact displayed three-case law; this symbolic derivation is the all-size proof. For incident edges, the one-sided two-sample deficit and the opposite-side nonnegative product prove nonpositive covariance. For disjoint edges, the two without-replacement corrections give the exact sign expression and positive examples.

**Independent finite computational cross-check.** Execute `python3 conditional_bipartite_edge_verifier.py` with Python 3 and only its standard library. It directly enumerates acyclic edge subsets rather than invoking the determinant or transfer-current identities. It checks class sizes, exact rational one-edge probabilities and all pair probabilities, nonpositive incident covariances, and both positive examples across \(K_{2,2}\), \(K_{2,3}\), \(K_{2,4}\), \(K_{2,5}\), \(K_{3,3}\), \(K_{3,4}\), \(K_{4,4}\). Observed output: `PASSED 231113 exact assertions`. Exhaustive verification of finite host sizes is not an infinite proof.

**Limitations.** This analysis is confined to simple complete bipartite graphs, feasible labeled full degree vectors and pairwise edge events. General association, arbitrary hosts and degree-multiset conditioning remain unproved. Historical priority of the conditional law remains subject to external review.
