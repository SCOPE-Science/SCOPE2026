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

# Reproducibility and limits

Run `python3 verify.py` (Python standard library only) after extracting the supplied standalone file. The program builds four-row masks and tests repeated row pairs, independently implements the original mutual-visibility shortest-path condition for small widths, checks extension maximality vertex by vertex, and compares every cardinality coefficient with the formulas in `RESULT.md`.

Checks performed: exhaustive \(2^{4n}\) subsets for \(n=2,3,4,5\), and exhaustive pair-disjoint admissible recursion for \(n=6\). The respective numbers of admissible sets are \(189,1952,18521,165120,1401445\), totaling \(1,587,227\). The maximal spectrum for \(n=6\) is \(6984,11520,31680,720\) at cardinalities \(9,10,11,12\). The program reports `ALL_CHECKS_PASS` when all assertions pass.

Finite enumeration cannot certify an infinite family: the full proof uses the pair-consumption decomposition and an exhaustive classification of simple graphs on four labeled row vertices. No independent mathematical audit has been performed.
