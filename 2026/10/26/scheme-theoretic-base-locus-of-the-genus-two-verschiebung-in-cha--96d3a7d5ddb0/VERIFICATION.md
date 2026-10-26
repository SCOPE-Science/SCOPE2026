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

The local generators are reduced explicitly in RESULT.md. In the affine chart at the unique base point, the local ideal is equivalent to \( (c+a+b+ab, a^2, b^2) \), so the local ring is \(k[a,b]/(a^2,b^2)\). The supplied pure-Python checker verifies the four quadratic equations in that quotient algebra. This checks the finite local computation under the stated hypotheses; it does not certify broader claims about Frobenius dynamics. Independent audit and independent validation remain unperformed.
