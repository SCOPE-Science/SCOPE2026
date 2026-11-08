---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Let u be any nonconstant binary scattered triple, k≥3; host W itself must avoid u and contain every length-k u-avoider. Reversal and complementation reduce six patterns to 001 and 010. For 001 the forced host form 1^a0 1^b0^c and witnesses 1^(k-2)01, 01^(k-1), 0^k imply a≥k−2,b≥k−1,c≥k−1, equality unique; complete decomposition of u-avoiding targets proves coverage of 1^(k−2)0 1^(k−1)0^(k−1). For 010 all zeros are one run, and witnesses impose W=1^(k−1)0^k1^(k−1). Independent exhaustive brute-force over all admissible hosts through minimal bound for k=3,4,5 verified unique winners for both orbit reps. Thus L=3k−4+number of changes in u. Finite checks corroborate, proof covers all integer k≥3.

## originality

PASS

PASS qualified: Fleischmann et al. 2022 study near-k-universality and Simon congruence, while Adamson et al. 2024/2025 fix universality index and optimize the count of missing scattered subsequences, not the single prescribed forbidden triple and its uniquely shortest internally avoiding host. General constructions for unary missing factors may be related; no inspected theorem covers both nonconstant orbits.

## value

PASS

The first nonunary fixed-forbidden-subsequence constrained universal host problem has a complete all-k classification, exact transition statistic and literal uniqueness. A genuinely structural combinatorial boundary case, not an arbitrary finite sample or textbook embedding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
