---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a prime q, multiplying by q increases v by q, 2, or 1, according to its previous exponent. Induction gives v(n) ≤ n, and for a composite n=qs with q and s at least d, v(n) ≤ q+s ≤ n/d+d. An admissible reversal keeps the digit length; a prime reversal of equal weight would equal the original prime. For a composite reversal, binary parity allows d=3; in bases 3 and 5 the parity and mod-3 checks allow d=5. In base 3 the odd prime is at least M+2 for M=3^(L−1). In base 4, odd leading digits give d=5 by digit-sum congruence, while leading digit 2 forces the sole candidate 2M+1 by the even-composite bound; its reversal M+2 fails the same bound. In base 5 the bound leaves only M+2 and M+4; their reversals dM+1 have weight at most (dM+1)/5+5 < M+d for both digits d and M≥25. All 32 cutoff cases (p<8,9,64,25 respectively, with primes divisible by the base omitted) were independently recomputed by extracting digits and factoring the reversal; no exceptions. The frozen checker was inspected, not executed.

## originality

PASS

Credit the earlier binary exclusion and the covered leading-digit-3 slice in base 4. The audited distinct claim is the completed four-base exclusion, in particular bases 3 and 5 and the closure of the uncovered base-4 cases. Neither the decimal classification, examples in larger bases, nor the earlier even-base obstruction implies this completion. The located coverage is partial, not a priority claim for binary.

## value

PASS

This answers the first four nontrivial cases of an explicit published base-classification problem and makes a mathematically useful distinction between bases that already have composite examples and bases admitting prime ones. The prime-factor thresholds and digit restrictions give exact unbounded exclusions for the missing bases/cases, rather than arbitrary scan cutoffs or recomputation of the known binary result alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
