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

Run `python3 verify_multicolor_voter.py` using Python 3's standard library. The script constructs every connected simple graph on at most five vertices by enumerating labeled edge masks, forms isomorphism orbits under all vertex permutations, and checks every missing edge. Its opinion-equivalence partition Markov chains use `fractions.Fraction` for exact Gaussian elimination, not floating-point approximations. It also recomputes and checks the opposite-sign six-vertex differences.

The observed output reports 92 exhaustive small-graph nonedge cases, 2 connected graph isomorphism classes on three vertices, 6 on four, and 21 on five, and exact signed witness fractions. The finite census covers *all* relevant connected graphs of orders up to five by construction; it is not claimed exhaustive at order six or above. The original article retrieval comparison is bounded by source availability; independent scientific audit has not been performed.
