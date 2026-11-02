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

Execute `python check_symbolic.py` using SymPy and `python check_numeric.py` using NumPy. The first asserts that all nine symbolic stationary covariance residuals vanish identically under the exact Lindblad second-moment generator. The second constructs a basis for nine Hermitian covariance coordinates, solves an independent full linear system for 256 seeded random parameter sets, compares its result and current with the closed form, and verifies the claimed optimizer against 1,750 sampled rates. These checks passed from files extracted directly from the final embedded record. Finite testing is not an infinite-dimensional proof, and full-state uniqueness is not claimed.
