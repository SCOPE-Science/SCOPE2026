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

For perfect evolution algebras the natural basis squares are linearly independent; zero products of distinct source basis elements force every target row of an invertible isomorphism matrix to have at most one nonzero entry, hence monomiality. The exact necessary and sufficient monomial compatibility equation is a_ij c_j=c_i² b_{σ(i),σ(j)}, including zero support and arbitrary field characteristic. Fixing primitive g in F_q^×, R1 cycles (i,t)→(i,gt) force every relational isomorphism to permute fiber indices and scale each t by c_i; this still works at q=2 where each fiber has a singleton loop. R2 edges (i,t)→(j,a_ij t²) force precisely the monomial compatibility equation for all nonzero entries, while the relation support matches zero entries. Standard directed edge/relation-type incidence gadgets and colors encode this bounded-relational vocabulary in ordinary uncolored GI with polynomial blowup for fixed q. For hardness, from simple G with n vertices,m edges the block matrix [I_n,C_G;0,I_m] has determinant one in every characteristic; its support digraph has original indegree one and edge-nodes indegree three, so the graph is recoverable and isomorphic iff the two perfect algebras are. Matrices size n+m=O(n²). Fresh exhaustive 2x2 F2/F3 comparisons and all simple graphs through n=5 corroborate; the unrestricted result is proved by the two reductions, not finite search.

## originality

PASS

Best-knowledge scientific comparison: For each fixed finite field F_q, isomorphism of perfect evolution F_q-algebras given by structure matrices is GI-complete under polynomial-time many-one reductions: a two-relation graph on n(q−1) vertices encodes arbitrary perfect algebra isomorphism, and arbitrary graph isomorphism reduces to block-unitriangular {0,1} perfect structure matrices with incidence columns of weight two. The claim provides a sharp fixed-field complexity classification of the entire natural class of perfect evolution algebras and directly answers a specifically p

## value

PASS

The claim provides a sharp fixed-field complexity classification of the entire natural class of perfect evolution algebras and directly answers a specifically posed October 2026 problem about graph-isomorphism equivalence. Both polynomial reductions matter: earlier monomial rigidity and graph-to-algebra constructions alone give neither a complete GI upper bound with all scalars nor an all-input equivalence. It does not assert a polynomial-time algorithm for GI or transfer to variable q or nonperfect algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
