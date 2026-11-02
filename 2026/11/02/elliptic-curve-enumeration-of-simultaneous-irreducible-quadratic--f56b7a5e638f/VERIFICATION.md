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

The standalone `verify.py` uses exact arithmetic in ten finite fields, including quadratic extension fields. It enumerates all \(a,b\) for each selected \(c,d\), forms both monic quartics, and checks irreducibility by the independent Frobenius-polynomial gcd criterion. It also enumerates elliptic points directly and checks all formula branches and Hasse's bound.

Recorded command: `python verify.py`

Recorded result: `VERIFY_OK fields=10 cases=74 direct_quartic_tests=65828`

An exhaustive calculation within each selected field and parameter pair is not an exhaustive check over all odd prime powers. The infinite theorem rests on the field-degree, character-sum, and elliptic-curve argument in `RESULT.md`. Independent audit and independent validation are not performed.
