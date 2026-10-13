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

The standalone script `artifacts/verify.py` was executed directly with standard Python. It uses exact integer factorization by a smallest-prime-factor sieve through \(10^6\) and validates the local alternating divisor-sum formula against the Liouville divisor sum on every integer through \(5000\). It then checks the iterative identity and rules out every even integer with nonsquare odd part through \(10^6\). The observed solutions through that limit were \(2,4,8,128,32768\); the known larger witness \(2^{31}\) was verified by exact Fermat-prime factorization without a large sieve.

The unrestricted proof instead derives rational inequalities \(3/4\), \(11/16\), and \(7/9\) from exact prime-power formulas. In the potentially exceptional \(\nu_2(\beta(n))=2\) branch, a factor \(3\) is forced into \(\beta(\beta(n))\); under the proposed equality it must divide \(n\), after which the remaining ratio estimate is strict. Nothing about integers beyond the finite verification limit is inferred from enumeration. Novelty screening cannot exclude all unindexed literature.
