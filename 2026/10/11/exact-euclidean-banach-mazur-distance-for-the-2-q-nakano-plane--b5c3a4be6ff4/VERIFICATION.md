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

The proof is analytic. The critical reduction is sign averaging of a positive-definite quadratic form: because the norm is invariant under independent sign changes of the two coordinates, averaging the four conjugate quadratic forms preserves any two-sided comparison with the norm while eliminating the cross term. Hence no rotated ellipse can beat the best diagonal ellipse.

For a diagonal quadratic form, the unit-sphere calculation is exact. With \(m=q/2\), \(t=y^2\), and diagonal ratio \(r>0\), the squared Euclidean form is \(F_r(t)=1-t^m+rt\) on \(0\le t\le1\). Concavity gives the minimum at an endpoint. The derivative \(F_r'(t)=r-mt^{m-1}\) gives the unique interior maximum when \(r<m\). Direct differentiation of the resulting distortion ratio proves it decreases on \(0<r\le1\), while the other two branches increase from \(r=1\). This verifies global optimality and not merely local stationarity.

The displayed \(q=4\) value is only a consistency check. No computation, numerical grid, or external certificate is needed for the theorem.
