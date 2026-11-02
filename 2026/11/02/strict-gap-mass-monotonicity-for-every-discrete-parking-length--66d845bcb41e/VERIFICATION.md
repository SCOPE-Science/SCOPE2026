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

# Reproducibility

Run `python3 rsa_monotonicity_checker.py` with a standard Python interpreter. It uses no external packages and asserts a rigorous lower enclosure of the universal integral greater than 0.001, over 750 cells, followed by an analytic tail estimate. Its literal output is in `verification_log.txt`.

The checked inequality is \(\int_0^\infty x(1-x)e^{-x-2J(x)}\,dx>0.001\). The program uses scaled integer intervals with outward division/multiplication and alternating Taylor polynomials. The sign validity follows from explicit remainder bounds for the nonnegative domains covered.

The analytic proof additionally requires verifying the integration-by-parts identity, the exact gap-step identity, increasing moment ratios, the strict right-Riemann-sum derivative inequality, likelihood-ratio stochastic order, and the continuum monotonic-ratio derivative. All are stated and justified in `RESULT.md`. Numerical checks alone would not prove these analytic steps.

Independent audit: not performed. The claim is subject to future independent mathematical scrutiny and historical-priority checks.
