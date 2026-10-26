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

# Verification details

Execute `python3 verify_safe_prime.py 50000` after extracting this file and `RESULT.md` in the same directory. The check enumerates all primes \(p\le50000\) for which \((p-1)/2\) is also prime. It tests the exact fixed-first-entry count for primes \(p\equiv3\pmod8\) and the explicit witness for \(p\equiv7\pmod8\), using modular-power primitive-order checks rather than Legendre symbols. It also exhaustively checks the two excluded small safe primes. Observed output:

`VERIFY_OK: safe primes <= 50000, 196 in 3 mod 8 and 193 in 7 mod 8; 5,7 excluded`

The code does not prove the theorem for larger primes. The universal argument depends on the cyclic-group order classification, the hyperbola character-sum identity, and the explicitly stated boundary and nonsquare arguments in `RESULT.md`. No separate mathematical assessment beyond self-review or independent audit is claimed.
