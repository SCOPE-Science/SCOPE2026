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
# Verification of the maximum-set exchange classification

The standalone `verify.py` uses only the Python 3 standard library. It constructs the simple graph on \(2n\) labeled vertices directly from outer-cycle and antipodal edges, rather than generating the graph from a claimed solution classification. Two independently organized exhaustive enumerators produce the same maximum independent sets: one recurses over independent subsets of the outer cycle and subsequently tests antipodal conflicts, while the second recurses over the choices in each antipodal matching pair and checks graph adjacency. Both are compared with the claimed explicit optimum-state family.

For each integer \(3\le n\le15\), a symmetric-difference test of all optimum pairs constructs the jump graph, and a separate direct enumeration of legal slides along original graph edges constructs the slide graph. The two edge sets agree. Connected components, degrees, edge counts, full rotational move descriptions, and maximum cardinalities match the theorem. The saved `verify.py` was executed directly and its concluding output was `VERIFY_OK`.

The finite run does not certify novelty or logically imply any assertion for arbitrary \(n\). That universal conclusion is supplied by the signed-antipodal-pair proof in `RESULT.md`. No independent external audit has been performed.
