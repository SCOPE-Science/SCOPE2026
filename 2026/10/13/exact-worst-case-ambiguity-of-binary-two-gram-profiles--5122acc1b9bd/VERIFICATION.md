---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The binary two-gram count class for a linear word is determined by transition loops a=N00,b=N11 and cross counts c=N01,d=N10. Feasibility forces |c-d|<=1. For c=d=j>=1, two endpoint orientations yield B_j(a,b)=(m/j) C(a+j-1,j-1)C(b+j-1,j-1), a+b=m-2j. For |c-d|=1, only one endpoint orientation gives U_j=binomial product. Strict log-concavity balances a,b when j>=2; for j=1 all loop allocations tie. The ratio B_{j+1}*/B_j* identifies k=ceil(m/4) and exceptional adjacent tie when m=1 mod4; direct inequality B_{j0}*>max U excludes all imbalanced transitions. Central-binomial Stirling yields F_n~2^(n+1)/(pi(n-1)). Independent direct enumeration of 131,064 binary words n=3..16 checked 1,078 profile classes and every equality profile. The all-length proof is analytic.

## originality

PASS

A published earlier full distribution of SAME linear two-gram fiber sizes substantially overlaps and must be credited; its objective is number of distinct profiles/singletons, not maximizing a fiber. The new sharp max and complete modal-profile equality conditions require global log-concave discrete optimization, strict endpoint comparison and asymptotic analysis. Earlier Whittle distribution or unindexed mode formula remains substantive priority risk.

## value

PASS

Worst-case reconstruction list size for complete linear bigram multiplicities is a natural quantitative ambiguity invariant. Exact all-n sharp maximum, all maximizing profiles and 2/(pi n) asymptotic are useful independently of previously known arbitrary-profile counts; the optimization is not a random slice nor a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
