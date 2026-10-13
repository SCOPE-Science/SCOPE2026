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

Run `python verify.py` with a supported Python 3 interpreter; the file uses no third-party packages. On the packaged reference execution the program returned `VERIFY_OK rational_sketched_Lanczos_cases= 1767 density_tail_checks= 12`.

The program assembles unreduced tridiagonal positive-definite matrices and exact rational sketches for dimensions \(k=2,3,4\). After discarding rank-deficient or exactly singular realizations, it checks the reduced matrix, determinant identity, terminal coefficient, and full Sherman–Morrison solution identity by exact fractions. It then integrates the analytic Student density around its pole in 12 numerical comparisons to the asymptotic \(2|c|f_D(-1)/R\). These tests corroborate nonstandard algebra and normalization. Rational input enumeration is not an exhaustive distributional test, and numerical quadrature is not a proof of the asymptotic.

The universal Gaussian law follows from column-orthogonal invariance and elimination against the remaining \(k-1\) Gaussian columns; the independent chi-square and standard-normal variables yield the Student-t law. Positive density at the pole proves divergent moments. A deterministic well-conditioned positive-definite witness is stated in RESULT.md. No floating-point backward-stability, conditional-embedding, adaptive-restart, or non-Gaussian-sketch guarantee has been checked.
