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

A path matching is inclusion-maximal exactly when its indicator has no adjacent ones and every zero touches a one. For m>0 this is equivalent to a first one at edge 1 or 2, successive gaps of length 2 or 3, and the last one at edge m−1 or m (indices restricted to existing edges). The empty path has one hypothesis. The two first-one choices give the asserted recurrence for m≥3. A depth-d tree needs at least 2^d distinct consistent hypotheses, since each fixed matching follows one leaf. My independent gap-based enumeration and depth-feasibility recursion exactly recovered the complete profile, checked every leaf of each supplied shattered tree against its entire branch (including the empty-path certificate), and checked the printed 65-matching list against the generated class. At m=15 only edges 4 and 12 give two branches of size at least 32, each splitting 33 no/32 yes. Reflection reduces to edge 4. In its no branch only edge 12 splits with both counts ≥16, giving 17 no/16 yes. In the doubly negative branch only edge 8 splits with both counts ≥8, giving 8 no/9 yes. In both final subfamilies the maximum smaller side over all edges is 3, so neither can shatter depth three. This precludes depth six at m=15, while the validated tree gives depth five; all smaller paths attain the cardinality bound. The replay directly checked the supplied JSON and text data, rather than assuming the frozen Python generator had reread those files.

## originality

PASS

The concept classes are exactly path maximal-independent-set classes under the line-graph relabeling. The classical count and information ceiling are not new, and exact early dimensions and a static formula appear in related catalogue work. The inspected statements do not give the decisive adaptive depth-six obstruction at 15 or prove the exact first miss; this is the distinct claim.

## value

PASS

In a natural concept family indexed by path size, the cardinality bound is the benchmark for adaptive membership-query depth, and equality up to the first miss is not automatic. The exact cutoff at 15 edges distinguishes hypothesis counting from optimal realizable mistake depth. The short query-balance obstruction and explicit depth-five witness make the meaningful first failure independently reusable, rather than merely providing a finite table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
