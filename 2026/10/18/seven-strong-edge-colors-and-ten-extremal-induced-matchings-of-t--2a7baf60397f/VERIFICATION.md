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

The repaired claim is exact strong chromatic index 7. A conflict between distinct duad–syntheme flags is exactly either cross-membership, including when they share an endpoint. The complete 45-entry coloring in repairs/1/RESULT.md passed its self-contained check of all equal-color edge pairs after reconstructing the canonical list; the proof uses the published six-color obstruction. Independently, the fresh standard-library replay /workspace/branches/24c45266-cb6b-47b6-8e5c-b64957ac6274/reproduce_tutte_coxeter.py and its .out.json regenerated the full 30-vertex, 45-edge instance and all induced matchings: (45,720,5160,16920,22680,8520,720,90,10), with maximum size nine. Every size-eight class has a unique parent, two maxima meet in one edge, and no edge lies in three maxima, so with no nine-class at most two eight-classes fit into six, covering at most 44 edges. With a nine-class at most one eight-class fits: two disjoint eights would have to omit their intersections with the nine-class, yet still share their parents' mutual intersection. The sole six-color profile is then (9,8,7,7,7,7). Each of the 90 ordered parent pairs leaves 32 candidate sevens, and fresh exhaustive tests found no cover by four. The frozen mathematical assertions therefore also check out; the repair addresses coverage, not a false enumeration. Frozen scripts and recorded outputs were inspected, not run. No conclusion for a larger family or list-coloring follows.

## originality

PASS

For the frozen combined contribution originality fails in part: the matching census and incidence classification are covered by the earlier partition classification or direct consequences of it, and the six-color obstruction is published. The repaired claim retains only the independently checkable seven-color upper bound yielding the exact index, with both overlaps credited. The strongest inspected primary passage offers only non-six-colorability and a conjectural general seven-color upper bound. Neither the distinct Resultary matching records nor the inspected published comparisons establish the seven-color upper bound. This PASS is for the repaired claim only.

## value

PASS

The repaired result computes a natural invariant of the canonical cubic girth-eight cage, singled out as a six-color obstruction in the literature. An explicit seven-coloring resolves the exact value needed to compare that obstruction with the broader seven-color conjecture. This is useful without claiming a general upper bound or counting the already-covered matching design as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
