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

# Verification of exact prime-modulus periods

Run `python3 verify_prime_periods.py` using Python 3 and SymPy. The program reconstructs the rational function from the exact partition bijection and differential operators; checks the polynomial identity and the resultants 864, 32, 144, 36; directly enumerates four-part partitions for 68 sizes; and checks the least predicted periods for primes 5, 7, 11, 13, 17, 19, 31, 41. The symbolic proof for the full infinite family is in RESULT.md. All checks succeeded in the stated environment. No independent scientific audit is asserted.
