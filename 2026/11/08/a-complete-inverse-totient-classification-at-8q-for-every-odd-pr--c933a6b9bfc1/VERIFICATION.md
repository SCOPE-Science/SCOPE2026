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
# Reproducible checks and limits

Run `python verify.py` with Python 3. No packages are required. It performs (i) a direct totient sieve for \(1\le n\le23940\); (ii) a distinct, prime-power-factorization inverse totient search for each target \(8q\); and (iii) a check of the closed, conditional formula, for all 167 odd primes \(q\le997\). The two inverse methods and the claimed sets agree in all tested cases, including \(q=3,5\); the script prints their exact members. It also checks the cardinality predictions, including the congruence-based restrictions and absence of singleton fibers.

Expected final line:

`VERIFY_OK primes_checked=167 q_max=997 n_bound=23940 exact_phi_sieve=yes independent_prime_power_inverse=yes equality_and_disjointness=yes`

Mathematical scope: these are finite tests only. Complete correctness for arbitrary odd primes follows from the written proof. Historical originality cannot be established by a verifier. Independent mathematical audit has not been performed.
