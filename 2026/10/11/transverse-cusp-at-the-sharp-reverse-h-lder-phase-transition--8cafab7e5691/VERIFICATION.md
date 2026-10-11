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
The analytic proof uses the source bracket \(p_0\in(2.9414,2.9415)\) and verifies transversality without relying on floating-point computation.

The bundled `verify.py` performs three supplementary checks from its own packaged source:
1. standard-library quadrature and bisection locate the crossing inside the published bracket;
2. numerical differentiation gives a positive right-minus-left branch derivative gap;
3. exact rational arithmetic verifies
\[
\frac16\left(\frac75+\frac13\right)-\frac3{10}=-\frac1{90}.
\]

The numerical crossing and derivatives are consistency checks, not proof of the universal statement. The covariance inequality and strict-convexity step are proved analytically in `RESULT.md`.
