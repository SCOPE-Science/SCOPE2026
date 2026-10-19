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

Run `python3 verify_cactus.py` with Python 3 and no third-party dependencies. It prints `VERIFY_OK` after agreement between exact structural enumeration and a direct enumeration of all vertex subsets, connectivity tests, minimality tests, the size polynomial, the full exchange graph, and component sizes. `verify_output.txt` records one successful run.

The graph6-encoded instances comprise all 103 connected unlabeled cactus graphs with at most seven vertices from the graph atlas; 180 further cacti are generated reproducibly by fixed arithmetic choices. Two explicit examples test the connected Cartesian product and disconnected exchange cases. Exact subset exhaustion applies to each listed finite graph, not to infinitely many cacti. The general theorem depends on the independent block-cut-tree argument in `RESULT.md`.

The algorithm checks scientific claims but does not itself establish historical novelty. Possible unindexed equivalent statements remain. Independent audit: not performed.
