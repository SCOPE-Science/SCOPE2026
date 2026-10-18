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

## Reproducibility

Run `python VERIFY.py` with Python 3, NumPy and SciPy available. The script computes the beta and gamma distribution-function eigenvalues, compares the nonnegative differences, verifies the closed trace identity, checks first-order asymptotics and tests mode crossings. A completed run returned `PASS: 52 cases; positivity, exact traces, trace-class first-order, spectral thresholds`.

## Analytic checks and limitations

The exact trace formula comes from the reproducing kernel's diagonal, with the radial primitive \(\int v^{d-1}(1-v)^{-d-1}\,dv=[v/(1-v)]^d/d\). The stochastic ordering uses a decreasing normalized density ratio, valid for every \(s>t>0\). The gamma-density Taylor expansion is for fixed \(d,k,t\); trace-class convergence separately requires positivity, pointwise convergence, and matching total traces. The maximizing-degree ratio is exact. Numerical checks do not establish infinitely many degrees, dimensions, or continuous parameter ranges.

Scientific priority was compared with the original March 2026 Bergman–Fock manuscript and related radial Toeplitz and Fock sampling work; the absence of a matching searched statement is not a proof of historical originality. The result has not undergone independent validation.
