---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The four-cube is labelled, paths are unoriented edge sets of 15 edges, and a face switch requires two opposite square edges with replacement still a single spanning path. The source exhaustive enumerator recursively lists every self-avoiding root-zero Hamiltonian path; XOR translations cover every endpoint and canonical edge-mask deduplication counts each undirected path once. Its full 24-face transition test covers every permitted operation, and components are obtained by complete graph traversal. Independently reconstructed the edge table, DFS, translation orbit, squares and switch graph from scratch: 5,712 rooted-zero paths, 45,696 unique paths, 69,120 undirected transitions, 5,184 singleton components, 32 size-528 and 32 size-738 components; reproduced all nine degree multiplicities. Bipartite parity gives only endpoint separations 1 and 3, with 32 unordered pairs of each, and the code partitions these to 672 and 756 states per pair. Finite exhaustive proof applies only to Q4, not Qn.

## originality

PASS

Qualified best-of-knowledge: the exact Q4 face-switch path component/degree census, unlike Hamiltonian cycle and grid/backbite results, was not found in inspected literature. Single Q4 size limits breadth, but the complete graph invariant is motivated.

## value

PASS

The strict endpoint-preserving four-face reconfiguration graph of the first nontrivial four-cube is a natural canonical finite system; its exact 64 mobile endpoint components coexisting with 5,184 frozen paths refutes an intuitive endpoint-only reachability assertion and provides a full benchmark for flip dynamics. This is a substantial non-random finite classification, not an arbitrary instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
