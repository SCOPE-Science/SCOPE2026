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

# Reproduction

Execute `python3 verify.py` in the same directory as the accompanying result. Expected output includes `PASS 11052 algebraic/deterministic checks`. Checks include exact rational factorization of \(2xq-(1-P^2)=x^3(3x-4)/12\), resonance \(x=4/3\), Gaussian-stage equality over 5,000 independently seeded parameter choices, exact innovation covariance, and finite-\(N\) AR(1) variance convergence toward its theoretical limit. The random inputs are reproducibly seeded. The script uses only Python 3's standard library.

The analytical derivation, not a Monte Carlo sample or finite grid, proves the claims for all admissible dimensions and steps. For finite \(N\), the stationary covariance series is \(vN^{-2}[N+2\sum_{j=1}^{N-1}(N-j)p^j]\) and converges after multiplying by \(Nh\) to \(hv(1+p)/(1-p)\); the finite-series test truncates a negligible geometric tail and accounts for finite-\(N\) correction. The formulas use the time integral of the Brownian path coupled to the same increment, not an independent surrogate.

No independent examination or validation has been undertaken.
