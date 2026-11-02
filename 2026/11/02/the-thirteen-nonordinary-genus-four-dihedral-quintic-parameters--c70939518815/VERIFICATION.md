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

# Reproducibility

Run `python3 verify_d10_strata.py` using Python 3 with only its standard library. The checker returns `GENUS4_QUINTIC_D10_STRATA_PASS` after all assertions. It reconstructs binomial coefficients, coefficient reciprocity, characteristic-\(23\) factorizations and reciprocal moduli identities; it also checks several primes as finite corroboration.

The mathematical proof of the universal squarefreeness and parameter counts is in `RESULT.md`. Checking primes only up to \(151\) does not establish a statement for infinitely many primes; no such inference is made. The characteristic-\(23\) calculations are exhaustive algebraic identities, while the irreducibility tests exhaust base-field elements for the six degree-two factors. The geometric isomorphism criterion is imported from the cited primary paper. Independent validation has not occurred.
