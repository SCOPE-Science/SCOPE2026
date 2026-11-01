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
# Reproduction and boundaries

Run `python3 verify.py` using Python 3.9+ and the standard library. The checker constructs the original generalized Mycielskian graph of the six-cycle independently of its quotient model. It enumerates all involution-orbits and verifies the exact orbit-conflict graph for each of the two reflection classes and levels \(1\) to \(11\). It verifies each tested folding neighborhood inclusion, then constructs all simplices and mod-two boundary ranks for the edge-axis cases through level \(7\) and vertex-axis cases through level \(3\). A successful run prints `VERIFY_OK` and a summary of finite Betti numbers.

The infinite-parameter assertion is supplied by the graph-fold lemma, the explicit three-level recurrence for the apex-deleted graph, and the homotopy-cofiber decomposition in `RESULT.md`. A finite calculation does not certify an infinite classification. This package does not claim independent replication or formal proof-assistant certification.
