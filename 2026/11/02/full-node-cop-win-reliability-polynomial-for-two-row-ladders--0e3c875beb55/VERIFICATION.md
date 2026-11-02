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

# Reproducible verification

Run `python3 verify_ladder_copwin.py` using the Python standard library. The program constructs each two-row ladder from its Cartesian-product edges, enumerates all 349,515 nonempty subsets for \(1\le n\le9\), and verifies that the direct graph-level connected-acyclic test agrees with the forbidden-transition column words and with every coefficient of the rational transfer and explicit binomial formulas. For \(1\le n\le7\), a separately implemented dominated-vertex elimination routine tests cop-win status directly on every nonempty induced subgraph. For \(1\le n\le100\), exact integer arithmetic verifies all coefficient formulas, unweighted totals, first moments, maximum cardinalities, and maximum-cardinality multiplicities.

The actual execution finished with:

`VERIFY_OK: 9 exhaustive graph/word/poly comparisons (349,515 nonempty subsets), 7 independent dismantling checks, 100 exact coefficient and transfer checks`

The graph-level enumeration is finite evidence. The all-order conclusions follow instead from the local word equivalence, its exact symbolic transition equations, the gap-counting identity, and formal coefficient extraction presented in `RESULT.md`. The verifier is ordinary code, not a formal proof assistant or an independent publication-priority assessment.
