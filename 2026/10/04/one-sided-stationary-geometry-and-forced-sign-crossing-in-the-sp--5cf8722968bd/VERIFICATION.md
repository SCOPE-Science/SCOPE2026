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
The canonical vector field was checked from a full-text same-object source. `verify.py` uses only Python's standard library and exact rational arithmetic. It verifies the unique equilibrium \((1/4,1/16,0)\), the exact offset \((1/4)^2=1/16\), and evaluation of the vector field at the equilibrium. Its recorded output ends in `VERIFY_OK`.

The conditional-expectation identities and the strict \(y>0\) support theorem are analytic rather than finite computational claims. They are verified in `RESULT.md` from generator stationarity and the exact backward variation-of-constants formula. The checker does not claim to certify measure invariance, literature originality, or any independent review.
