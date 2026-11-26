---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every exponent partition of m is realizable using distinct primes, and both divisor counts give the product of f(a)=(a+1)/2. In a maximizer for m>=2, merging 1 with any other part increases the product; splitting a>=6 into 3 and a-3 multiplies the product by 2(a-2)/(a+1)>1. Replacing each 5 by 3+2 preserves the product. Among the remaining parts, 2+2 is worse than 4, 2+4 is worse than 3+3, and 4+4+4 is worse than four 3s. Thus the only candidates by residue are all 3s, one 4 with 3s, or either one 2 or two 4s with 3s. The two-4 pattern wins the last comparison by 25/24 if m>=8. A maximizer with any unreduced 5 would produce a 2 on reduction, hence is possible only at m=5 (a 5 cannot occur at m=2). This recovers every equality case and proves the formulas without a cutoff. Inspected the frozen exact-rational partition verifier and its recorded check through m=40 (215307 partitions); that is supporting evidence only and was not executed.

## originality

PASS

The same multiplicative function and the classical analogous partition problem are known. The complete fixed-total-multiplicity envelope and maximizing exponent multisets are distinct on the checked evidence. The prior size-growth and mean results do not supply the needed exact comparisons at equal sum.

## value

PASS

Fixed total prime multiplicity is a natural arithmetic slice independent of prime size. An exact envelope with all equality cases provides information neither the mean nor the asymptotic maximum order supplies, including the genuine tie at m=5 and the change in the residue-two optimizing pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
