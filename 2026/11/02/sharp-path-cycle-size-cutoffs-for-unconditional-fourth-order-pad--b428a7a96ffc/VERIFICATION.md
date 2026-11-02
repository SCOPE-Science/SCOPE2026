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

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3 (no third-party packages). The checker reconstructs numerator and denominator from the weighted Laplacian by exact rational matrix arithmetic and compares formula-derived entries with rational matrix inversion. The executed output was:

`VERIFY_OK {'exact_matrix_instances': 114, 'pseudoinverse_identities': 17, 'c5_kernel_identities': 15, 'multipartite_checks': 21}`

The checks cover selected integer graph sizes and rational timesteps, including large steps; they are not exhaustive over all integer orders or over real timesteps. Infinite-family correctness relies on the exact spectral argument, resistance-centering identities and the strictly positive five-cycle numerator polynomials in `RESULT.md`. The checker also verifies that row sums remain one and diagonal entries stay positive. The key large-step asymptotic is derived analytically and not inferred from numerical extrapolation. Independent mathematical assessment is not available.
