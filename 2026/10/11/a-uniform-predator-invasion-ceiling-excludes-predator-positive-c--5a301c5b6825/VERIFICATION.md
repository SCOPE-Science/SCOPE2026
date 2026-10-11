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

The displayed equations were checked against system (1.7) in the publisher PDF. The source's predator-free local-stability condition (4.8) was also inspected to distinguish the new global statement from the closest printed result.

For a compact invariant set, each prey coordinate attains a two-sided maximum on a complete orbit. Substitution into its exact differential equation yields the coordinate ceilings used in the theorem. Dividing the predator equation by positive predator density gives the exact logarithmic growth rate; under the stated threshold it is uniformly negative, which forces unbounded backward growth and contradicts compactness.

On the invariant plane \(y=0\), direct differentiation with \(B=(x_1x_2)^{-1}\) gives the strictly negative Dulac divergence \(-s_1/x_2-s_2/x_1\). The packaged checker re-expands this identity and the predator threshold algebra. This computational check is supplementary; the proof is the analytic argument in `RESULT.md`.

Limits: the threshold is only sufficient, it does not classify noncompact transients, and it is not asserted to be a sharp global extinction boundary.
