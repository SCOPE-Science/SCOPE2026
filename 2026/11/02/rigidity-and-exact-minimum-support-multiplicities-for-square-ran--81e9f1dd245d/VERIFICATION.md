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

# Reproducibility and verification

Run `python3 verify_spc_square_ranks.py` with Python 3.8 or later; it needs no third-party packages or network connection. The included recorded output was obtained from this standalone utility and can be recreated verbatim.

The utility exhaustively searches all bipartite edge subsets of sizes 2-by-4, 3-by-3, 3-by-4 and 4-by-4, checking exactly which support sets support an s²-dimensional cycle space at the smallest size. This checks the equality classification, not just existence of a square construction. It also checks the rank of the SPC parity equations by modular elimination over prime fields of orders 2, 3, 5 and 7. Its final line is `SPC_SQUARE_RANK_VERIFICATION_OK`.

The infinite-domain proof is the graph cycle-rank inequality and its equality conditions in `RESULT.md`. The executable does not prove the prime-power statement for all q and does not test any cases larger than 4-by-4; the proof does not depend on those experiments.
