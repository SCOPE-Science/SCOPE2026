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

The symbolic proof is the primary correctness evidence. It uses two elementary complete-multipartite facts: a set dominates exactly when it meets at least two parts or equals one whole part, and a set of at least two vertices induces a connected subgraph exactly when it meets at least two parts. From these, accuracy reduces to whether the complement contains an equally large set of one of those two types.

`verify.py` independently enumerates every nondecreasing complete-multipartite profile through order 10 and every subset of vertices. For each subset it evaluates domination, connectivity, and the accurate condition literally by enumerating all equally large complement subsets when necessary. It then compares the result with the claimed structural criterion and compares the minimum size with the closed formula. It separately verifies the published complete-bipartite formula for every tested profile with both parts of size at least two.

The finite calculation does not prove the theorem for arbitrary order. Its purpose is to test boundaries and implementation-independent consequences of the symbolic argument.
