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

# Verification and reproducibility

The proof and domain are in `RESULT.md`. Run `python verify_power_kernel.py` after installing `requirements.txt` (NumPy and SciPy). The script checks the explicit two-node linear-system solution, symmetric/antisymmetric squared-norm identity, kernel-mean derivative, Gaussian specialization and numerical ridge asymptotic constants. It passed **109 deterministic checks** in the stated environment.

The exact collision-tail and nugget limits are **analytical claims**. Finite integration and floating-point comparisons are diagnostic and are not independent proofs of infinite-tail exponents or exhaustive original-publication uniqueness. The kernel is two-node power-exponential on the unit interval, with fixed parameters and exact quadrature weights. The alpha-two Gaussian specialization is known; the critical alpha-three-halves transition and the all-roughness phase diagram constitute the present new mathematical claim.

Independent scientific review, independent reproduction and independent verification channels have not been performed.
