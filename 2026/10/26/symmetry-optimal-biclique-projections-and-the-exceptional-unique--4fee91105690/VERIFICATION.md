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

Execute `python3 check_min_biclique.py` with the Python standard library. The program uses `fractions.Fraction` for exact rational arithmetic. It verifies both projection matrices, their idempotence and complementary ranges, the zero-flow constraints, endpoint operator norms and their signed difference, and explicit distinct optimal cycle projections away from the square for each \(2\le m,n\le9\): 64 bicliques and 1,936 edge columns.

The computations are not exhaustive over unbounded graph sizes. The mathematical proof for all \(m,n\ge2\) instead rests on four coefficient orbits under independent row/column permutations, invariance of both target ranges, and averaging arbitrary projections. No external proof assistant or independent audit was used. Literature comparisons and the generality of the claimed novelty require external scholarly review.
