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

# Reproducible checks

Run `python3 verify.py` with an ordinary Python 3 installation; no third-party libraries are needed. This script uses the standard library only. Its matrix entries come from the gcd/totient form of Ramanujan sums, not the incidence-matrix diagonalization used by the proof.

For each integer modulus from 2 through 30, it enumerates every square minor, computes its exact integer determinant with Bareiss elimination, forms determinantal divisors, and compares the resulting Smith invariant factors with the primewise theorem. For all moduli from 2 through 150 it separately computes exact determinants and compares the claimed formula; over the primes 2, 3, 5, 7, 11, 13, 17, and 19 it checks 1192 modular ranks using finite-field Gaussian elimination.

Observed replay:

`VERIFY_OK: 29 complete determinantal-divisor Smith checks; 149 exact determinants; 1192 modular ranks.`

This provides exact finite checks, not an exhaustive proof for every modulus. The universal proof is the elementary local module computation in RESULT.md. No independent audit has been performed.
