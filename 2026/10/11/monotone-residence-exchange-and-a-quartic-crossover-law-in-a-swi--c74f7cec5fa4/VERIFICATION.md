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

# Verification and reproducibility

The Hamiltonian is differentiable and conserved separately in \(x>0\) and \(x<0\), with matching values and first derivatives at the switching line. For each positive energy, both turning points are unique, so the two exact side-time quadratures partition one minimal period without additional switches.

The proof's critical equality is the implicit-derivative identity
\[
\partial_\alpha[\alpha z_\alpha(u)^2+d z_\alpha(u)^3]
=\frac{\alpha z_\alpha(u)^2}{3(\alpha+d z_\alpha(u))}>0.
\]
It makes the inverse-potential time integral strictly decreasing in the cubic coefficient, a statement holding at every positive energy and not inferred from numerical samples. The endpoint beta integrals and the small-\(\alpha\) derivative \(-\sqrt2/(3d)\) yield all asymptotic coefficients.

Run the standalone standard-library checker using `python verify/check.py`. It uses a turning-point bisection and a nonsingular substitution \(s=1-t^2\) to evaluate the exact quadrature by Simpson's rule, and prints `CHECK_OK` on its prescribed tests. The checker samples finitely many energies and does not certify an infinite assertion or uniqueness by itself. There is no external auditor or external formal certificate.
