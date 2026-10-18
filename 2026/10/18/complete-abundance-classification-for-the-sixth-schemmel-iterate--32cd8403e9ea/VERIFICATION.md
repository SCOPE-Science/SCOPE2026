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

# Verification record

Exact-arithmetic checker: `verify_prime_powers.py` (Python 3 standard library). Executing it checks all primes at most \(1000\) and each exponent from \(1\) through \(8\), giving \(1344\) instances: \(961\) abundant, \(383\) deficient, \(0\) perfect. It also checks the closed forms at \(19\) for exponents through \(25\), and at \(83\) for exponents through \(19\). These are finite checks of an independently written iterative implementation. The universal claim is established by Steps 1–5 of `RESULT.md`, not by the checker. No formal proof assistant or independent auditor was used.
