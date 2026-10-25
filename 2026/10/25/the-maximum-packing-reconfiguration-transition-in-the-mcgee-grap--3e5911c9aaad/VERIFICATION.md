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
# Reproducible verification

Run `python3 verify_a.py` and `python3 verify_b.py` with Python 3, without third-party dependencies. The first recursively enumerates independent sets and constructs legal directed exchanges, checking undirected symmetry and all-pairs shortest-path eccentricities. The second exhaustively enumerates every cardinality-nine and cardinality-ten subset, checks the edge constraints, and builds the state graphs by pairwise symmetric difference, then independently verifies their distance spectra. The outputs of the executions are recorded as `verify_a.out` and `verify_b.out`.

The original graph has 24 vertices and 36 edges, degree three throughout. The independent-set counts are `(1,24,240,1304,4212,8328,10024,7072,2668,424,8)` at cardinalities zero through ten. The number of independent eleven-sets is zero. The programs construct, without sampling, each of the 424 independent nine-sets and eight independent ten-sets and every legal move between them. All outputs and source hashes are embedded alongside this document.

This certificate proves only the finite exact claims stated. It does not independently verify worldwide originality, journal priority, or a theorem for other graphs.
