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

# Reproducibility

The full symbolic argument is in `RESULT.md`. Run `python3 qudit_torus_check.py` with Python 3.9 or later and the standard library; compare exact stdout with `qudit_torus_verification.log`. The checker independently constructs all checkerboard adjacency matrices, performs exact Gaussian elimination in the finite field, and verifies the predicted deficit in 420 parameter cases (310 equal-valuation and 110 unequal-valuation cases), across local prime dimensions 3, 5, 7 and 11. It also constructs the truncated crossing-algebra multiplication matrix and checks 15 quotient dimensions against the general local-length lemma. All 435 exact finite comparisons passed.

The proof's all-size assertions rely instead on factorization of the Laurent multiplier and the monic-quadratic local intersection calculation. Exhaustive computation in a bounded window is not an infinite proof. No independent audit has been performed, and historical priority is provisional against unlocated specialized grid-rank tables.
