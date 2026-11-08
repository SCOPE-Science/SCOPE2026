---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every even M>=4, the word has exactly M occurrences of 1, begins and ends with 1, odd zero-gaps equal 1 and even gaps >=3. The canonical W_M=(101000)^(M/2-1)101 is a scattered subsequence of every member. W4 is 4-universal via its four complete binary blocks; prefix 101000 is 2-universal, so W_(M+2)=101000 W_M preserves full M+2-universality. The explicit 23 length-5 present words of W4 provide the base certificate for 9 missing words. Greedy earliest-prefix matching in the six-letter prefix and induction determine the only missing critical targets as {α1^(M-3)β : α∈{00,01,11}, β∈{00,10,11}}. For an arbitrary longer-gap word, the boundary patterns force >=z initial+final omitted ones whereas an embedding would omit only z-1, so all 9 remain absent. Cantor substitution 1→101,0→000 gives gap lengths 3^{nu_2(j)} for j=1..2^k−1 and M=2^k at k>=2, proving the specialization. I independently enumerated all binary target subsequences in canonical M=4,6,8,10 and Cantor k=2,3,4; every instance had universality M and exactly the specified 9 missing words. The all-even-M theorem is supplied by the induction/omission argument, not sample extrapolation.

## originality

PASS

Qualified acceptance for the exact nine-word first-absent spectrum on a natural Cantor substitution and a strictly wider arbitrary alternating-gap family, rather than for the classical Cantor morphism or generic subsequence algorithms.

## value

PASS

The first nonuniversal length is a canonical invariant of scattered-subsequence complexity, and this result completely describes its absent language for a natural automatic Cantor word and an infinite alternating-gap extension. The constant nine forbidden patterns persist despite arbitrarily long heavy gaps and exponentially increasing number of ones; the precise set, not just its cardinality, can be used as an exact benchmark in word combinatorics/sequence matching. This is not a routine known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
