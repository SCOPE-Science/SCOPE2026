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

Distinct-word violations are exactly the forbidden unordered triples; coalitions of size at most one cause no violations. Per coordinate an ordered target and parent pair satisfying descent has 15 assignments. Of the 15^3 ordered triples, 2*27^2-27 have the target equal to a parent; no distinct triple admits two different targets. Division by the two parent orders yields 972. Increasing-index enumeration visits each feasible set once because feasibility is inherited by every prefix. Checking additions from the entire 27-word universe, not just later indices, certifies inclusion-maximality. A separate implementation reproduced all feasible ranks (1,27,351,1953,4455,4482,2439,756,108,12), total 14584; maximal ranks 3,4,5,6,7,9 had counts (27,162,540,27,324,12), total 1092. It checked the full 1296 coordinate and independent symbol permutations and obtained the nine stated orbit sizes; explicitly testing each feasible size-eight code gave exactly one valid addition for each of the 108 codes. Replay: /workspace/branches/ca789421-95bb-4523-a1ac-0e77f1845ec6/independent_census.py and independent_census.log in that directory. The uploaded Python and C++ verifiers were inspected, not executed. As an analytic check of the size-eight extension, if a feasible pair differs in one coordinate, any other word must have the third symbol in that coordinate (else one of the pair can be framed). At this fixed symbol, the two remaining coordinates give a bipartite graph on 3+3 vertices with no three-edge path, hence a star forest with at most four edges. Such a code has size at most six. A feasible size-eight code is therefore a partial Latin square with one hole. The deficient row and column both need the one symbol used only twice; it fills the hole uniquely, yielding a distance-two code and thus a two-frameproof code at length three.

## originality

PASS

The supported distinct claim is the full inclusion-maximal saturation polynomial and orbit census, especially the non-maximum strata. The exact size-nine coefficient and its one orbit already occur in the inspected equality-case record and are not credited as novel. The one-hole extension fact is not needed as an independent novelty claim. The older literature comparison is bounded and the inaccessible sources leave the named residual risks.

## value

PASS

This is a natural smallest ternary length-three extremal-code setting with known maximum configurations. The counts address a distinct practical and structural question: where greedy codeword addition can stop, and how many symmetry types those terminal codes have. The spread from size three to nine, absence of terminal size eight, and the nonmaximum orbit breakdown supply precise useful data rather than merely recomputing the maximum. The finite scope is complete and transparent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
