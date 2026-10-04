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
The analytic proof establishes the multiplier invariant \(y=bz\), the residual-ratio identity \(|r|/|s|=b/\rho^2\), the induced deadband map, the sharp universal stabilization threshold \(\tau\le\mu\), and the explicit period-two obstruction when \(\tau>\mu\).

`verify.py` uses exact `fractions.Fraction` arithmetic to replay the unscaled scalar ADMM update on a grid of rational examples. It checks the multiplier invariant, residual identity, state contraction factor, finite deadband capture in the stable regime, and exact two-cycles in the unstable parameter regime. The packaged checker is corroborative; it is not used as an exhaustive proof over real parameters.

The rate-optimal fixed penalty \(\rho_*=\sqrt{ab}\) is treated as prior work and re-derived only to compare it with the residual-balancing deadband. No floating-point experiment is used to certify the theorem. Later adaptive-penalty literature was not exhaustively inspected, and the 2024 McCann--Wohlberg full text remains an originality risk noted in the review.
