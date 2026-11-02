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

# Reproduction and limits

From the top-level directory containing this document, run `python3 verification/verify.py` with Python 3.8+. No third-party modules or network access are required. The checker enumerates all 512 triples of three-bit columns, builds all allowed transitions, uses an independent Kosaraju strongly connected components routine, checks the precise cyclic components and verifies the predicted cyclic count for lengths 3 through 48. It also directly enumerates every chosen-edge subset for prisms of lengths 3, 4, 5 and 6 with explicitly constructed adjacency lists.

Expected output: `VERIFY_OK states=42 arcs=102 cyclic_SCCs=1+6 brute_prisms_n=3..6 exact_all_n_by_cycle_classification`.

The graph-theoretic reduction from a perfect edge dominating set to the three local clauses, and from a periodic word to a closed walk, is proved in `RESULT.md`. The finite computation exhausts a fixed state space, rather than extrapolating from finite graph orders. Reproduction does not constitute independent mathematical certification. Full-text historical priority for all general counting results remains unverified.
