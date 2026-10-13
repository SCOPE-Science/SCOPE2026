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

The accompanying `verifier.py` was executed from the packaged source content with the Python standard library. It confirms actual base expansions, exact product collisions for every even \(12\le b\le1000\), independent complete input squarefreeness equivalence for even \(12\le b\le400\), and exhaustive local root counts for all primes at most \(101\). It prints a truncated Euler product and an explicit `VERIFY_OK` record.

The unrestricted result is proved in `RESULT.md` using symbolic factorizations, elementary gcd identities, Hensel lifting, CRT, and an explicit tail estimate for large prime-square divisors. Finite tests cannot prove infinite squarefree occurrence or a natural-density limit. This record is not an independent audit or external certification.
