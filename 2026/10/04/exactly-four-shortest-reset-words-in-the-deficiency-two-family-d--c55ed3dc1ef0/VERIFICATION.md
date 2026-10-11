---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The source lower-bound proof gives the complete equality budget: a shortest reset must enter the critical configuration after either \(ac\) or \(c^2\), every proper merge has length at least three, and between nonfinal merges at least \(n-3\) transport letters are needed. The source's complete minimum merge list shows the only length-three candidates are \(bcc\) and \(bca\); a nonfinal \(bca\) returns the merged coin to the wrong location and costs one extra transport step, so equality forces \(bcc\) at every nonfinal merge and \(c^{n-3}\) between them. The last merge can use either minimum option, yielding exactly the displayed four words. A fresh independent power-set BFS for \(5\le n\le10\) reproduced lengths \(10,17,26,37,50,65\), exactly four shortest words, and target split \(2+2\).

## originality

PASS

The defining paper proves only the shortest length and exhibits one shortest word; it does not enumerate all equality cases. The later shortest-reset-word algorithm paper optimizes or finds a shortest word but does not state an all-optimal-word classification for this family. Fresh Resultary and web searches found no distinct statement of the four-word set or the exact two-target split.

## value

PASS

The result classifies every optimal synchronization control in an infinite extremal family, determines the only two reset targets, and shows the deficiency-two letter can appear optimally only at the boundaries. That is structural equality information beyond the known threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
