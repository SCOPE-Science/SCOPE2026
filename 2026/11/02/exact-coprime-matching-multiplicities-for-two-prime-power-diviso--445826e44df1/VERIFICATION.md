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

Run `python3 verify_coprime_matchings.py` using only the standard library. The verifier independently forms every divisor \(p^i q^j\), builds the gcd-allowed bipartite adjacency relation, and computes its permanent using dynamic programming on subsets of target divisors. This routine is algebraically independent of the closed-form falling-factorial argument. All calculations are exact integers.

Observed output:

`VERIFY_OK progression_cases=7776 occupancy_cases=846 positive=4281 zero=3495 exact_permanent_dp=yes`

The progression sweep uses the prime pairs \((2,3)\), \((2,5)\), \((3,5)\), \((3,7)\), exponent pairs with each exponent in \(\{1,2,3\}\) and at most twelve divisors, starts in the integer range from negative twelve to fourteen, and positive steps from one through nine. The occupancy sweep constructs distinct residue representatives and exhausts all nonnegative four-class populations for exponent pairs in \(\{1,2\}^2\) at prime pairs \((2,3)\), \((3,5)\).

This is finite validation. The proof in `RESULT.md` covers all distinct primes, all positive exponents, and all appropriately sized sets of distinct integers. It does not claim a computer-generated proof or independent mathematical certification.
