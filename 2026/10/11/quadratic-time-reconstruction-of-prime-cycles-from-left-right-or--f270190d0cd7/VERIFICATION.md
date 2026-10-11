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

The byte-identical standalone checker source was executed before being embedded as `check_prime_cycles.py`. Exhaustive reconstruction succeeded for prime lengths \(2,3,5,7\) (respectively \(1,2,24,720\) distinct cycles), and \(200\) random cycles each at prime lengths \(11,13,17,19,23\) using seed `20261008`. The code builds a signature table from each permutation and compares its cyclic-match reconstruction to the input. The matcher uses the prefix-function method and contains no quadratic rotation scan.

The analytic check is independent of finite enumeration: each observed row is a cyclic shift of the previously known phase-set indicator word after its time-zero bit is cleared, and every proper nonempty subset of a prime cyclic group has trivial translation stabilizer. This establishes uniqueness for all primes. Each KMP search scans at most \(2p-1\) text positions for a pattern of length \(p\); at most \(p-1\) searches occur. This establishes the claimed complexity.

No test covers every prime length. The input is assumed to come from a prime cycle, and the procedure does not characterize arbitrary inconsistent signature tables. Independent mathematical audit has not been performed.
