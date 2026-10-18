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

# Reproducibility and verification

The analytic proof reduces the claim to four independently checkable identities: the falling-factorial eigenvalue diagonal, the beta-integral kernel norm, the central-binomial convolution, and the second-order Laplace/Euler–Maclaurin expansion with a Gaussian tail bound. A finite-rank Schur decomposition establishes the nonnegative interpretation of the discrepancy.

Run `python3 check_kantorovich.py` with Python 3.9 or later. It performs exact-rational beta-integral and generating-function checks, exact finite transition-matrix power-trace checks, and floating-point asymptotic consistency checks. The checker passed 95 assertions grouped as structural checks at dimensions \(1\) through \(30\), exact stochastic-matrix calculations at dimensions through \(6\), and asymptotic consistency checks at five larger dimensions. Finite computations cannot prove an infinite asymptotic: the Gaussian-dominated expansion and Euler–Maclaurin error bounds in `RESULT.md` supply that part of the argument.

An equivalent historical derivation has not been ruled out, and no independent audit has been performed.
