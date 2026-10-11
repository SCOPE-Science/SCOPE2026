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
The packaged checker `verification.py` was executed from its actual package path and returned `VERIFY_OK`.

It verifies the exact generator relation
\[
L\left(\frac{Q^2+D^2}{2}\right)=\mu Q^2-\nu D^2,
\]
the residual equalities
\[
VD-\mu Q=-\dot Q,
\qquad
VQ-\nu D=\dot D,
\qquad
QD-(V-\Gamma)=\dot V,
\]
and the source-parameter ratio
\[
\frac{119/1000}{1/10}=\frac{119}{100}.
\]

The conditional-expectation argument is analytic and is not certified by finite sampling. No numerical trajectory is used to infer an infinite-time or all-invariant-measures statement. The literature comparison is not exhaustive; the later fractional-order article was inspected only at abstract level.
