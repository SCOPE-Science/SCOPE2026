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

Run `python3 verify_boundary.py` with Python 3.9 or later from the same directory; no packages or network access are required. The script outputs `FINITE_FIELDS (135621, 5909)`, `RECURRENCES 4240`, `SHARP_h5_x05 [3]`, and `VERIFY_OK`.

The enumeration covers relevant primes no larger than 2000 and positive starting values for parameters no larger than 40. The program checks exact rational squares using integer square roots and an independent modular first-hit computation. It verifies the claimed example and many finite cases, but does not prove the result for untested primes or parameters. The proof in RESULT.md supplies the universal argument via coprime recurrences, finite-field symmetry, and prime-wise exclusion. No external or independent audit was performed.
