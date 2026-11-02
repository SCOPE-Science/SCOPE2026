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

# Verification of the locating-total domination polynomial

`verify_prisms.py` constructs both complete clique layers, the matching edges, and open neighborhoods directly. For each \(2\le n\le10\) it examines all \(2^{2n}\) labeled subsets, requires nonempty selected neighborhoods at **every** vertex, requires distinct selected-neighborhood intersections for all distinct unselected vertices, and compares every cardinality count against the polynomial coefficients.

The observed sums of coefficients were \(9,36,149,588,2103,7178,23913,78552,255659\) for \(n=2,3,\ldots,10\). Their exact minimum sizes and multiplicities were \((2,4),(3,14),(4,56),(4,30),(5,120),(6,350),(7,896),(8,2142),(9,4920)\). Result: `VERIFY_OK`.

`verify_prisms_structure.py` separately reconstructs the graph, checks that no subset smaller than the claimed minimum is locating-total, and checks that **every** subset of minimum size matches the predicted equality structures for \(2\le n\le10\). It also checks forty explicit larger constructions for \(n\in\{11,12,17,23,35\}\). Result: `VERIFY_OK`.

The enumeration is exhaustive only for the stated finite graphs. The theorem for arbitrary \(n\) is proved by the neighborhood and coefficient argument in `RESULT.md`. Verifiers are self-contained, use only the Python standard library, and may be run with `python verify_prisms.py` and `python verify_prisms_structure.py`. All checks were rerun from the actual newly embedded checker files after the final JSONL was saved and reopened. No independent mathematical audit was performed.
