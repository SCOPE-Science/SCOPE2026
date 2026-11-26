---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The one-gap circle has exactly one zero run of length q+s-1; the others have length q-1. The coverage of 1 is the set O of ones, and that of 0^q is the long run R. Each of 10^q and 0^q1 has a unique occurrence covering respectively the last 1 and first q long-gap zeros, and the last q long-gap zeros and initial 1. Any zero-only factor can slide across R, covering every position in it in some occurrence. A factor containing either boundary witness covers the respective witness interval. Every other factor with a 1 has h consecutive regular-spaced ones and at most q-1 zeros on either flank; sliding its block of h ones over the m displayed ones gives valid occurrences that collectively cross every member of O, including at a cyclic flank. Thus every factor-coverage set contains one of the four witness sets, and intersecting all four is necessary and sufficient. Since O and R are disjoint, a pair must choose one from each; the boundary intervals impose exactly the two implications on j,t. The endpoint ones each allow q zero choices, and each of the m-2 interior ones allows max(q-s+1,0). This also proves attainment and covers q=1, m=2, s=1 and s>q without assumptions about nonempty regular gaps or an irredundant set of four tests. The proof establishes the infinite claim; checker.py and its output were inspected, not executed. In that code the attribution to all pairs relies on the prior mask-containment test, rather than independently testing each pair on every factor.

## originality

PASS

The reviewed circular literature provides the framework and related checking and consecutive-position results. Exact Resultary analogues under linear occurrences or three distinct circular gaps do not establish either the all-subset four-witness reduction or the all-minimizer census in this one-gap family. The possible Sturmian overlap at s=1 is not credited as a new scalar bound; the result here includes all optimal pairs and the arbitrary-marked-set test and works when s>1. No exact prior theorem or mechanical implication was established in the bounded evidence.

## value

PASS

All-optimal-position counts distinguish circles with the same minimum size. The proof identifies four coverage constraints that suffice for any marked set, not merely a faster check of candidate pairs. It quantifies the effect of a single nonperiodic gap in a natural family: interior ones stop participating above the gap threshold while endpoint choices remain. This structural and counting result goes beyond exhibiting one pair or rechecking a finite catalogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
