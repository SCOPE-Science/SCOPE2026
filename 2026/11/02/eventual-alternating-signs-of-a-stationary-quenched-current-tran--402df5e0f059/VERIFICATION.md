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

The proof checks the stationary Laplace crossing kernel for both dynamics, evaluates the spatial logarithmic integral, expands the principal dilogarithm at its branch point, and transfers the logarithmic singularity into the stated alternating coefficient asymptotic. It also independently uses Pringsheim's theorem and periodicity of Laplace transforms to exclude any nonnegative probability law.

The complete standard-library checker `verify_coefficients.py` was executed from its actual packaged source and returned:

```
PASS: 6 parameter choices, coefficient recurrence through degree 240,
      second-coefficient threshold, signed tail samples, and quadrature identity.
      Finite checks do not prove eventual alternating signs or positivity failure.
```

Numerical samples support the coefficient identities; the infinite-sign theorem is proved analytically. No independent scientific audit or external validation was carried out. Published-source priority remains a separate open verification question.
