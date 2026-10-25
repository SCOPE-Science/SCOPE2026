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

The attached `VERIFY.py` uses Python's standard library only. It checks the Laurent exponent recurrences in the characteristic-three partial derivatives, the defining equation modulo \(t^{21}-1\), the exact Hessian rank and kernel at \(P_1\), and the nonzero restricted cubic term. It checks the order of \(3\) modulo \(7\), and enumerates the prime-field normalized singular support. Execute `python3 VERIFY.py` in the extracted directory. The script reports `VERIFY_OK` when these identities pass.

These are exact integer/modular checks; the universal assertions are established in the accompanying proof by explicit ideal elimination, factorization, and formal quadratic splitting. The finite-field enumeration does not imply the geometric point classification by itself. The formal splitting argument uses characteristic \(3\ne2\), Hessian corank one, and the nonzero cubic kernel coefficient; it has not been independently certified.
