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

# Reproducible verification

Extract `artifacts/check.py` and run `python3 artifacts/check.py`. It uses exact integer arithmetic, basic deterministic trial-division primality tests, modular fast doubling, and no external packages. The program checks the first 16 prime-part primes through 53 and a total of 63 pairs of exponents; it prints `CHECK_OK primes 16 q_power_pairs 63` when completed. For p=5 the explicitly chosen exponents are 2,12,22; for other primes they are 2,4,6,8. These finite comparisons are consistent with the algebraic argument but are not an infinite verification.

The proof itself requires the classical rank-of-apparition theorem and Fibonacci valuation formulas as displayed in arXiv:2609.24544v1, plus CRT, Dirichlet and the elementary lifting-the-exponent lemma. The review is same-model only; no independent audit has been performed.
