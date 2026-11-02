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

The mathematical proof of the long-time and weak-thermal-diffusivity statements is in RESULT.md. Independent confirmation has not been performed.

Execute the bundled file using `python verify.py` with Python 3 and no third-party packages. The completed run reported 1,607 deterministic numerical and exact-path consistency checks. Tests include finite-time reflected telegraph-path mass balance, symmetry and monotonicity of the Legendre optimizer, and convergence of the scaled edge deficit to \(-3/2^{4/3}\). Sampling uses deterministic seed 724399. Numerical diagnostics have bounded scope and cannot establish a universal large-deviation principle or replace the proof.

Scientific limitations: fixed finite interval; normal reflection; autonomous symmetric flipping; translational Brownian noise independent of propulsion; sequential \(T\to\infty\) before \(D\downarrow0\). No claim of individual-wall force fluctuations, interacting particles, or coupled long-time/small-noise regimes.
