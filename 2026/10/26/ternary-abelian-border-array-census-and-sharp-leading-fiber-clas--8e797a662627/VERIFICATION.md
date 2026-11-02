---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Global alphabet relabeling preserves all prefix Parikh equalities. Every ternary word has a unique restricted-growth representative; the examined artifacts/abelian_census.cpp runs a complete depth-first enumeration (3^n+3)/6 representatives through n=16, computes Parikh prefix counts, and packs each border length into distinct 4-bit positions (length <=16). Independently inspected artifacts/abelian_independent.cpp instead enumerates all 3^(n-1) words beginning with 0 and uses base32 prefix count differences with no borrow (all counts <=16), computing the same exact table. Our separate Python implementation exhaustively computed every first-zero ternary word for n<=11 and matched T_3(1..11), top three fiber multiplicities and specific two runner-up arrays. The all-n fiber bound follows from second-letter branch and each subsequent symbol either forced 0 if border i-1 or one of 1,2 otherwise; the all-zero branch attains 2^(n-2) restricted-growth words. The two runner-up cases follow by first repeated zero and strict split at next position, with 6 labeled permutations for every nonconstant canonical representative. The n=12..16 table rests on inspected exhaustive algorithm and its two independent implementations, not our truncated Python check; no infinite table extrapolation.

## originality

PASS

Best-of-knowledge: compared mathematical implication, equivalent aliases, broader frameworks and exact tables; not directly covered by sources actually inspected. Residual literature risks and incomplete full-text access are explicitly recorded.

## value

PASS

A natural reconstruction ambiguity invariant beyond the binary case: exact attainable signature counts through a substantial finite cutoff plus all-length extremal fiber geometry. The 16-term table is independently motivated by the explicitly open ternary complexity in the 2021 parent work; the infinite top-two classification remains useful without a full all-n census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
