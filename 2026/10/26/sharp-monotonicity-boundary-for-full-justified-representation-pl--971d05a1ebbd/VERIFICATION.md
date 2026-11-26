---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The six inequalities agree with Teh's Hare Definition 3.1, including the elected-candidate cap and weak quota inequality. At level one a positive-weight voter has no winner approvals and cannot have acquired one. At level k, kZ<=sum_c support_active(c)y_c<=nY<=kZ forces every positively weighted candidate to be approved by all n active voters. Positive weight in the allocation must reach some unelected candidate because each active voter approves at most k-1 winners and each can supply at most z_i. That universally approved unelected candidate and the n still-underrepresented voters already give a pre-expansion certificate with x=1 per voter on that candidate and z_i=1/k. Thus at k<=2 all levels are covered. At k=3 and l=2, if there is only one unelected candidate then every active voter must approve it. EJR+ initially forces their number below 2n/3; summing their individual capacity bounds then gives 2Z<2(n/3)Y. With no unelected candidate a positive row is impossible. If n<=3, every initially unrepresented voter has an empty ballot or would already violate level-one EJR+ singly. At the new intermediate level such a voter cannot supply 2z_i with at most one approved winner; the other voters who stay below level two have unchanged ballots. For the witness the pre-change upper bounds Z<=Y, Z<=5Y/4, and 3Z<=3Y all exclude 4Y/3. In the middle bound, the two mins are bounded by convex combinations of their stated arguments, which apply to all real nonnegative weights, not only a grid. The post-change certificate assigns one approved winner and one approved loser in each row, respects the cap exactly, and has Z=4=(4/3)Y with Y=3. A fresh exact-rational replay checked the witness and bounds; replay with python replays/5.py. Packaged verifier and output were inspected, not executed. The small-parameter exhaustiveness rests on the case arguments, not profile enumeration. Minimal voter and candidate counts are at k=3, not claimed for all k.

## originality

PASS

Best-of-knowledge pass for the sharp small-parameter classification and single-approval witness, not for the definition or the existence of some nonmonotonicity.

## value

PASS

For a recently defined representation property, this distinguishes genuine robustness on one- and two-member committees from failure at three, and establishes independent lower bounds on electorate and candidate sizes at that threshold. The gain is not just a smaller instance: the top-level reduction and the support obstruction explain why counterexamples need an intermediate level and at least two unelected candidates at k=3. This is a structural result about Hare FJR+, not a claim about voters' real-world strategic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
