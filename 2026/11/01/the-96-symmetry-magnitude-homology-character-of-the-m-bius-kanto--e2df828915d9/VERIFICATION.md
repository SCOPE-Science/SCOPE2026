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
# Reproducibility and limits

The accompanying `magnitude_verify.py` is a standalone standard-library Python 3 program. Run `python3 magnitude_verify.py` from the directory containing `character_table.csv`. The program exactly reconstructs the graph and distance matrix; exhaustively forms the four length-four magnitude chain groups; tests signed integral compositions; obtains complete binary elimination ranks \(1040\) and \(1248\); verifies \(48\) independent alternating cycles; exhaustively enumerates all \(96\) distance-preserving permutations; and checks every line of the full individual character table and the three-dimensional invariant average. Its actual terminal output is recorded in `verification_output.txt`.

Correctness uses binary matrix ranks only as lower bounds for rational ranks, with independent upper bounds from the chain complex and explicit cycles. Thus no inference about integral torsion from finite-field ranks is made. The proof concerns rational homology in a single bidegree, not an integral module classification. The bibliographic comparison cannot exclude an undiscovered or unindexed identical result.
