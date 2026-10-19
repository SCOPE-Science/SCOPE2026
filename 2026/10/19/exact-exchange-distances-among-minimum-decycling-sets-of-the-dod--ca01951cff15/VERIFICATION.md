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

# Exact finite verification

Run `python3 decycling_checker.py` in the folder containing this document. The checker uses only Python's standard library and checks the following without random sampling:

- The explicitly specified \(GP(10,2)\) has twenty degree-three vertices and thirty undirected edges.
- For every \(k\le5\) the elementary cubic edge count excludes a feedback vertex set of size \(k\).
- Every one of the \(38760\) six-element subsets is tested for acyclicity of its complement by both disjoint-set and depth-first-search methods; both accept exactly \(2520\).
- One-in/one-out swaps generate the complete simple undirected configuration graph, with \(23940\) edges.
- All-source breadth-first searches check connectivity, all \(2520\) eccentricities, the complete unordered-pair distance histogram, and the exact distance excess over \(|S\setminus T|\).

The recorded output file `decycling_checker.stdout` contains `ALL_CHECKS_PASS`. The test exhausts a finite graph, not an infinite graph family. No external audit or independent certification is claimed. The principal scientific limitation is possible previously unlocated exact work on this example, especially uninspected full text of a related paper.
