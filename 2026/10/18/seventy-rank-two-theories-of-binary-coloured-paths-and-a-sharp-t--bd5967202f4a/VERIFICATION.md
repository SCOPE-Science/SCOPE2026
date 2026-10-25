---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For ordinary first-order quantifier rank <=2 over undirected adjacency and TWO NAMED unary colours, a pointed rank-one type is determined exactly by its vertex colour, set of neighbour colours and set of distinct non-neighbour colours. Consequently a structure’s rank-two theory is exactly its set of pointed types. In word notation each local type is recoverable from 3-symbol windows and total count of each colour capped at FOUR, as local window uses at most three positions. Deterministic append transitions are closed under both colours; independent BFS reconstructs exactly 760 reachable finite states, 70 distinct theory signatures, 62 mixed-colour signatures, shortest lengths distribution (2,3,6,10,14,18,10,5,0,2), and precisely two length-10 witness words 0011001100 and 1100110011. Direct word enumeration independently corroborates signatures for all binary words through n=11; all-n result follows only from complete 760-state transition closure. Structural run proof forces at least two 1-runs and three 0-runs of size >=2 for the first 10-word signature.

## originality

PASS

Brown–Hoshino handle UNCOLOURED undirected paths and cycles; Weis–Immerman 2009 treat FO² in ordered words with an available directed successor, not arbitrary-variable quantifier-rank two in simple undirected vertex-labelled adjacency; Mwesigye–Truss 2011 classify TWO-COLOURED LINEAR ORDERS and their two-depth g(2,2)=8 model bound, which does not translate to 70 adjacency-only path types and sharp 10. Resultary one-red linear orders and directed-path bounds likewise different signatures. General two-round pointed-profile logic is known; exact 70/10 classification and finite automaton are the contribution.

## value

PASS

The classification gives a complete small-model theorem for a canonical graph class with named unary colours and ordinary bounded quantifier depth, plus a concrete sharp expression/model-size boundary ten. It distinguishes undirected adjacency reducts from linearly ordered or directed-successor words and gives all 70 attainable logical equivalence classes. This exact natural quotient is independently useful in finite-model theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
