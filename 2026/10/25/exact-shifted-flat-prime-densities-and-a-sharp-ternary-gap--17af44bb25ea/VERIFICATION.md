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

The accompanying `verify.py` uses deterministic integer arithmetic to test the forbidden-residue formula at all odd prime squares up to 101 for nine odd shifts (225 prime-square cases); it also enumerates unit residues of the product modulus for the first three odd primes (nine Chinese-remainder cases). Exact rational finite Euler products agree with correction factors over those primes. Direct shifted-flat counts are obtained from 49,071 prime inputs greater than 106 and at most 600,000.

The successful execution returned `VERIFY_OK local_residue_cases 225 exact_CRT_cases 9 finite_primes 49071`. The script prints observed counts for shifts 1, 3, 5, 7, 9, 15, 21, 35, and 105.

These checks confirm finite identities and provide numerical consistency only. The proof of the infinite density requires the classical prime number theorem in fixed reduced arithmetic progressions and the Brun--Titchmarsh inequality; it is supplied in `RESULT.md`. No independent audit or validation has been performed.
