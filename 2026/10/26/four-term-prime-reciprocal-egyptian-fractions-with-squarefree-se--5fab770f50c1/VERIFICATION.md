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

The proof of the universal theorem is in `RESULT.md`. For an exact finite check, run `python3 verify.py` using an ordinary Python 3 interpreter and no third-party packages. The script enumerates \(55\) edges and \(341055\) four-edge selections from the primes \(\le31\), checking the reciprocal sum through `fractions.Fraction`; it finds exactly \(p=3\) with \(\{6,14,15,35\}\) and \(p=5\) with \(\{6,62,93,155\}\). The search over target primes \(p\le997\) enumerates odd divisors of \(p(p+6)\), checks admissible primality and distinctness, and independently verifies all resulting unit-fraction identities. Expected output includes `VERIFY_OK`.

Finite enumeration cannot establish exhaustiveness for larger primes. That follows from the modular leaf obstruction, graph classification, parity argument, four-cycle prime-triplet obstruction, and reversible Diophantine factorization in `RESULT.md`. The cited literature addresses different assertions; bibliographic coverage is not mathematically certified. Independent audit has not occurred.
