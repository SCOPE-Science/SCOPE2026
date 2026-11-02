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

# Reproducibility of distance-equalizer basis counts

Execute `python3 verify_equalizer.py` with Python 3 and the standard library. The program builds edges of the root complete graph, forms separately the Johnson graph (intersecting root edges adjacent) and the Kneser graph (disjoint root edges adjacent), computes every source-to-vertex distance using breadth-first search, and uses the original existential witness condition to test all candidate sets of the asserted minimum cardinality and all pairs of smaller cardinality two when appropriate.

Observed output: triangular graph orders \(4\) through \(10\) give, in increasing order, exactly \(3,40,35,35,56,84,120\) bases. Kneser graph orders \(5\) through \(10\) give exactly \(40,35,35,56,84,120\). All structural orbit types and counts agree. The program examines 57,753 distinct candidate subsets over 13 graph instances and finishes with `All direct BFS census checks passed.`

This is a **finite** reproducibility check only. The proof that covers all natural orders uses the incidence-word equivalence and all five three-edge root-graph types; no unbounded computation or external verifier was employed. No independent audit has yet been performed.
