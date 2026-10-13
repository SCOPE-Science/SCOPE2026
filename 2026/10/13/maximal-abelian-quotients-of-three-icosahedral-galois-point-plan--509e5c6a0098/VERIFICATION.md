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

Run `python verification/verify.py` with Python 3. The script uses only the standard library and exact rational arithmetic. It checks:

- \(g(C_d)=(d-1)(d-2)/2\) for \(d=12,20,30\);
- \(|G_d|=60d\) and \(|G_d/\operatorname{SL}(2,5)|=d/2\);
- uniqueness of the two nonspecial full inertia orders under the divisor constraints and full Riemann--Hurwitz equation;
- the coprime-order forcing that gives the two nonspecial residual inertia orders in the cyclic abelianization;
- Riemann--Hurwitz for the residual signatures, yielding quotient genera \(1,2,4\).

The checker does not re-prove the source theorems asserting the full automorphism-group structures or the three-branch binary-icosahedral geometry. Those are the explicitly cited mathematical premises. It also does not provide equations for the three quotient curves.
