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

The proof is symbolic for every dimension and all factor sizes at least two. In particular, the induction uses a uniform regular-degree frontier and the injective predecessor-profile identity \(\sum_q k_q(\mathbf{k}-\mathbf e_q)=(k-1)\mathbf{k}\); neither assertion is inferred from experiment.

`verify_graph.py` independently enumerates graph vertices and edges and tests every intermediate stable partition on eighteen chosen products (2,859 vertices total). `verify_quotient.py` builds a compressed weighted quotient instead, and tests all tuples of 1 to 8 factor sizes chosen nondecreasingly from 2 through 7, plus twelve longer examples (3,014 tuples and 126,596 quotient states). Both use exact integer arithmetic and Python's standard library; no third-party dependencies are necessary. The actual captured outputs are supplied alongside both scripts.

The tests do not exhaust all dimensions or all factor sizes and are not a replacement for the proof. All claims concern one initially marked vertex and within-graph orbits only. The possible existence of an unlocated earlier specialized theorem remains an originality risk. Independent audit was not performed.
