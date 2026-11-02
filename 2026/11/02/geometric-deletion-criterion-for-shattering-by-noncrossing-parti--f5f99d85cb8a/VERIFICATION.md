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

Use Python 3.10+ (standard library only). In the directory containing the accompanying scripts, run `python3 verify_geometric.py`, `python3 verify_traces.py`, and `python3 verify_closure.py`. These invoke three independently represented exhaustive algorithms: chord-intersection reachability after deletion, explicit enumeration of Catalan concept traces, and recursive merging of crossing blocks. The geometric run covers vertex counts 4 through 8; direct-trace run covers 4 through 7; closure run covers 4 through 6.

The deterministic expected outputs are compared against every f-vector in the article. The largest geometric census has 28 candidate pair queries and enumerates supports only through seven queries because all larger supports fail by the proven forest bound. The direct-trace algorithm enumerates all noncrossing partitions and exhaustively checks both truth values at every selected query. Each script raises an assertion on any discrepancy.

The finite scripts check the explicit tables and selected structural implications, but do not certify novelty, the general all-size geometric lemma or an external independent audit. The all-size theorem depends on the self-contained planar separation argument in `RESULT.md`.
