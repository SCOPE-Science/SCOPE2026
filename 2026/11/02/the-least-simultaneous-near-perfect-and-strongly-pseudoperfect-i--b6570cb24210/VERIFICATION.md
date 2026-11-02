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

# Reproducibility and limits

The attached `verify_near_strong_overlap.py` is the exact standalone verifier. Run `python3 verify_near_strong_overlap.py` with standard Python 3.

It checks every positive integer from 2 to 174592 for the near-perfect divisor-sum equation using a complete sieve; for all 37 passing candidates, it enumerates the complete positive-divisor list, independently recomputes each divisor sum, and runs exact complementary-divisor-orbit subset-sum dynamic programming. Only 174592 passes both tests.

It also checks the factorization \(174592=2^{9}\cdot11\cdot31\), the exact divisor sum \(392832\), the proper omitted divisor \(43648\), all nine displayed complementary divisor pairs, and their sum \(349184\). The test has a fixed finite endpoint because it proves a least-element statement, not a claim over unbounded values.

Expected output:

```text
VERIFY_OK limit=174592 near_candidates=37 intersection=[174592] factorization=2^9*11*31 sigma=392832 redundant_divisor=43648 included_orbits=9 included_divisors=18
```

The scientific assessment is a self-review. Independent audit and independent validation are not performed, and no stronger certification is claimed.
