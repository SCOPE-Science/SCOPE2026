---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Inspected exact joint tagged-block law: if tags share a block choose x−2 others then S(n−x,k−1), else independently choose x−1 and y−1 others then S(n−x−y,k−2). Indicator collapse yields a=S(n−1,k)/S(n,k), b=S(n−2,k)/S(n,k) and covariance a+n(n−2)b−(n−1)²a² (one squared pair indicator). Elementary k=2 factor F_n=2^(n−1)−n(n−2)−2 changes sign at n=6 and obeys F_(n+1)−2F_n=(n−1)(n−3). k=n−1 exactly one doubleton gives negative covariance. Independent exhaustive RGS enumeration n=2..8 matched every joint cell and rational covariance; fixed-k surjective-box conditioning proves limit (k−1)/k² with O_k(n²(1−1/k)^n).

## originality

PASS

Best-of-knowledge priority comparison against primary full/partial texts, published Resultary and target-domain queries found no mathematical implication of the final asserted new portion. Specifically: Known k! labeling and Stirling recurrence supply tools but do not by themselves state the sharp universal sign contrast at k=2 and k=n−1 for each n≥6. Earlier ingredients and special cases are credited; search absence alone is not proof.

## value

PASS

Size dependence of two labeled clusters is a canonical natural statistic of finite random partitions. Exact joint distribution, sharp n=6 sign crossover under two versus n−1 blocks, and fixed-k limit give a genuine dependence classification, not a table of Stirling numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
