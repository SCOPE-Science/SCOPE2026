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

# Verification and limits

The formal proof counts allowed labeled components of \(([n],S)\) exactly. A separate executable verifies the recurrence using direct shortest-path distances in \(L(K_n)\): all possible selected vertex subsets are handled by an include/exclude recursion that prunes only sets already containing a forbidden geodesic triple. No original or unselected set is omitted through the pruning because the forbidden property is monotone under enlargement. It compares every coefficient for \(0\le n\le7\), then verifies the top-degree and divisible-by-three multiplicity formulas for \(3\le n\le20\). The exact output is in `verification_output.txt`. Reproduce with `python3 verify_triangular_gp.py` (Python 3 standard library only).

This finite calculation is not an infinite proof; the all-size theorem follows instead from the exact graph-distance equivalence, star–triangle component classification, and labeled exponential formula proved in `RESULT.md`. The novelty check read the same-graph extremal results and the complementary Kneser-graph polynomial literature but did not establish uniqueness among all possible classical labeled-component enumerators. No independent audit or external certification has been performed.
