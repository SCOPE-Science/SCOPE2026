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

# Reproducible checks

Execute `python3 verify_matchings.py` and `python3 verify_cycles.py` in a directory containing both complete scripts (Python 3 standard library only). Both were executed from their packaged artifact paths before inclusion.

The first algorithm recursively enumerates all perfect matchings of the 30-vertex, 45-edge incidence graph by fixing the partner of the least unmatched vertex. It checks 288 matchings, the (144,144) complementary factor split, all 10,296 Hamiltonian-pair differences, 504 ten-cycle trades, all vertex degrees and 144 BFS distance profiles.

The second algorithm independently generates Hamiltonian cycles by an anchored DFS of all simple spanning paths. It removes reversal duplicates and checks 144 undirected cycles, the 504 ten-cycle trades and all 144 BFS profiles. Both report the same distance histogram \((1,7,36,85,15)\).

Exhaustive finite-state enumeration is complete for this precisely specified graph; it cannot certify priority in all literature, nor the result for other graphs. No external independent audit has been conducted.
