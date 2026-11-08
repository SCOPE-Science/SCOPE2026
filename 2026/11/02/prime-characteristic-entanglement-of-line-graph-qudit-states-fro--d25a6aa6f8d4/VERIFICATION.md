---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every finite simple undirected base graph, arbitrary partition of base edges E=A disjoint B (empty allowed), and prime p, the graph-state cut matrix equals unsigned-incidence product C=U_A^T U_B exactly because two distinct base edges share at most one endpoint. Removing local internal phases, additive-character orthogonality makes reduced density rho_A equal p^{-|A|} on pairs differing by ker(C^T), yielding p^r equal nonzero eigenvalues p^{-r} (r=rank_Fp C). Left kernel U_A^T has one all-one vector for each component in characteristic 2, while in odd characteristic exactly bipartite components contribute alternating indicator vectors; isolated vertices are included. Rank pairing gives r=n-q_A-q_B+rank(T_A^T T_B) even for empty matrices and odd cycles. For K_n, n>=5, Hamilton A and odd-cycle connected complementary B give q_A=1, q_B=0 odd p, and q_A=q_B=1 with overlap [n mod2] at p2, yielding stated parity split and maximal odd-prime subsystem. Independently checked 2,280 n<=4 colored graph partitions and 27 Hamilton examples, distinct from unrestricted proof.

## originality

PASS

Qualified PASS for an exact evaluated all-edge-cut signed-component overlap formula for prime-characteristic line-graph graph states and sharp Hamilton-path parity split; graph-state cut-rank and incidence-kernel lemmas are established precursors.

## value

PASS

PASS: A single exact, small-component linear-algebra formula for the entire Schmidt spectrum of all line-graph qudit bipartitions, with a concrete sharp prime-dependent maximally mixed transition. Meaningful simplification beyond generic cut-rank computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
