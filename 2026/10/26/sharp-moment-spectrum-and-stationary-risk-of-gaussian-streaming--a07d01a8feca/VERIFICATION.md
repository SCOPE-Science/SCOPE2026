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

The accompanying `verify.py` uses fixed-seed numerical tests and exact rational identities. It verifies 70 independent test conditions spanning a set of integer dimensions and candidate counts, beta–gamma negative moments, conditional row selection identities, and Monte Carlo second-moment recursion checks. The actual check can be repeated with `python verify.py` using NumPy and SciPy.

For universal reproducibility, read the proof in `RESULT.md`: the divergence conditions at the two corner configurations of selected radii are analytical comparisons of nonnegative integrals, not extrapolations from simulation. Invariance and uniqueness follow from isotropic contraction of random orthogonal projections and an absolutely convergent backward affine series; finite-sample numerical tests are not used to establish these infinite claims.

The diagnostic code assumes NumPy and SciPy; tests are randomized but deterministic under the included seed. No external mathematical audit has been conducted. Priority relative to specialized older literature is not certified.
