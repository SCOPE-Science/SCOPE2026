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

Run `python3 checker.py` (Python 3.9+ standard library; no external dependencies). The code checks the exact tilted-current quadrature on three sawtooth apex locations, strict limits for varied diffusion strengths, two-sided small-temperature cusp prefactors, and an independent two-state finite-grid Poisson-bracket diffusivity calculation. In the recorded run, the program returned `PASS 93 diagnostic assertions`. With a sinusoidal potential of amplitude \(0.5\), period \(2\pi\), translational diffusion \(0.7\) and active speed \(1\), the continuum fixed-force formula gives \(Kpprox0.4212981\). The independent grid calculation shows errors decreasing to approximately \(0.0580\) at switching rate \(0.03125\).

These are finite-resolution tests; the infinite-domain and ordered-limit claims are proved through stationary flux, elliptic Poisson correction and corner Laplace estimates in RESULT.md. No independent audit was undertaken.
