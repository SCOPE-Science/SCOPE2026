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

Run `python verify.py` using Python 3.10 or later, with no third-party dependencies. The program reproduces the exact rational witness \(F_\beta=11574741702400/8063279547193\) and ground-state value \(405/338\), checks the sign of their rational difference, and checks the diagonal excited-state comparison. It also evaluates exact stationary Bloch residuals, analytic temperature derivatives, positive physical-state constraints and QFI, the six selected limiting pure-target latitudes, and the leading critical-curve slope against numerically located derivative-sign boundaries. The final packaged verifier passes 7,220 finite assertions.

The finite tests do **not** establish the continuous supremum or uniqueness over all temperatures and target states; these are proved in the accompanying mathematical argument through exact stationary equations, a uniform expansion on the closed Bloch ball, strict concavity, and the analytic implicit-function theorem. The explicit finite parameter witness uses rational arithmetic and needs no numerical tolerance. The high-temperature limit is taken at fixed, finite positive reset rate and bath rate, not uniformly in the ratio of those two rates. The comparison measures single-copy inverse-temperature QFI, not physical experimental costs.
