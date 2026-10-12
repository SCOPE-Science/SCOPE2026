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
The verification artifact uses exact rational arithmetic only.

For \(t=6/5\), it reconstructs the upper-bidiagonal \(M\)-matrix and positive right-hand side, computes the first GMRES coefficient, solves the second-step normal equations exactly, and verifies
\[
x^{(1)}
=
\frac1{47}(5,10,10,5)^{\mathsf T}
\]
and
\[
x^{(2)}
=
\frac1{1777}(6445,5630,2000,-815)^{\mathsf T}.
\]
It also checks the positive exact solution and the exact residual-norm decrease.

The script compares the direct GMRES calculation with the closed coordinate formulas at rational values below, at, and above \(t=1\). The interval-wide sign result and the field-of-values threshold are analytic statements proved in RESULT.md, not conclusions drawn from finite sampling.
