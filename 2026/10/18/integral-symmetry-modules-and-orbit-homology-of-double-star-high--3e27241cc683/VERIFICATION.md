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

# Verification record

Run `python3 check_bistar.py` with the Python 3 standard library. The self-contained verifier reconstructs each double-star graph from adjacency bits, exhaustively searches induced component sizes, and compares each candidate face against an independently stated formula. It verifies the proposed elementary collapses *as actual free-face removals*, in descending face order, leaving precisely the full leaf simplex. Complete mod-two boundary matrices are reduced by exact bitset Gaussian elimination for all tested examples with at most eight graph vertices. Independent signed fixed-face Lefschetz sums are compared with exterior augmentation characters, including hub interchange where permitted. A full finite automorphism-group character average checks quotient-homology ranks.

The supplied `check_output.txt` is the captured output from this verifier. The expected all-success counts are 112 face criteria, 6,210 elementary collapse pairs, 84 homology computations, 266 trace comparisons, and 36 quotient ranks. Finite computation does not establish the infinite theorem; the proof's all-parameter chain argument is the primary correctness evidence. No independent scientific audit has been performed.
