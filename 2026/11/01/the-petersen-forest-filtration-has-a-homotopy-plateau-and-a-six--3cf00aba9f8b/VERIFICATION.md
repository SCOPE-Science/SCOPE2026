---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Independently constructed KG(5,2) on the ten 2-subsets of [5] and classified all 1024 vertex sets by induced acyclicity and degree bound. Exact face totals d=0,1,2,3 are 76,261,621,786 (empty included); deterministic vertex-toggle Morse reductions leave only critical cells {0:1,2:4},{0:1,3:1},{0:1,3:1},{0:1,5:6} with 35,129,309,389 pairs respectively, and all 170,860,2540,3470 Hasse incidences topologically sort. Since each reduced CW model has a point and only cells of one positive dimension, these give integral sphere wedges. The RELATIVE F2\F1 has exactly 360 faces, 179 acyclic relative toggle pairs and only two critical cells masks 538 (dimension3), 914 (dimension4); independent exact signed unit-pivot cancellation gives relative boundary -1, establishing zero integral relative homology. As both F1,F2 are simply connected, Whitehead gives actual inclusion homotopy equivalence; persistent groups and nonshellability of pure 5-dimensional F2 with H3=Z follow. No extrapolation to other cubic graphs.

## originality

PASS

Carnero Bravo introduced vertex-induced forest filtration and proves families such as paths, cycles and cactus graphs, not Petersen; previous Petersen Ind2=S3 covers only F1. This result adds F2, F3, actual inclusion and nonshellability not consequences of F1 or higher component-size Ind3, which has 381 versus F2 621 faces.

## value

PASS

A complete 4-stage classification of a natural filtration on the canonical noncactus cubic Petersen graph and a nontrivial inclusion equivalence distinguish persistence of homotopy from equality of homology ranks. The new nonshellable pure stage is a meaningful structural example, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
