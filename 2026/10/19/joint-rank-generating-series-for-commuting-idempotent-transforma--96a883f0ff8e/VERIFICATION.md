---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For commuting idempotents the product is idempotent and its image H is the intersection of their fixed-point sets. On a point fixed only by e, the f-image must be a common fixed point, because ef=fe and f fixes its output; the reverse holds for points fixed only by f. A point fixed by neither can choose its two images independently among e's and f's fixed points attached to one common root, including the root itself; equality of roots is exactly commutation at that point. Conversely these choices give the requisite idempotence, ranks and commutation on all four disjoint subsets. A component with one root, a first-only points, b second-only points and c remaining points has (a+1)^c(b+1)^c image choices for those remaining points. Distinct root components form a labeled set, giving the stated formal exponential and F_0=1. Choosing the four subsets globally first and then assigning the single-map fixed points to roots gives the exact multinomial coefficient sum. If n>0 it is positive precisely for 1≤h≤min(r,s) and r+s−h≤n; the empty assignments and c=0 cause no exceptions. Removing the component containing a specified label gives the recurrence and its stated totals. Separate direct composition on idempotents at n=4 and n=6 checked all rank triples (601 and 113989 commuting ordered pairs); exact coefficient recurrence also reproduced the totals for n=0,…,11. Replay: python3 /workspace/branches/8fe4ecb4-9ae7-4437-8bab-2340985b31bf/joint_idempotent_reproduction.py; see reproduction.log alongside it. The frozen verifier was inspected, not run; these finite checks supplement the unrestricted proof.

## originality

PASS

The supported distinct claim is the simultaneous three-image-rank enumeration on the full labeled transformation monoid, including its explicit coefficients and sharp support. The strongest inspected indexed matches either restrict, change, or explicitly exclude the target pairs. An uncited mention of full-transformation formulas and an inaccessible structural paper leave real historical-priority risk but establish no prior formula, table or rank-preserving implication. The pass is limited to the supported distinction, not a priority claim for the unweighted sequence, labeled exponential formula, or general centralizer structure.

## value

PASS

Two commuting retractions and their common retraction are natural objects in a full transformation monoid. Their three ranks distinguish the two fixed sets from their overlap and give information lost in an unweighted commuting-pair count. The explicit rooted-component weights give a usable all-size census and show why the only support restrictions are nonempty intersection and the union-size bound, without enumerating pairs of maps. This is a useful natural exact invariant rather than an arbitrary rank slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
