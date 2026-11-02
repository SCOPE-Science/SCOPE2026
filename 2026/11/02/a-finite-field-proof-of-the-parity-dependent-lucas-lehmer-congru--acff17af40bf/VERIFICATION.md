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

Run `python3 verify.py` after installing SymPy. The code computes the Lucas–Lehmer recurrence modulo each prime \(P=2^{n-1}+3\) for \(3\le n\le400\), separately verifies the quadratic-field trace identity for primes below 20,000 using pair arithmetic, and asserts the two congruence classes. It returned `VERIFY_OK prime_cases=16 trace_cases=570`.

These are finite checks, not an exhaustive enumeration of primes nor an infinite proof. The full proof in `RESULT.md` uses quadratic reciprocity and the Frobenius automorphism. No test of the converse or of pseudoprimes is claimed.
