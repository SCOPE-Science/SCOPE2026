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
# Verification record

Analytic proof checks: differentiate the full lift, reduce signs by half-turn conjugacy, derive \(g'(\theta)=2\sin^2\theta-\rho\sin\theta-1\), classify all negative lobes and their unique minima, and separately verify the cases \(\rho=0\), \(0<\rho<1\), \(\rho=1\), and \(\rho>1\). The threshold has a double zero of \(F'\), not a double fixed point. At the double zero \(F'''\) is positive. The same algebra verifies the asymptotic formulas near \(\rho=0\) and \(\rho=1\).

Standalone reproducibility command: `python3 check_turning.py` (Python standard library only). Observed result: `PASS: 118 deterministic parameter and asymptotic tests`. Tests include sign-changing derivative-zero counts away from tangencies, comparison of the analytic and numerically sampled derivative minimum, the near-resonance threshold scaling, and square-root separation on both sides of the first critical point.

Limits: finite sampling is not a certificate for all parameters; the exhaustive lobe argument is the proof. The related 2025 study was inspected through its abstract, not its full text. Neither independent verification nor publication-priority certification has been performed.
