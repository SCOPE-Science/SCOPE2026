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

The standalone `checker.py` iterates all multiplication-tensor coefficients in ten small cases over prime fields of orders two and three. It calculates the rank of the linear map from input monomials to the output layer and the common kernel of left/right matrix constraints. Separately, it evaluates the exact Gaussian-coefficient and subspace-Möbius prediction and asserts equality in every profile stratum. Run `python3 checker.py` to reproduce `checker_output.txt`.

The preserved output records `ALL_NILPOTENT_ANNIHILATOR_PROFILE_CHECKS_PASSED cases=10 maps=71840`. The checker covers both arbitrary and symmetric tensors, including characteristic two. It does not enumerate extension fields or prove the asymptotic bounds. Those claims are verified within the mathematical proof by quotient tensor factorization, finite-subspace Möbius inversion, Bonferroni estimates, and a surjectivity union bound. An independent scientific audit has not been performed.
