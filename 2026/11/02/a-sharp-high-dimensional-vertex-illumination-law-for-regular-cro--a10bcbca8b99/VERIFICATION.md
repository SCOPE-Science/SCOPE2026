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
# Mathematical verification

The proof is self-contained and distinguishes exact identities from asymptotic consequences. Both standalone Python programs were executed from their delivered source paths. `check_illumination.py` independently integrates the dimension-three simplex probability, reproduces its spherical-angle value, and compares Gaussian directions against the direct Dirichlet expectation. It tests the conditional means and leading dimension-asymptotic factor. `check_dirichlet_moments.py` symbolically verifies the fourth central moment identity used to control Taylor remainders. Exact cases and symbolic checks do not constitute an external formal proof or an independent audit; generality rests on the analytical argument.

For reproducibility, execute `python check_illumination.py` and `python check_dirichlet_moments.py` in a Python environment with NumPy, SciPy and SymPy. The random stream has a fixed seed; Monte Carlo comparisons have explicit statistical tolerances. No external data or downloaded paper is required by either checker.
