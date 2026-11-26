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

PASS for the corrected RESULT.md in /workspace/repairs/3/ only. The frozen headline asserted completeness by the two local degrees, but its membership proof covers only cubic bipartite incidence elections with k equal to the shore size; the score-equality test is not valid on the degree-only domain. Even a simple cubic incidence graph can have no perfect matching, e.g. join a new central vertex to each subdivision vertex of three disjoint copies of K4 in each of which one edge was subdivided. Each five-vertex component would force its attachment edge into a perfect matching, which is impossible at the center. Also, the cited wider winner-determination theorem uses nonnegative, nonincreasing marginal weights, not every utility satisfying the two strict inequalities. This is a scope/membership gap, not a proof of nonmembership. The repaired family is recognizable in polynomial time. Independently checked the sharp score argument: every local score is at most c times the selected degree, strictly below it for degrees two and three, while the total selected degree is 2n; equality means all 2n degrees are one. Hall's condition follows by cubic edge counting, so this equality is attained. The exact one-to-one reduction and guessing each incidence subset once with the degree-one test establish hardness and membership with the known optimum. The repair specifies polynomial-time Turing hardness and keeps parsimony only for the graph-to-election map. The simple-graph convention is harmless even with a multigraph source: the added K3,3-minus-edge gadget has four completions with neither attachment used, two with both used, and zero with only one by bipartite balance. Replacing every edge gives the same factor 4^(M−n)2^n for every original matching, and all degrees and simplicity are preserved. Inspected CHECK.py and VERIFICATION.md without executing the supplied script; their finite rational diagnostics support the score claim on the same subclass.

## originality

PASS

The surviving claim is completeness on cubic bipartite incidence elections, with a fixed explicit optimum and an exact winner–perfect-matching correspondence throughout the stated utility family. This credits the known incidence encoding, the known counting source problem, and available single-winner algorithms. No inspected theorem supplies that exact optimum-counting classification on the specified family.

## value

PASS

The repaired theorem exhibits a meaningful search-versus-counting separation on a natural class of approval profiles where an optimum can be found by matching and the score is known from the input size. Hardness is attributable to ties, not to searching for or certifying an optimal score, and persists across the indicated utility family, including PAV. The bounded degrees and exact matching characterization are independently useful even though the proof is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
