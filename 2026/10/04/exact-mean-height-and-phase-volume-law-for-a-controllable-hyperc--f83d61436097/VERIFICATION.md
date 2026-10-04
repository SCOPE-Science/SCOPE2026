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

The printed vector field is
\[
\dot x=-ay-xz-u,\quad \dot y=x(z-c),\quad \dot z=-b-mxy,\quad \dot u=kx-y.
\]
For \(R=m y^2+(z-c)^2\), direct differentiation gives
\[
2my\,x(z-c)+2(z-c)(-b-mxy)=-2b(z-c),
\]
with exact cancellation of the nonlinear terms. This is the critical algebraic step; no numerical experiment is used to extend a finite observation to an infinite-time theorem.

Integrating the identity gives the finite-time boundary-term formula exactly. Boundedness is used only to make \(R(T)/T\to0\). For invariant measures, compact support is used to justify integrating the generator of \(R\). The divergence is independently reconstructed from the four diagonal Jacobian entries and equals \(-z\), matching the introducing source. Liouville's formula then yields the exact determinant identity.

As a source-consistency check only, the reported exponents at \(c=1\) sum to \(-0.9999\), while those at \(c=1.3\) sum to \(-1.3001\), agreeing with the exact sums \(-1\) and \(-1.3\) to displayed precision. These rounded values are not used as proof.

Limits: the verification does not establish global boundedness, existence of any attractor, hyperchaos, or individual exponents. It does not resolve whether the inaccessible full text of the 2014 precursor contains a fixed-parameter special case.
