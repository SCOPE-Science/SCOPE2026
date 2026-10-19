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

## Analytical checks

The exact angle-doubling identity maps the oscillatory integral to a Fourier cosine coefficient with a smooth weight. Repeated integration by parts generates endpoint-derivative terms; the Riemann–Lebesgue lemma controls the remainder. For polynomial compressions, expansion through three powers of inverse squared frequency determines the large and secondary eigenvalue scales. The Schur complement gives the coefficient \(21/16\); the endpoint derivative evaluation has rank \(\min(2,d-1)\).

## Reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter. Expected output: `VERIFY_OK: independent exact integrations and finite asymptotic checks: 115`.

All tests are exact-rational and finite. The implementation compares independent Chebyshev-recurrence polynomial integrations and trigonometric moment integrations, checks low-degree closed formulas and parity, and tests asymptotic coefficients at selected powers of two. A determinant test for the three-dimensional compression is consistent with the two \(4^{-n}\) eigenvalues and the \(\frac{315}{4}64^{-n}\) secondary eigenvalue. The code is not an infinite-case certificate.

## Scope of verification

The mathematical conclusions apply to fixed cutoffs and the scalar full-chaos logistic map only. Neither numerical tests nor the analytical theorem establish uniform growing-dimension estimates or operator-norm convergence. Independent validation is not performed.
