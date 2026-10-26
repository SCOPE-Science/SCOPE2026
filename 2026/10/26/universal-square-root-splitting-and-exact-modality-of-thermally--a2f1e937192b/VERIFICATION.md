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

# Analytic and finite checks

The proof in `RESULT.md` establishes the theorem for all stated parameters through the exact beta-moment recurrence, zero transversality, a global one-sign-change power series, and the quartic expansion. These calculations are the mathematical basis of the result.

To reproduce the **266 finite diagnostic assertions**, run `python verification.py` with Python 3, NumPy, and SciPy installed. The program checks Jacobi quadrature for six persistence values, verifies the moment recurrence and critical fourth derivative numerically, tests modal derivative signs above/at/below each threshold, checks the universal displacement ratio near criticality, tests unimodality for five larger persistence values, and verifies monotonicity along 19 parameters. The checks use numerical quadrature and cannot establish uniqueness, absence of distant modes, or asymptotics for all real parameters by themselves.

The source's stationary Gaussian convolution and the known implicit center-curvature threshold are not proposed as new. No independent external audit has been performed. The full text of one plausible related 2026 paper was unavailable; potential priority overlap is openly retained as a limitation.
