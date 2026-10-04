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

The analytic proof was reconstructed from definitions. For \(F_i(\mathbf p)=P_0(\mathbf p)o_i(\mathbf p)\), equality of a nonzero singleton fingerprint forces both odds vectors onto one ray. Along that ray, direct differentiation gives \(h'(u)/h(u)=\{1-\sum_i p_i(u)\}/u\), establishing the monotonicity boundary at total coordinate sum one.

For the cube obstruction, the homogeneous fingerprint coordinate is \(\phi(u)=u(1-u)^{n-1}\), with \(\phi'(u)=(1-u)^{n-2}(1-nu)\). This proves a single fold at \(u=1/n\). At the boundary, \(\phi''(1/n)=-n(1-1/n)^{n-2}\), so the singleton discrepancy changes quadratically while projection to one Bernoulli coordinate shows total variation changes at least linearly.

The bundled `verify.py` was executed from its finalized package path. It numerically reconstructs the two homogeneous branches for several dimensions and checks increasing divergence of the boundary TV-to-singleton ratio. The numerical checks are supplementary; no finite experiment is used to prove the quantified theorem.

Unproved limit: no claim is made about the optimal positive comparison constant, or even dimension-free comparability, for all cubes strictly between \(1/(2n)\) and \(1/n\).
