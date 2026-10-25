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

# Reproducibility and limits

Run `python3 verify.py` using a standard Python 3 interpreter. The script performs rational Taylor-series enclosures with an explicit geometric remainder, proves strict opposite signs of the derivative numerator at the two stated rational endpoints, and encloses the unique maximizing variance in a narrow rational interval. It also runs 51,200 scalar covariance/Cauchy–Schwarz grid checks, scalar variance checks, a sharpness example and finite relative-underestimation illustrations. Only the exact interval comparisons are arithmetic certificates; the numerical mesh is not proof of the continuum theorem.

The universal sign, unique maximizer, equality cases, and operator norm are established analytically in `RESULT.md` by orthogonal diagonalization, an exact covariance identity, Cauchy–Schwarz, and a derivative sign-chain. Reproducing the entire proof requires checking those algebraic and calculus steps. The statement is for exact matrix functions and excludes floating-point implementation error, higher tensor dimension, nonsymmetric generators and any convergence assertion for a complete time integrator.
