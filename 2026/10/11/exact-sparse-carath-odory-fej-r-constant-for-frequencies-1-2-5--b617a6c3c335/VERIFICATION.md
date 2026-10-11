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

The proof was replayed in exact algebraic form. The upper bound uses positive weights \(d/(1+d)\) and \(1/(1+d)\) at \(\theta=\pi\) and \(\theta=5\pi/7\); the coefficients of \(\cos(2\theta)\) and \(\cos(5\theta)\) cancel exactly. The seventh-root relation \(8d^3-4d^2-4d+1=0\) reduces the resulting first-harmonic bound to \(1+2d\).

`verify_exact.py` checks the contact equations, the coefficient solution, the exact factorization after algebraic-number reduction, the discriminant identity, and the rational Taylor estimate \(d<223/1000\). It also numerically samples the final polynomial only as a stress check; the universal proof does not depend on that sample.

Limits: this verification concerns the continuous polynomial on the whole circle. It does not certify any discretized cyclic analogue or any support other than \(\{1,2,5\}\).
