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

For n>=5 Aut(K(n,2))=S_n. Every selected two-subset induces an edge in a labeled graph H; its membership signature at vertex v is the set of selected edges incident to v. Distinct signatures are equivalent to no K2 component and <=1 isolated vertex: a repeated nonempty signature forces an isolated selected edge. Labelled exponential formula removes singleton components exp(-t) and isolated edges exp(-zt^2/2) from all graphs, then permits one singleton with (1+t), giving the exact all-cardinality EGF. Minimizing edges in components of size >=3 yields floor(2n/3), all minima forests with enumerated residue profiles; Cayley s^(s-2) yields D_n. Independent exhaustive enumeration of all edge sets for n=5,6 and separate EGF coefficient inclusion-exclusion reconstructs D5=80,D6=840. The all-n proof is structural, not inferred from finite counts.

## originality

PASS

PASS best-of-knowledge: structural separation criterion and determining number are old; the complete all-cardinality labelled fixing polynomial and counts of all minimum fixing sets are distinct new enumerative statements not found in inspected published proofs.

## value

PASS

The symmetric-group action on 2-subsets is a canonical family, and counting all pointwise bases by cardinality is a natural finer invariant than minimum size. The exact labelled EGF, classification of every optimal forest structure, and residue counts supply independently useful enumerative data and exact benchmarks for determining-set algorithms; not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
