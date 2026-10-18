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
# Verification instructions

Run `python3 check.py` using Python 3 from the extracted package. The script uses only the standard library, computes exact fractions, and prints:

`VERIFY_OK: 16 intervals, 16 conditional masses, finite inequalities exact`

It verifies the exact rational inequalities for primes \(11,13,17,19,23\), four separating bounds for primes \(2,3,5,7\), the universal lower-bound coefficient at \(p=29\), uniqueness of sixteen rational left endpoints, positivity of each of sixteen conditional density weights and their exact sum \(1\).

The infinite part is not an exhaustive computation: Nagura's unconditional theorem (every real \(x\ge25\) has a prime in \((x,6x/5)\)) supplies one prime in every successive multiplicative annulus. The logarithmic inequality \(\log(1+t)\ge t/(1+t)\) and an exact geometric series then establish the coverage inequality for every prime \(p\ge29\). A greedy-subsum argument concludes density of tail products in an interval. No independent audit has been performed.
