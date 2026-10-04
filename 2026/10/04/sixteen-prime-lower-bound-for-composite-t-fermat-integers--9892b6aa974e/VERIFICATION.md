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

The universal conclusion reduces to a finite exact census because any hypothetical composite T-Fermat integer with \(M\le15\) must have every prime divisor below \(2^M\), all divisors in one common \(\nu_2(p-1)\) class, and every ordered pair satisfying an odd multiplicative-order condition.

`verify_tfermat_bound.py` performs the following checks with integer arithmetic only:

1. Sieve every prime below \(2^{15}\).
2. For each \(3\le M\le15\), retain primes below \(2^M\) and group them by \(\nu_2(p-1)\).
3. Compute each required multiplicative order exactly by factoring the relevant Euler totient and reducing the order with modular exponentiation.
4. Enumerate all \(M\)-cliques recursively in every common-valuation class.
5. Confirm that the target-clique list is empty for \(3\le M\le14\), contains exactly one support for \(M=15\), and test that support against every Korselt divisibility condition.

The replay output is:

`VERIFY_OK M=3..14_no_compatible_cliques M=15_unique_compatible_clique_not_Carmichael`

`M15_CLIQUE 331 631 751 991 2311 4951 7351 11251 11551 14851 17011 25411 26251 28351 30871`

`M15_KORSELT_WITNESS ('331', 90)`

The accompanying `tfermat_bound_certificate.json` records the exact graph sizes, all target-size cliques, and the Korselt remainders. The finite computation proves only the exclusion needed for \(M\le15\); it does not test or certify any claim for \(M\ge16\). The cited structural lemmas from the primary source are premises of this reduction and were checked in the source text, not recomputed by the verifier.
