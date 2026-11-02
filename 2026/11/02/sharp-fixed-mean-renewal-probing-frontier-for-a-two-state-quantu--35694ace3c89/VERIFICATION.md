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

# Reproducibility and verified limits

The theorem is proved analytically in `RESULT.md`, using the unitary evolution, exact renewal identity, unique tangency and global concave majorant. The attached `artifacts/verify.py` can be executed using Python 3, NumPy, SciPy and mpmath; it checks nontrivially detuned and complex-coupling Hamiltonians by matrix exponentiation, the high-precision critical root, optimal distributions, a broad majorant grid, finite-dimensional LP crosschecks and 800 random finite-support laws. Finite numerical tests do not prove the infinite-dimensional optimality; the global concavity and Jensen argument supplies that proof.

The results assume finite positive mean i.i.d. waiting intervals, perfect rank-one projective detection, and a coherent two-dimensional Hamiltonian with nonzero transition coupling. The first regime is an infimum, rather than an attained minimum, when strict positivity of every interval is imposed. No independent scientific audit has been performed.
