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

For commuting retractions, p=ef=fe is idempotent and its fixed set is the intersection of the two fixed sets. Since pe=pf=p, each fiber of p stays invariant. A fiber contains one common root, a points fixed only by e, c fixed only by f, and d fixed by neither. Each single-fixed point is sent to the root by the other map. For each of the d points there are independently (a+1)(c+1) nonrestricting choices of images; these give idempotence and send both composites to the root. On m=1+a+c+d fixed labels the resulting count is m!((a+1)(c+1))^d/(a!c!d!). Rank weights multiply over the unordered set of these rooted blocks, giving exactly the EGF. The support inequalities are inclusion-exclusion and nonemptiness; to realize an allowed triple, place the required r-t and s-t singly fixed points and any surplus at one root and use the other t-1 roots as singleton fibers. The empty pair gives the unit term. Independent direct map enumeration through n=5 matched a least-label block recurrence; recurrence output through n=8 reproduced all listed totals and the rank support and symmetry.

## originality

PASS

Credit the unrestricted labeled three-rank EGF and rank support, not the general idea of decomposing into product fibers. The strongest available prior records either count the analogous ordered problem with regressive restrictions or count a different pair condition on the full monoid. The plausible older centralizer paper remains an access-limited priority risk, not evidence of prior coverage.

## value

PASS

The statistics measure each retraction's range and their common range simultaneously. The coefficient formula gives exact counts and feasible triples for every labeled size, including their correlations, rather than just a single total or a finite table. The unrestricted rank census remains a useful result despite the related constrained encodings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
