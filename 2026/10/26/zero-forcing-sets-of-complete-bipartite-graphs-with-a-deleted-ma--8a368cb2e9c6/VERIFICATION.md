---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

With white complements I subset A,J subset B, no forcing into a side with three or more whites is possible because any opposite vertex misses at most one cross edge. Two white vertices on one side must include a matched index so an opposite vertex can have a unique white neighbor. If both sides have two whites with equal nonempty matched supports, every initially blue vertex sees either zero or two opposite whites and no first force exists. In all other cases with at most two whites per side, explicit forcing via b_i or a_j (possibly first clearing a one-white opposite side) reduces to at most one white per side, then finishes. Thus four structural conditions are necessary/sufficient. Enumerate white set sizes 0..4; P_m,P_n count 2-subsets meeting matched indexes; overcount at four whites is E=t(m-t)(n-t)+C(t,2) from equal nonempty matched supports. Sharp min supports for t=0,1,>=2 follow. Independent direct color-change closure over 78 m,n,t triples and 83,456 blue subsets agreed exactly; infinite family relies on case proof.

## originality

PASS

Best-of-knowledge new complete ordinary zero-forcing polynomial for K_{m,n} with t deleted disjoint edges, m,n>=3. The complete-bipartite t=0 specialization is prior and explicitly carved out. The new structural characterization uses four white-subset conditions, with two transition thresholds and crown specialization. Later zero-forcing graph-operation paper was inspected and concerns coefficient upper bounds, not target exact family.

## value

PASS

Matching deletion is a natural controlled perturbation of complete bipartite forcing. A complete all-m,n,t initial-set characterization and polynomial describe two sharp zero-forcing-number phase changes and all minimum crown forcing sets, data useful independently of more general forcing questions. Not merely t=0 coefficient reuse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
