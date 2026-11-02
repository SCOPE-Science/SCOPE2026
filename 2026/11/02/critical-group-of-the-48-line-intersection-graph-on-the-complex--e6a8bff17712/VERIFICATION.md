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

Run `python3 verify.py` in the same directory. The checker uses only the Python standard library. It constructs all 48 lines from the three pair partitions and the four odd eighth-root exponents; checks every pair-intersection using exact determinants in the cyclotomic integer ring; reproduces the complete 14-regular adjacency matrix; and confirms connectivity.

The spectrum certificate consists of an exact annihilating polynomial and traces of the first five matrix powers. The reduced graph Laplacian then has an exact matrix-tree determinant. For each of its determinant primes the verifier computes a complete local Smith diagonalization modulo a power strictly larger than the determinant valuation, checking that all local valuations account for the determinant. The invariant-factor combination is then verified for divisibility and exact product. `VERIFY_OK` means these finite calculations completed.

This procedure proves the result for the explicitly defined finite graph when used with the cited classical completeness theorem for the 48 geometric lines. It does not establish priority, publication status, or any independent mathematical audit. The critical group is not a Picard or Néron–Severi discriminant group.
