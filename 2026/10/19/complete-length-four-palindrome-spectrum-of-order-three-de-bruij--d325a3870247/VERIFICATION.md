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

A palindrome abba is exactly a fixed point a of the diagonal successor permutation at bb. The loop bbb cannot follow itself in a tour of q³>1 edges, so at least two letters move at every bb. Conversely, when b moves, every edge entering bb from off the diagonal has a forced exit; just the entrance from σ_b⁻¹(b) first traverses bbb. These paths cover each diagonal incident edge exactly once. Along with the off-diagonal edges they form a balanced macrograph: the forced paths permute the off-diagonal exits at each b. The unchanged subgraph is the directed line graph of the complete loopless digraph, strongly connected even for q=2. Euler traversal and expansion therefore respect all prescribed transitions, including wrap-around. For each b, a cycle on q−f≥2 letters including b fixes exactly f letters, so summing the q independent choices gives every integer 0 through q(q−2). As a bounded independent calculation, audit_palindromes.py applies directed matrix-tree and BEST to the contracted graphs for every admissible tuple at q=2 and q=3, with the first macroedge fixed to be the one containing 000. It gives two binary cycles with no palindromes and the ternary counts 55296, 165888, 124416, 27648, totaling 373248. The proof, not this finite test, covers all q.

## originality

PASS

The binary constant-center obstruction and the fixed-point interpretation already occur in an earlier Resultary theorem; specializing to binary order three forces P=0 and leaves only the transposition at each diagonal vertex. The supported distinct part is the simultaneous realization for larger alphabets, where there are multiple choices at each diagonal vertex, and the resulting full arbitrary-alphabet spectrum. No inspected prior statement or implication settles that claim. Closely titled literature that was inaccessible remains an access risk, not evidence of noncoverage.

## value

PASS

The exact spectrum addresses a natural local-factor statistic on a standard universal-cycle family. More importantly, the realization lemma identifies the only obstruction to arbitrary diagonal transitions and supplies a constructive extension; merely finding tours at the two extremes would not give this control. The new value is in the multiple-choice alphabet regime, not the already known binary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
