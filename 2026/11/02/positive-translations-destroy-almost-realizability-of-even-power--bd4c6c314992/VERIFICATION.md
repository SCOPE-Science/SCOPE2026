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

# Reproducibility and limits

Run `python3 verify.py` with standard-library Python 3. The checker computes modular Fibonacci values via fast doubling and uses separate matrix exponentiation to verify the companion-matrix Frobenius statements; it checks all odd primes below 250 congruent to 2 or 3 modulo 5, translations 1 through 20, and exponents 2 through 12. It also tests integer binomial parity, the fixed positive comparison difference for small parameters, and the unshifted modulo-five obstruction at the first six even exponents. It prints `VERIFY_OK` with counts if and only if every asserted check succeeds.

**Logical limit:** The finite checks do not prove the quantified infinite theorem or Dirichlet's theorem. The complete mathematical proof appears in RESULT.md, including the independent derivation of matrix identities and the infinite prime obstruction. The \(h=0\) sufficiency is a cited published theorem rather than a new computational certificate. Bibliographic priority is not independently certified.
