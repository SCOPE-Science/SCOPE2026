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

I checked all six factor lists, multipliers, block lengths and ordered tail patterns against arXiv:2609.37056v1 Appendix A, including the two repeats of the parity coordinate at n=172 and the tail-free index-three core at n=189. The first block has f_1=1; the g*x^j there have strictly increasing degrees below m, proving full row rank. In a separate implementation I solved h*g=1+x^m from the constant term up, built each row by explicit coefficient convolution, and exhaustively combined the two halves of every message. A word lies in the hull exactly when its inner-product signature against all original rows is zero, equivalently when the signatures of the two halves match. This enumerates all words and all hull words without using the supplied checker, its Gram-nullspace reduction, or its Gray-code traversal. The parent (d,A_d) pairs matched Appendix A Table 3 in all six cases. The reconstructed Gram ranks were 4,18,1,2,0,1, inferred from the power-of-two cardinality of the zero-signature class. The resulting (n, hull dimension, hull distance, minimum-shell size) tuples are (172,17,68,1360), (173,2,104,3), (176,20,68,2992), (181,19,72,6358), (184,21,72,9826), (189,21,72,2394). In particular the n=184 hull equals the entire parent and its full weight census is doubly even. Replay from /workspace: python3 audit-work/5/hull_crosscheck.py 172 173 176 181 184 189; two bounded runs are recorded in audit-work/5/census-172-176.txt and census-181-189.txt. These are exact assertions for the six specified matrices, not all codes of the same parameters, and the record does not analyze n=200.

## originality

PASS

The parent distances and three numerical shell coincidences are already covered as parent invariants. Standard QC hull theory is relevant to the unaugmented cores, but neither the inspected table nor those general hull formulas gives the exact Euclidean hull subcodes' distances and multiplicities for these printed constructions. The supported distinct finding is the joint six-code profile, not simply recognizing that a doubly-even binary code is self-orthogonal.

## value

PASS

These are the six distance-record constructions presented explicitly via their QC polynomial descriptions, a motivated set rather than sampled lengths. The Euclidean hull measures the radical of their actual bilinear form; its dimension governs how many coordinates an LCD extension needs, and its exact distance and shell distinguish how much of the parent's distance profile survives that restriction. Four of the six hulls have codimension at most two, but the n=173 hull has codimension 18 and all three of its nonzero words have weight 104. The complete profile reveals both the coherent large-hull behavior and this exception. No hull subcode is asserted to improve a distance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
