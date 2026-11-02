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

Compile `verify.cpp` with a standard C++17 compiler and optimization, then run the executable. The verifier enumerates precisely the \(972\) even Zumkeller numbers through \(4288\) by a descending subset-sum decision procedure and sieves all odd primes through \(10^9\). It checks every one of the \(55,555,554\) integers in the arithmetic progression, confirms no missing representation, and verifies the unique extremal least even summand and exact prime difference.

Expected complete-run output:

`VERIFY_OK checked=55555554 uncovered=0 maximum_least_summand=4288 unique_max_n=679570815 extremal_prime=679566527 admissible_even_summands=972`

The direct witness \(4288+2+4+8+16=4318\) gives half the sum of divisors of \(4288\), and trial division through the relevant square-root limit confirms primality of \(679566527\). A separately coded bitset-based divisor-sum implementation agrees on the \(972\) admissible even summands, and separate primality/divisor checks agree on the entire initial progression through \(10^5\) and the sharp extremum. The complete bound depends on the executable exhaustive search; the smaller checks are corroboration rather than full independent verification.

The program has no third-party package dependencies and requires approximately 63 megabytes of memory for the odd prime bitmap. The certificate is finite: it cannot establish representations beyond \(10^9\) or remove residual bibliographic uncertainty.
