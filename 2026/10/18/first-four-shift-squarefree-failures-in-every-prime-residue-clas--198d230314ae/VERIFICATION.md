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

# Exact computational verification

Run `python3 verify.py` with the Python 3 standard library. Expected stdout is embedded in `certificate_output.txt`; the final line is `VERIFY_OK; 12 residue-class minima; bound 6165527`.

The verifier builds an exact sieve of primes through \(6{,}165{,}527\) and exhaustively tests the four positive shifts of each prime in every reduced class modulo \(36\). It then repeats the entire search with a separate prime-square trial predicate and confirms the primality and four explicit square-divisor witnesses for each minimum. The paper's proof explains why the finite enumeration is exhaustive for each *least-prime* claim, not an extrapolation. Both predicates use the same prime list, whose correctness follows from the elementary Eratosthenes invariant; witness primality is independently checked by integer trial division.

The verification establishes only the twelve least-prime values, not a distribution or infinitude theorem. Publication overlap comparisons remain subject to the source-access limitations stated in the result and review.
