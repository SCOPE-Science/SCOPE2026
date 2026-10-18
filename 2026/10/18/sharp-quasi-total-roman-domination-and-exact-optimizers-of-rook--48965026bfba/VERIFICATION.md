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

`verify.py` uses only the Python standard library. Run `python verify.py` in the directory containing the script to reproduce `verification_output.txt`.

The checker independently builds all rook-graph neighborhoods, enumerates all label-\(2\) choices up to the mathematically sharp weight \(2m\), identifies every zero cell that must instead receive label \(1\), and exhaustively enumerates the remaining permitted label-\(1\) placements. It then applies both original quasi-total Roman adjacency rules. This enumerates all labelings at or below the optimum **within the finite test graphs**, without relying on the structural theorem to validate each labeling. An independent subset-selection dynamic program computes the associated-Stirling expression and counts the exceptional cases; exact comparison succeeds on eleven small rectangular boards. Five larger defender-map cases are checked independently, all with exact integer arithmetic.

The output line `examined` counts only candidates surviving mandatory-one pruning and a weight cap, not every possible ternary function. No infinite classification is inferred from these finite computations. The universal assertion depends on the written argument in `RESULT.md`. No independent audit or external certification is claimed.
