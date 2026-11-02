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

# Computational verification and logical scope

Run `python3 VERIFY_EXACT.py`. The program uses only standard Python library exact fractions, not floating-point comparisons.

The exhaustive check enumerates every set partition for paths of orders one through nine and cycles of orders three through nine; it computes induced-subgraph shortest paths directly for each coalition and compares the maximum welfare and number of maximizers with the theorem. It includes all disconnected coalition sets, not merely interval partitions.

Separate checks enumerate all contiguous path compositions by exact dynamic programming through order one hundred and all cyclic-cut patterns through order sixteen. Both check optimum values and counts. All assertions passed when the packaged code was executed.

These finite checks are not a proof for arbitrary numbers of vertices. The universal result follows from the strict path-length splitting inequality, the proper-cycle edge-cut reduction, the explicit grand-coalition formula, and the exact counting argument in `RESULT.md`. No independently audited or externally certified verification is asserted.
