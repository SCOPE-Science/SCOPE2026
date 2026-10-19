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
# Verification of the half-turn Fourier trace theorem

The theorem is proved for **every integer** \(L\ge1\) by an explicit Peter–Weyl reproducing kernel, the \(SO(3)\) rotation-character identity, the Chebyshev–Gegenbauer derivative identity, probability-normalized Funk–Hecke diagonalization, and an exact positive integral proving every adjacent spectral gap. The bottom eigenvalue follows from the leading-coefficient ratio of Gegenbauer and Legendre polynomials, giving the exact condition number and its asymptotic.

`checker.py` is a self-contained Python standard-library test executable with `python3 checker.py`; no external packages or inputs are needed. It computes exact polynomial coefficients and rational integrals, not floating-point approximations. For \(1\le L\le12\), it checks the character kernel, all nonzero spectral coefficients, strict ordering, the explicit smallest eigenvalue, the eigenvalue trace equal to the Wigner-band dimension, and the output rank. These tests are not the all-\(L\) proof and no external or independent validation has been performed.

Normalization conditions: both the Haar domain and the \(\mathbb{RP}^2\) axis target carry probability measure; normalized Wigner coefficients have squared norm one. A different target scaling would scale every squared singular value. The operator is point restriction to half-turns, not the Radon integral over stabilizer fibers. The nullspace remains nontrivial for \(L\ge2\), and there is no full-function recovery claim.
