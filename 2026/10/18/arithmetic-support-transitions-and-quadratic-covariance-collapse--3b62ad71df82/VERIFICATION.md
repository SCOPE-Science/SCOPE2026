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

# Reproducible verification

Run `python3 verify.py` using Python 3 standard library (no external packages). On the reviewed source it reports `VERIFIED 3655 deterministic checks`. Its independent 3-by-3 Lyapunov solver cross-checks analytic resonant determinant formulas for rational and irrational split fractions, verifies exact denominator resonance arithmetic, tests the nonzero sharp quadratic small eigenvalue coefficients, and checks the small-step invariant covariance limit against the continuous Lyapunov solution.

For \(\gamma=0.2\), \(\omega=1.3\), \(\sigma=1.17\), \(\alpha=1/2\), and \(h_*=2\pi/\omega\), the calculated stationary velocity variance is approximately \(5.338718097851207\), and \(\lambda_{\min}(P_h)/(h-h_*)^2\) approaches \(1.322167202261677\).

Exact irrationality, infinitely many exceptional rational steps, positive coefficients for all admissible parameters and the sharp total-variation claims depend on the analytic proof. Finite tests alone do not certify those quantifiers. The 2020 nonuniform sampling paper was accessible only through its abstract; independent literature priority and independent audit have not been performed.
