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

# Finite verification

The accompanying `verify_primary.py` enumerates all spanning paths from the zero vertex and transports them by all 16 XOR translations, then builds every legal face switch on all 24 coordinate squares. `verify_alt.cpp` enumerates paths independently from every possible starting vertex, deduplicates edge masks and reconstructs switches using its own integer indexing and search. Both must confirm the full 45,696-vertex configuration graph, 69,120 edges, nine degree classes and components of sizes 1, 528 and 738 with multiplicities 5,184, 32 and 32.

The Python implementation additionally reads path endpoints from the degree-one vertices of each edge set and verifies that distance-one endpoint pairs number 32, each with 672 paths and 144 frozen paths; distance-three pairs likewise number 32, each with 756 paths and 18 frozen paths.

Neither verification is a probabilistic sample. Both exhaustively enumerate the fixed finite graph, but this is not a proof for other cube dimensions and has not undergone external independent validation.
