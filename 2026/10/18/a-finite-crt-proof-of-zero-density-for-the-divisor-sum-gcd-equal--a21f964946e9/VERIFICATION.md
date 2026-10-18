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

The accompanying standalone `verify.py` computes the divisor sum of each square from its prime factorization and tests the exact defining GCD equality for all integers from 1 through 1,000,000. It compares six cumulative checkpoints, checks two explicit prime-root witnesses at primes 7 and 13, and checks the exact \(q-1\) valuation-one residue count modulo \(q^2\) for nine primes. Execute with `python3 verify.py` using Python 3's standard library.

These are finite regression checks. The infinite theorem requires the symbolic CRT and variance argument, multiplicativity of the divisor sum, and the classical divergence of prime reciprocals in reduced arithmetic progressions. The proof makes no extrapolation from the finite results. An independent audit has not been performed.
