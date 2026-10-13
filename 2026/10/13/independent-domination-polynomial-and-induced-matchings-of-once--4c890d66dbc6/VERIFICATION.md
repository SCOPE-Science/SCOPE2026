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

# Verification of the one-subdivision independent-domination theorem

`CHECK.py` is a standalone Python 3.10+ program; run from the extracted artifact directory as `python CHECK.py`. An installed version of NetworkX is used for nonisomorphic-tree and random-forest checks; if absent those extra tests are explicitly skipped, while the graph-subset and induced-matching checks still run. `CHECK_OUTPUT.txt` records a run where all checks, including optional ones, passed.

The direct evaluator constructs the full one-subdivision graph by inserting an independent vertex for each base edge, then checks independence and dominating neighborhoods on *every* selected-vertex subset of each tested graph. A separate evaluator enumerates original-vertex subsets and applies the stated no-isolate criterion. Agreement is checked coefficient by coefficient. A third evaluator enumerates candidate induced matchings of the base graph and checks equality of the polynomial's minimum exponent with the proposed matching expression.

Exhaustive domain: all labeled simple graphs of order zero through five (\(1{,}100\) base graphs, \(1{,}901{,}463\) direct subdivision-subsets); additional seeded random instances of orders six and seven (\(119\) base graphs, \(1{,}328{,}512\) direct subdivision-subsets). The recurrence was compared against independent induced-subset counting on \(201\) nonisomorphic trees of orders one through ten and \(640\) seeded random forests. The three-rung ladder was independently checked against all \(8{,}192\) subdivision-subsets and yielded the polynomial \(x^4+27x^5+7x^6+x^7\).

These are finite tests, not a computational proof for unbounded graphs. The universal argument is the forced-insertion bijection and the tree-component/induced-matching inequalities written in `RESULT.md`. The tree dynamic program uses symbolic Laurent weights and finite convolution; it is not a numerical approximation. No independent audit or external formal proof has been undertaken.
