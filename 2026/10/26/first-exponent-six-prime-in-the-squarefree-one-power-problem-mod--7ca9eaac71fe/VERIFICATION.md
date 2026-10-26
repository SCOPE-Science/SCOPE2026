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

## Actual checks
An exact full-array Eratosthenes and squareful sieve enumerated 879429 primes in the class through 189954151, identifying 21 failing the initial four offsets and only 189954151 failing exponent five. An independently implemented segmented sieve reproduced those numbers and lists. The local obstruction CSV was verified by direct integer divisibility. Candidate primality and the squarefreeness of its exponent-six remainder follow from the exhaustive sieve; separate exact trial factorization supplies a cross-check.

Run `python3 verify_sieve.py` with `obstruction_certificate.csv` in the same directory, and independently compile and execute `verify_segmented.cpp` as specified in `RESULT.md`. The two checkers use different sieve layouts, not floating point approximations or probabilistic tests. No assertion about infinitely many primes is derived from the finite checks.

## Limits
Computational completeness is conditional on the inspectable sieve-loop invariants described in `RESULT.md`. The result has not undergone independent mathematical audit or external certification.
