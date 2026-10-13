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

Run `python3 verify.py`. A successful exact run checks all 109685 semiprimes through 500000, including squares, and checks the polynomial construction for primes through 3000. Output:

`VERIFY_OK limit= 500000 semiprimes_checked= 109685 hits= [6, 15, 95, 287, 1199, 4607, 23519, 28799, 101567, 223199, 296207, 352799] p_leq= 3000 family_prime_pairs= 108`

The unrestricted proof uses modular divisibility and coprimality, not brute force. All tests beyond the stated ranges remain unperformed. Independent audit has not been performed.
