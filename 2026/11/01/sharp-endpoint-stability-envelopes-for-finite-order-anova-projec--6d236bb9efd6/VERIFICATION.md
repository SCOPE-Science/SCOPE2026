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

# Verification notes

The standalone `verify.py` is executable using Python's standard library only. Run `python verify.py` from the directory containing this file and the script. The checker uses exact rational arithmetic to form direct matrix rows for a finite sample of factor distributions, computes the operator norm by absolute row sums, and separately forms the expected Bernoulli kernel formula.

The actual run output was:

`VERIFY_OK independent_direct_matrix_checks=990 monotone_and_bounded_checks=140 sharp_rare_samples=21 binomial_identites=105`

The 990 independent direct matrix comparisons include nonuniform binary and three-atom marginal distributions with interaction truncations. The monotonicity and bound tests cover degrees through seven factors. The rare-event tests compare small positive-mass realizations with the universal exact combinatorial limits; the 105 combinatorial tests verify a finite range of the coefficient identity. Numerical convergence in finite samples is not a universal proof; the complete proof is the algebra and convex-order argument in RESULT.md. No external or independent scientific audit has been performed.
