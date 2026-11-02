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
# Verification of the prime-cube root-count theorem

Execute `python3 verify.py` in the same directory. The script uses only the Python standard library and independently evaluates every monic degree-six polynomial modulo eight (all 262,144 coefficient vectors), explicitly enumerates roots in the eight residue classes and checks the full probability-generating function coefficient by coefficient. It additionally calculates the local distribution for primes 3, 5, and 7, using the exact polynomial coefficients from the theorem, and tests a fixed-seed collection of monic polynomials of degrees 9, 15, and 21, respectively.

The fully enumerated dyadic case checks the prime-two boundary without a simulated distribution assumption. The independent proof for all primes uses the Chinese remainder isomorphism, Taylor expansion, and exact quadratic-polynomial counts. Finite tests do not establish the infinite theorem, the large-prime asymptotics, or a sharp degree threshold. No independent audit has been performed.
