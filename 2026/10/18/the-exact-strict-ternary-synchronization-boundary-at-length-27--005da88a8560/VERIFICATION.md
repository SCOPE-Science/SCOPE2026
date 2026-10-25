---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For ternary words the gap G(w) is minimum over every i<j<k of (k-i-2LCS(w[i:j],w[j:k]))/(k-i); strict G>1/8 is equivalent to 16LCS<7(k-i), including unequal adjacent block lengths. Relabel symbols in order of first appearance to a unique restricted-growth word. Prefix inheritance means the exhaustive recursion need test only interval triples with new right endpoint; the exact one-row LCS DP computes all such values without heuristics. Independently rebuilt this enumeration and reproduced the entire 28-entry level-count vector (1,1,2,3,5,7,10,13,14,18,17,17,16,15,12,11,10,9,9,10,11,10,9,9,10,11,1,0). Its sole canonical n=27 survivor is 012010212021012102010212012, hence six alphabet permutations, and no n=28 survivor. Independently exhaustively computed all 3276 triples for the witness with exact fractions; minimum 3/23 only at (0,12,23) and (4,15,27); no other length27 word can improve since it has G<=1/8. Prefix obstruction excludes every n>28. Inspected the second separately encoded squarefree candidate census over 5162 length27 and 6740 length28 words beginning 0; it provides additional independent exhaustive confirmation, not a bound on all untested infinite lengths.

## originality

PASS

Xu--Fu--Qiao--Tao 2026 establishes ternary synchronization strings with much smaller positive universal gap, and Appendix E exact rational tests concern a 54-uniform 952-codeword construction, not the sharp strict 1/8 last finite length. The 2018 alphabet bound and equal-length approximate repetition results do not classify unequal adjacent intervals at n=27. Resultary searches found no exact 27/28 finite strict-G boundary table; unindexed brute-force data could remain. Best-of-knowledge original under the stated exact finite parameter.

## value

PASS

Determines a sharp, mathematically motivated high-gap finite frontier and all extremizers with an exact rational optimum, directly situated within the recently established ternary alphabet question. Exhaustive finite boundary is nontrivial because normalized LCS examines all unequal adjacent intervals and 3^27 words up to normalization; self-contained useful cutoff does not need a general asymptotic result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
