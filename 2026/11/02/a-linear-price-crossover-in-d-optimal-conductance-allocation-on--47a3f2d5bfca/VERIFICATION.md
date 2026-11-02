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

# Reproducible verification

Run `python3 VERIFY.py` from the extracted package directory. The script uses only the Python 3 standard library; its completed execution reported `PASS: 124 checks; standard-library exact cofactors, resolvents and crossover tests`.

The checks compare exact integer Bareiss cofactors with independent Fourier eigenvalue products for small square tori, solve the stationary scalar equation, test reciprocal prices and root monotonicity, check the closed cyclic-resolvent identity, and verify convergence to the two-term singular-price expansion. The proof that the optimum is globally unique for every size and every price uses strict determinant concavity; the infinite-volume crossover uses exact resolvent expansions, periodic quadrature and monotonicity. Finite tests cannot certify those universal assertions by enumeration. No independent review is asserted.
