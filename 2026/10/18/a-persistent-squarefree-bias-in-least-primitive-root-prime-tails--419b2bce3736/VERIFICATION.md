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

The proof is analytic and self-contained apart from the prime number theorem and standard elementary number theory. To rerun the finite consistency checks, use `python3 VERIFY.py` with Python 3 standard library. It prints a finite-product enclosure for \(K\), checks exact local prime-square counts for eight primes, verifies the full residue census modulo \(900\), and compares direct samples through \(100000\) with their predictions at six cutoff values. The program tests the \(p=2\) boundary separately in the same calculations.

Checks cannot replace the infinite sieve argument or the prime number theorem. The relative asymptotic is proved only in the explicitly stated logarithmic window. No independent validation is claimed.
