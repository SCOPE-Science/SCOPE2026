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

## Reproduction
Place `verify_morse.py` and `verify_boundary.py` together and run each with Python 3. The code has no external dependencies, downloaded reference data, random choices or unchecked cached intermediate data. Both programs were executed successfully from their original package source paths.

`verify_morse.py` enumerates the full finite complex, constructs every priority-ordered matched pair, checks all critical-cell dimensions and counts, and reorients each Hasse incidence. Its exact topological sort visits all 3,480 vertices and certifies acyclicity. It reports 1,694 matched pairs and critical-cell counts one in dimension zero and 91 in dimension five.

`verify_boundary.py` independently reconstructs the complex using a different indexing order and performs exact bitset elimination on all five mod-two simplicial boundary matrices. It reports rank vector `(14,91,329,661,599)` and Betti vector `(1,0,0,0,0,91)` including ordinary dimension-zero homology.

## Interpretation and limits
The complete acyclic matching—not the finite-field homology cross-check—proves the integral homotopy equivalence. The proof only treats the explicitly specified fifteen-vertex simplicial complex, not a generalized or infinite family. Reproduction assumes correct Python integer arithmetic and faithful execution of the displayed sources; no independent external audit has been performed.
