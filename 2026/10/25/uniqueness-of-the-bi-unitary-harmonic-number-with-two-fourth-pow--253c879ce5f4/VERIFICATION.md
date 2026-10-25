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

The accompanying `verify_biharmonic.py` is Python 3 standard-library-only, deterministic, exact and self-contained. It implements (1) the strict first-prime bound, (2) the 72 complete second-prime integer-free intervals, (3) the congruence \(c\mid hB\), and (4) complete factorization of every finite denominator and candidate integer level. It refuses to return success if a large unfactored residual remains or any unaccounted solution appears. The program enumerates all three permutations of the prime exponents \((4,4,1)\), so the singleton prime may be smallest, middle, or largest.

Actual successful execution from the embedded file yielded:

```
VERIFY_OK
cutoff_checks 72 first_primes 24 max_first 89 max_second 389
ordered_prime_pattern_pairs_tested 4644 interval_feasible_pairs 1540 integer_levels 44193 last_prime_candidates 36313
largest_reduced_denominator 2761790798745225 largest_denominator_prime_factor 143263
solutions [(9072, 12, 2, 3, 7, (4, 4, 1))]
```

The output is a certificate of **finite** branch exhaustion only in conjunction with the proved monotonic bounds and the modular last-prime reduction in `RESULT.md`. Merely counting examples up to a numerical cutoff would not prove the universal statement. The basic primality sieve and complete-factoring assertions are included for reproducibility. The source-overlap assessment is the literature-based self-review recorded in `AUDIT.json`, not independent validation.
