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

# Exact verification and limits

Execute `python3 verify.py` with Python \(3\) and no third-party packages. Its transfer-graph builder enumerates the \(17\) legal column types, \(119\) compatible ordered-pair states, and \(343\) triple-valid optimality transitions. Cyclic strongly connected components have sizes \(49\), \(2\), \(2\); the integer characteristic-polynomial computation confirms the exact factors in the proof. It independently enumerates matching and singleton states directly in the original prism graphs and verifies the closed-neighborhood sub-quorum inequality for \(n=3,4,5,6\).

The infinite enumeration follows because valid cyclic words are in bijection with closed transfer walks and the matrix identity holds exactly; merely checking the first four graph sizes would not prove the result. The determinant-factor check is a finite exact calculation included in the source. It is **not an independent audit**. The graph-theoretic result counts only reduced optimum colorings, not optimum partitions containing a larger color class.

Expected terminal lines include:

```
EXACT_119_STATE_TRANSFER_AND_CHARPOLY_OK [49, 2, 2]
INDEPENDENT_ORIGINAL_GRAPH_COUNT_OK 3 16
INDEPENDENT_ORIGINAL_GRAPH_COUNT_OK 4 65
INDEPENDENT_ORIGINAL_GRAPH_COUNT_OK 5 151
INDEPENDENT_ORIGINAL_GRAPH_COUNT_OK 6 434
FORMAL_RATIONAL_GENERATING_FUNCTION_CHECK_OK
VERIFY_OK
```
