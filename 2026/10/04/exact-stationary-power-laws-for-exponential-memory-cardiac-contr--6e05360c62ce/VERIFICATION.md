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

The symbolic verifier checks the algebraic core of the proof: \(U'(x)=G(x)\), exact cancellation of the two mixed control terms in \(\dot{\mathcal E}\), and differentiation of the polynomial primitive whose invariant mean removes \((x-v_1)(x-v_2)y\).

The invariant-measure steps are analytic. For a compactly supported invariant probability measure, generator averages of smooth observables vanish. Applying this to \(u^2/2\), \(x\), \(u\), and the damping primitive gives the stated stationary identities. Rotation invariance of the phase marginal for \(\dot\theta=\omega\ne0\) gives zero mean sine.

Strict negativity of mean controller power is not inferred from numerical sampling. If \(\langle u^2\rangle=0\), support invariance forces \(u=y=0\) and constant \(x\), contradicting nonzero periodic forcing as the phase traverses the circle.

No claim is made about orbit existence, uniqueness, basin size, or pointwise monotonicity of the storage.
