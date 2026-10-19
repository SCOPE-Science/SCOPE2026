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

# Verification

Run `python3 verify_components.py` and `python3 verify_normalform.py` from the directory containing the files. The programs use only Python 3's standard library, and each terminates with `VERIFY_OK` if and only if its assertions pass.

`verify_components.py` exhaustively constructs derangements and every allowed adjacent-position swap for \(2\le n\le9\), independently partitions into connected components by breadth-first search, and checks the signatures and isolated vertices. It computes the \(n=6\) witness shortest-path distance by full breadth-first search and its unrestricted Kendall distance directly from inversions.

`verify_normalform.py` independently enumerates all derangements for \(2\le n\le8\), reorders each via the explicit canonicalization procedure, checks every intermediate state has no fixed point and no signature change, checks every prescribed sign subset has a canonical state, and locates all isolated states by a separate move generator.

The outputs in `components_output.txt` and `normalform_output.txt` are successful executions of the embedded sources. The infinite theorem follows from the structural argument in `RESULT.md`; experiments do not establish assertions for untested \(n\). The \(n=6\) minimum-distance assertion is a finite exhaustive computation, not an unsupported heuristic.
