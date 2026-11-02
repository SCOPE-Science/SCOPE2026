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

The analytic proof reconstructs the exact powered-distance matrix, its three zero-sum eigenfamilies with all multiplicities, and the monotonicity of the only active threshold for \(p\le1\). The strict-convexity argument excludes any later reappearance of negative type. Centering the matrix gives a positive-semidefinite Gram factorization, and its rank proves the sharp embedding dimensions. An analytic implicit-function expansion verifies the asymptotic coefficient and the comparison with the complete bipartite exponent.

Run `python verify_crown.py` with Python 3, NumPy, and SciPy to replay bounded graph-distance, spectrum, endpoint-multiplicity, and asymptotic checks. One execution produced `PASS: 178 supplementary assertions`. These tests use numerical tolerances; they cannot certify all graph orders, uniqueness of literature priority, or independent validation.
