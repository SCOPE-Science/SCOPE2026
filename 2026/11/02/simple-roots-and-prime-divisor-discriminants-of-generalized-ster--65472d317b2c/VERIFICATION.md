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

The proof is a characteristic-\(p\) coprimality argument plus a monic-discriminant composition identity, reproduced fully in RESULT.md. Finite symbolic replay from the standalone `verify.py` extracted from this package checked \(t\in\{2,3,4,5,6,8,9\}\), indices \(3\le n\le43\) of positive degree at most \(65\). It verified polynomial normalization, complex squarefreeness by exact polynomial gcd, all 124 prime-divisor discriminant valuations, and all 74 tested odd-index modular squarefreeness cases.

Replay command: `python verify.py` (Python 3, SymPy required).

Actual output: `CHECK_OK t_values=7 squarefree_polynomials=113 valuations=124 odd_mod_prime_checks=74`

This is not exhaustive verification of the infinite family. The complete proof is mathematical, and independent audit has not been performed. The finding concerns primes dividing the parameter and does not assert exact valuations at other primes.
