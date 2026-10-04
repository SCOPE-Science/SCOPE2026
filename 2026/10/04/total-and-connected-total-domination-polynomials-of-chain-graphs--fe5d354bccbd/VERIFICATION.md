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

The arbitrary-order theorem is proved symbolically in `RESULT.md`. The packaged `verify.py` is an exact finite regression check. It generates canonical connected chain graphs by nondecreasing positive neighborhood-size sequences, with both bipartition sizes at most six and total order at most eleven. For every generated graph and every vertex subset it checks the total-domination definition directly, compares it with the extreme-universal-class criterion, tests connectivity of each accepted induced subgraph, and compares brute-force size counts with the coefficients of the stated product formula.

The checker also verifies the minimum coefficient and the complete-bipartite specialization. Finite enumeration does not prove the infinite theorem; it is intended to catch boundary, indexing, connectivity, and coefficient errors.
