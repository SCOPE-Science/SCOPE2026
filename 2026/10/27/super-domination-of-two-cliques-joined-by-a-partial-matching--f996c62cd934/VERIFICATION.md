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

# Reproducibility

The standalone file `verify_superdom.py` builds the graph with exactly two internal cliques and the cross matching of cardinality \(t\). For every \(n=3,4,5,6,7\) and \(t=0,\ldots,n\), it loops through every omitted set, tests directly whether each omitted vertex has a selected witness with exactly one omitted neighbor, compares the resulting truth values with the theorem, and computes independently the coefficient dictionary for super dominating sets and the inclusion-minimal members.

Run `python verify_superdom.py` from the directory containing this file and the program. The output includes `PASS total 167424 subsets, 30 parameter pairs.` The program uses the Python standard library only. A finite exhaustive test is not a proof for larger graphs; the proof is provided in `RESULT.md`.

Boundary behavior: \(n=3\) and \(t=0,1,2,n\) are included. The general theorem is not asserted for \(n=2\), and all counts refer to labeled subsets. The Cartesian-prism minimum-number specialization was previously known. A relevant 2024 super-domination-polynomial chapter was not inspected in full, leaving an explicit literature-priority limitation.
