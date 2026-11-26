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

For three distinct anchors, the full signed product sums to q minus the sum of three sign-pair products plus the signed cubic character sum. The two-factor sums are −1, the linear sums vanish, and the squarefree cubic defines an elliptic curve with Hasse bound 2√q. At the anchor vertices the omitted factors contribute at most 12 total. Thus 8N≥q−15−2√q>0 for all q≥27, including proper prime powers. My independent exact prime-field replay used Euler's criterion and intersections of incoming/outgoing neighborhoods. It checked all eight patterns on each of 969 and 1771 triples at q=19,23, and all four patterns for each pair at q=7,11. Four (respectively three) game rounds then require no more than three (respectively two) existing anchors; repeat choices are mapped to repeat choices. The replay confirmed a transitive triple first at q=7, a transitive four-set first at q=11, and no common in-neighbor of {0,1,3} at q=11. The latter sentence holds throughout the three-extension tail. The degree-sequence census confirmed all four isomorphism types at q=11 (55,55,55,165), but only three at q=7 (7,7,21); all types extend from triples in the tail. Labeled diagrams with identifications reduce to these induced types and their subdiagrams, proving existential-prenex agreement. The explicit forall-forall-forall-exists formula, notwithstanding the stray 'existential' label in the proof's Step 3 introduction, has rank four and separates the last two classes. The bound on representatives is within the stated family. Independent finite replay: /tmp/opencode/paley_review.py; the infinite portion is the character estimate plus the game, not a replay extrapolation.

## originality

PASS

Credit the earlier prime-order extension threshold and its immediate rank-four tail implication. The exact partition of the prime-power family, including the small classes and the 11-versus-19 existential-prenex gap, is distinct on the inspected evidence. A closely overlapping later-dated Resultary item covers the tail even for unrestricted-depth four-variable logic but does not state the small-class or fragment partition.

## value

PASS

The useful contribution is the precise classification and the sharp detectable difference between bounded-rank logic and its existential-prenex fragment, not a new claim of 3-e.c. at the known threshold. T11 already suffices for every four-variable existential-prenex witness in the family tail, yet no family member below T19 can represent all rank-four sentences there. That gives different, provably minimal finite tests for two natural classes of questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
