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

# Reproduction

With Python 3, NumPy and SciPy installed, run `python verify.py` in the directory containing this file. The script evaluates only the present model: it checks free-tree Green functions against independent finite-ball resolvents, the angular quantization against dense Toeplitz matrix diagonalization, the tridiagonal inverse identity, numerical mode counts, the large-array mode fraction, and the two finite-size shifts.

# Logical and numerical boundaries

The infinite regular-tree spectral theorem follows from the cavity resolvent, strictly monotone finite-dimensional Birman–Schwinger family, and tridiagonal angular quantization, as proved in RESULT.md. The finite tree simulations are approximations, not proofs that an infinite graph is captured by a finite cutoff. The large-size numerical samples cannot establish asymptotic statements without the displayed analytic argument. No nonstandard external certificate or independently conducted review is claimed.
