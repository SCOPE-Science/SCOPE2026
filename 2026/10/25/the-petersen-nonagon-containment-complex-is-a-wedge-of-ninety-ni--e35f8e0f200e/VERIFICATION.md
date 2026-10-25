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

The standalone `verify.py` uses the Python standard library only. Execute `python3 verify.py` in the same directory; it asserts all the numerical and structural facts needed for the finite proof, and prints `VERIFY_OK` on success. `verify_output.txt` preserves an execution of the packaged script.

The exhaustive domain consists of every one of the 32,767 nonempty subsets of the fifteen Petersen-graph edges. A connected two-regular-support predicate identifies all simple cycles, including all twenty maximal nine-cycles. The complex contains 6,320 nonempty simplices; its complete oriented face-incidence graph has 32,775 arcs. A topological sort of every vertex proves the 3,110-pair discrete-Morse matching acyclic. The critical dimensions are zero (one cell) and four (99 cells).

A separate simplicial-chain calculation over \(\mathbb F_2\) gives boundary ranks \((0,14,91,354,861,1050,560,160,20)\) in dimensions zero through eight. This check does not by itself prove integral homotopy equivalence; the discrete-Morse argument does. The theorem is limited to the specifically defined Petersen nonagon-containment complex. No independent validation has been performed.
