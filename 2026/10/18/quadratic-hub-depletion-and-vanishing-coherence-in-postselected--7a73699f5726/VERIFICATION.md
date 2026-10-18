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

# Verification details

The standalone `check_star.py` constructs the entire complex quantum Liouvillian independently of the five-dimensional symbolic block and compares the dominant eigenvalue, every stationary matrix entry, the eigen-equation and positive definiteness for stars with 2, 3, 4 or 6 leaves and nine mixing/detection parameter pairs per size. It also checks asymptotic coefficients at 10,000 leaves using only the small reduced matrix, and tests the \(\eta=\xi/m\) crossover. All 216 assertions passed with NumPy and SciPy in the executable verification environment.

The finite checks are corroboration of the analytic Perron semigroup and scalar implicit-function proof. They do not establish a uniform double limit, the nontrivial asymptotics by numerical extrapolation alone, experimentally robust inference, or independent scientific validation. The source paper's exact nonlinear generator and jump convention were checked against its full accessible primary text.
