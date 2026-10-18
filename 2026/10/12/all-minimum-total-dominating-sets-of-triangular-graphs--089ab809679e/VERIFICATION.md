---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The selected K_n-edge subgraph totally dominates its line graph iff it has at most one isolated K_n vertex and no isolated K2 component. With k edges, c nontrivial components, eps isolates, and cycle rank s, n-eps=k+c-s and c<=floor(k/2). For k=ceil(2(n-1)/3), the residue-class equalities force forests of P3 blocks, optionally a P4/P5 or two P4 blocks; the proposed structural list exhausts possibilities (including n=4,5,6). Labeled partitions multiplied by Cayley tree counts 3,16,125 give all formulas. Independent direct open-neighborhood enumeration reproduced 12,80,840,630,13440 for n=4..8, including the two n=6 forest types. Finite enumeration is corroboration, the vertex-count/acyclicity argument is the all-n proof.

## originality

PASS

The same Johnson graph and exact total-domination scalar minimum appear in Cornet–Dravec–Torres 2026. Their inspected Theorem 14 specifies the number, not a complete extremizer classification or enumerator. The new labeled forest-type family is mathematically different from, not implied solely by, the scalar minimum. The line-graph edge-domination alias was explicitly searched. Equivalent older complete-graph total-edge-domination enumerators may exist but were not located in the bounded search.

## value

PASS

Minimum total dominating sets are a standard natural graph invariant; knowing every minimum set and its exact labeled count adds meaningful structural and enumerative data beyond the known minimum cardinality. The mod-3 forest dichotomy/trichotomy is a complete classification for an infinite graph family, not a sample count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
