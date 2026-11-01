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

Use Python 3 with NumPy and SciPy and run `python verification/check.py` from the root of the extracted package. The program solves the moment ODE with an adaptive method, independently reconstructs its ramp solution by nested numerical quadrature, checks sixty randomly generated admissible slew-bounded controls for pointwise moment dominance, tests the strictly decreasing threshold solution, and checks the small-tolerance predictions in all three spectral regimes.

The analytic certificate consists of the integrating-factor comparison and exact constant-stiffness moment evolution in RESULT.md. Computer tests are finite sample corroboration only, not proof of the universal quantifiers or publication novelty. In the critical case the leading \(\log\log\) approximation converges comparatively slowly: at \(\varepsilon=10^{-17}\), its absolute arrival-time difference is about \(0.195\), consistent with an asymptotic \(o(1)\) remainder and not a numerical accuracy claim.

Independent mathematical assessment and external certification have not been performed.
