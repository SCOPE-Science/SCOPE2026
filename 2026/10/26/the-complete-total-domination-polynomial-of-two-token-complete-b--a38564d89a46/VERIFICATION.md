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

# Reproducibility and mathematical checks

The associated `verify.py` uses only the Python standard library and takes no arguments. Run `python3 verify.py` from the directory containing it. It constructs each two-token graph directly from unordered vertex pairs and the symmetric-difference adjacency rule. An independent graph-neighborhood enumerator counts selections on each side of the resulting bipartite graph and convolves their cardinality counts. A separate full-subset enumerator checks the open-neighborhood condition without using the structural theorem.

The recorded successful execution printed `VERIFY_OK symbolic_actual=9 exhaustive=5`. Nine host pairs, \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\), were compared in every coefficient against the closed inclusion-exclusion polynomial. Five of these, \((2,2),(2,3),(2,4),(3,3),(3,4)\), were also compared against direct exhaustive enumeration over all vertex subsets. The checker verifies the exact minimum degree, Stirling-number minimum coefficient, and top coefficient.

The general result is not inferred from the finite computations: the proof in `RESULT.md` derives a necessary-and-sufficient two-sided total-domination test and counts both tests independently. No independent audit or external validation has been performed.
