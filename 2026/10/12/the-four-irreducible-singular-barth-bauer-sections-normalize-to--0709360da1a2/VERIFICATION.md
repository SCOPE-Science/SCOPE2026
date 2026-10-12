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

The exact symbolic verifier `artifacts/verify.py` reconstructs the relevant coefficient identity, checks \(\gcd(g_1,\alpha^2+1)=1\), derives and expands the common sextic, verifies square-freeness and four distinct parameters, and checks the local Hessian at the published node.

The verifier establishes the algebraic reduction and ordinary-node check. It does not re-prove the published reduced-\(S_4\) automorphism classification, and it makes no arithmetic field-of-definition claim.
