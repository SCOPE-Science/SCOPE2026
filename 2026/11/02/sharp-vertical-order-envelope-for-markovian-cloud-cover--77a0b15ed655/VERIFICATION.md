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

# Verification

The mathematical verification is the path-degree and induced-forest proof in `RESULT.md`. In particular, the two sharp bounds are attained by explicit permutations for every finite number of cloud levels; finite computations do not establish this universal quantifier.

Run `python3 verify_cloud.py` using Python 3 and only its standard library. The program evaluates the Markov clear-state recursion directly from pairwise cloudy probabilities and separately computes the edge-minimum factorization. It exhaustively enumerates permutations for layer counts 2 through 8 with four overlap weights, checks repeated fractions, constructs both extremizers, and verifies the monotone gap on a rational parameter grid. The run passed **369,986 assertions** and printed `CLOUD_MIN=454/625 CLOUD_MAX=3917/5000 GAP=57/1000`.

The theorem requires a common adjacent overlap weight and first-order Markov dependence. This checker is a reproducibility tool, not a proof for arbitrarily many layers, and is not empirical validation of atmospheric radiative fluxes. Historical priority is evidence-limited and independent audit has not been performed.
