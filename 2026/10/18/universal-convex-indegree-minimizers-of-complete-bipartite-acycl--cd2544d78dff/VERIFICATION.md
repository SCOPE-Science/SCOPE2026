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

# Computational verification and limits

The standalone `check_minimizers.py` enumerates each direction assignment of the actual labelled edges of \(K_{a,b}\) and uses Kahn topological elimination to reject cyclic orientations. It then independently determines the minimum \(\sum_v\varphi(\operatorname{indeg}(v))\) and its multiplicity and checks them against the claimed formulas and indegree multiset.

The checked part sizes were all \(1\le a\le b\le4\), plus \((1,5),(2,5),(3,5)\). Four strictly convex functions were tested: quadratic, cubic, exponentiation, and a nonmonotone quadratic with negative linear term. Output of the checked execution: `PASS: 52 strictly-convex cost tests, 104334 edge assignments, 13638 acyclic orientations.`

This is finite verification; the mathematical proof for unrestricted part sizes and all common strictly convex functions uses canonical part-words, improving adjacent switches, and exact run-factorial counts. A proof of absolute bibliographic novelty and independent external validation are not supplied.
