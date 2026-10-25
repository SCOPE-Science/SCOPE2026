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
# Verification of the Fourier-zero theorem

The analytical steps are the normalized beta Fourier transform, the exact ODE, an integrated sign-definite Wronskian, the Bessel zero representation at equal beta parameters, and holomorphic implicit differentiation in the asymmetry parameter. The proof explicitly states all parameter conditions and distinguishes fixed-index expansion from large-index slope asymptotics.

Execute `python checker.py` in an environment with the dependency in `requirements.txt`. The checker separately calculates the characteristic function through `mpmath.hyp1f1`, its analytic frequency derivative, a quadrature for the nonnegative Wronskian integral, and four local complex-root continuations. The actual representative output is included as `CHECKER_OUTPUT.txt`. Finite numerical examples do not establish the universal assertions, and no independent mathematical audit or external certification has been performed.
