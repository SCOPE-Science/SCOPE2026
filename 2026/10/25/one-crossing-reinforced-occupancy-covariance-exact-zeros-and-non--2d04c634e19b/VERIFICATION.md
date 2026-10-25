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

# Mathematical and computational verification

The probability law is Dirichlet–multinomial. Formula (1) is evaluated independently of enumeration, whereas the checker calculates all joint expectations directly from the exact composition weights. The standalone script verifies \(m\in\{3,4,5\}\), \(n=2,\ldots,8\), and \(\alpha\in\{1/2,1,3/2,2\}\) for every \(1\le r\le n\), 420 rational cases, including exact zero cases. It separately tests sign order, endpoints and the weak-composition criterion; basic floating-point asymptotic checks are supplemental. The general one-crossing, gamma limit, and limit-order disagreement are proved symbolically in RESULT.md. No finite check certifies an infinite asymptotic conclusion. Independent audit has not been performed.

Run `python3 verify.py` using the standard Python library only. Expected final output: `VERIFY_OK`.
