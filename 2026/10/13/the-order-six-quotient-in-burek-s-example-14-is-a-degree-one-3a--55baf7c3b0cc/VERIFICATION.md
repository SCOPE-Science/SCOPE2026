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

The included `verify_burek_quotient.py` checks the algebra used in the finding with exact symbolic arithmetic.

It verifies:
- projective smoothness of the cubic \(Y\) by checking all four standard affine charts;
- smoothness of the complete intersection \(C=V(F,Q)\) from the Jacobian-minor criterion;
- that \(Y\cap\{a=b=0\}\) consists of exactly three reduced points because \(c(c^2+d^2)\) is square-free;
- the canonical-degree computation \(K_Z^2=1\);
- the Riemann--Hurwitz computation giving \(g(C/\langle\tau\rangle)=1\).

The local \(A_2\) classification is proved symbolically in the text from the residual tangent weights \((1,2)\); the script checks the reduced intersection that excludes the weight-zero tangent direction.

A fresh copy of the included verifier was replayed after packaging and returned `VERIFY_OK`.

Limits: the verifier establishes the exact calculations used here; it is not a classification of all order-six K3 quotients and does not assess independent novelty.
