---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Possible outputs retain the last symbol and, for longer words, are the unchanged word or its immediate suffix. Conflicts are exactly parent–child and sibling pairs in four disjoint suffix trees. In each tree a four-vertex clique (the root and its three children) and six length-3/length-4 pairs bound a code by seven words, attained by the root and all leaves. Equality forces one choice per block; the three sibling groups independently contribute x4(x4+2x3) unless the short selected word is their parent, in which case both leaves are forced. This gives the stated P and factors across terminal symbols. The rooted transfer recurrence also follows: choosing the root forbids every child, while excluding it allows at most one child, with no cross-branch conflicts among lower selections. Direct independent packing of the actual output masks recovered all seven local optimal profiles. Convolving them four times and weighting by word length gave 8,503,056 global optima of size 28, minimum length 88 with multiplicity 4096 and unique composition (4,0,12,12), and maximum length 104 with multiplicity 81.

## originality

PASS

Pass is restricted to the enumeration, composition and length extrema of all maximum labeled codes. The size 28 and existence of optima in precisely this model are prior work. The closest inspected exact classification records count different configurations, and the theorem giving the known maximum does not determine its full set of equality cases.

## value

PASS

The exact labeled optimum spectrum distinguishes cardinality-optimal selections that have very different total lengths and identifies the unique minimum-length composition. Four symbols is the first nontrivial profile case beyond the rigid three-symbol maximum, where the root and two length-three leaves are forced in each component. A designer or enumerative researcher can use the exact composition frequencies, rather than a single construction, to assess the cardinality–length tradeoff in this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
