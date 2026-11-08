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
Run `python check.py` in the directory containing the standalone files, with NumPy and SciPy installed. The script tests numerous independently generated positive spectral nodes, chi-square weights, negative spike sizes, and Krylov dimensions against the exact signed moment-matrix inertia criterion; checks the two-positive-band exhaustion by direct Ritz compression; checks one rational polynomial determinant identity; and checks a single large-dimensional probability instance against the chi-square limit.

The mathematical proof is the five-part derivation in `RESULT.md`. Numerical checks cannot certify the universal finite-dimensional statement, the asymptotic limits for all admissible sequences, or priority in the literature. Independent mathematical validation has not been performed.
