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

`verify.py` performs four checks using only the Python standard library:

1. It evaluates \(\psi\), \(\delta\), \(c_3\), and \(\phi\) for admissible parameter sets.
2. It verifies numerically that the stable-branch linear coefficient satisfies \(-f'(c_3)=\phi\).
3. It substitutes the closed-form cosine and sine coefficients into \(n_1'+\phi n_1=-\alpha c_3\sin(\omega t)\) and checks both harmonic residual coefficients.
4. For \(\sigma=5\), \(\alpha=0.3\), and \(\omega=1\), it computes \(\phi^2+1\approx9.3947331922\), the factor by which the printed Eq. (6.4) overstates the first-order harmonic amplitude.

A successful replay ends with `VERIFY_OK`.

The checker validates the algebraic first-order claim only. It does not certify a uniform error estimate for the full nonlinear finite-\(\varepsilon\) model, nor does it reproduce the article's original plotting pipeline.
