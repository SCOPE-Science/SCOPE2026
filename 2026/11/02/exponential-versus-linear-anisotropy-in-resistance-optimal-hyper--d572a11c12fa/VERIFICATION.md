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

The proof derives the unique optimizer over individually variable nonnegative conductances, not merely among symmetric trial allocations. The weighted Walsh spectrum, budget normalization, derivative, and binomial asymptotics are proved in `RESULT.md`.

Executed `python verify.py` successfully with Python 3, NumPy, SciPy, and SymPy. The verifier reports 13 exact identities and 556 numeric comparisons (including full-matrix spectral checks, asymmetric allocations, KKT checks, unrestricted edge-weight optimizations, and large-dimensional asymptotic tests). The infinite-dimensional claims rely on the analytic proof, not the finite computations.

All edge weights and prices in the proof are positive at the optimum. The zero-price limit, changing price ratios with dimension, nonsymmetric prices within a coordinate class, and alternative objectives are outside the stated theorem.
