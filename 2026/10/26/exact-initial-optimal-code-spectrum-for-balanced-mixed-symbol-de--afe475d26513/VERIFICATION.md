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

# Reproduction

Run `python3 check.py` using Python 3 (standard library only). A valid replay prints one row each for \(n=2,4,6,8,10\), then `BALANCED_MIXED_DELETION_EXACT_PASS`.

The channel enumerator removes every pair of different-valued positions from each balanced word and deduplicates outputs. The corresponding complement-confusability graph has a node for each balanced source word. `exact_codes` enumerates all cliques of the target size with exhaustive branch-and-bound; greedy color classes give a mathematically rigorous bound on further extensions, so there is no unverified heuristic pruning. A separate search confirms no clique one larger. Each reported maximum codebook is also independently replayed against its original output sets. Reversal and complement preserve the channel; their orbit action is checked on every maximum codebook.

Expected counts: size-optimum sequence \(1,2,2,6,10\), labeled-optima sequence \(2,1,40,3,666\), orbit-count sequence \(1,1,14,2,174\). At length \(10\), the two searches visit \(59{,}384\) and \(12{,}006\) branch nodes. These are exact finite certificates, not statistical experiments. No statements about larger lengths are verified here.
