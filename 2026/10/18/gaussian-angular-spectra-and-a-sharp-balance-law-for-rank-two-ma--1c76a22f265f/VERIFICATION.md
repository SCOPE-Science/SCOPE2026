---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

The matroid greedy algorithm selects the top Gaussian coordinate x and the highest coordinate y outside its parallel class; symmetry of uniform rank permutations gives the sum 1/[n(n-a_i)]+1/[n(n-a_j)]. Summing p_xy^s over all cross-class pairs gives every collision moment, including n²C2=sum_i b_i+2sum_{i<j}b_i b_j for b_i=a_i/(n-a_i). Differentiation along fixed-total-sum pair transfers gives n(a_i-a_j)[a_i+a_j+2(2n-a_i-a_j)T]/[(n-a_i)^2(n-a_j)^2], strictly positive when a_i>a_j, proving unique balanced/skewed integer extremizers up to permutations (degenerate single-partition cases included). Exact face formulas f0=sum_{i<j}a_i a_j and f1=sum_i a_i choose(n-a_i,2) yield both examples (1,4,5,8) and (2,2,7,7) with f0=109, f1=1250, yet C2=11581/1253070 versus 11617/1254528 (difference 2151/119799680). Independently computed these exact rational identities and greedy finite rank-order examples. For fixed m the balanced and skew asymptotics follow directly from class-size expressions.

## originality

PASS

Best-of-knowledge originality established for the final exact claim, not for known supporting formulas: searched published Resultary records and compared actual mathematical statements, same-object literature, reductions and stronger plausible frameworks; this PASS is conditional on the explicitly documented access/priority risks.

## value

PASS

Determining the complete outward cone-angle spectrum and the sharp balancing law connects a canonical matroid base-polytope family to randomized optimization. The two face-count twins establish the mathematically motivated non-reconstructibility of this Euclidean angular functional from low face data, rather than a gratuitous parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
