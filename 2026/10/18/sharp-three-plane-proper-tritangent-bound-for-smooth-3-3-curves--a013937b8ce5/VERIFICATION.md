---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The split quadric Q=P1xP1/F2 embeds by O(1,1), so a smooth (3,3) section has canonical genus-four embedding. Exactly 15 rational planes correspond to nonzero 2x2 matrices: six invertible planes cut smooth (1,1) graph conics, nine rank-one planes cut the union of ruling lines. On an invertible graph, restrict a binary (3,3) equation to a sextic G; scheme-theoretic proper tritangency is exactly G=g² with a squarefree homogeneous binary cubic g (three odd sextic coefficient vanishing and projective gcd including infinity). For rank-one LM=0, the two restricted cubics must be M h1² and L h2²; h1(s),h2(u) nonzero ensures one ordinary doubled contact at the ruling-line crossing and one separate doubled contact on each ruling. This is stronger than merely even intersection and correctly excludes nonreduced contact supports. I wrote an independent GF2 polynomial/contact enumerator (different implementation from both supplied checkers), enumerated the complete 65,535 masks, generated all five split-quadric automorphism operations, enumerated 1,075 orbits and checked 4 affine Gröbner charts for each representative. Exactly 252 smooth orbits containing 16,020 equations remained; their proper-plane histogram is 0:10,656;1:5,022;2:324;3:18 and refined (graph,tangent) histogram [(0,0):10656,(0,1):2088,(1,0):2934,(1,1):252,(1,2):18,(2,0):72]. A unique 18-mask orbit attains 3, representative mask 10723 with (1,2) plane-type counts; orbit stabilizer 72/18=4. The two provided checkers were also read and independently implement full graph/rank-one contact with different filtering; finite exhaustion is complete because all possible coefficients and rational planes occur in the enumerated domain. The exact Gröbner unit-ideal criterion detects geometric smoothness over the algebraic closure, not just F2-point regularity.

## originality

PASS

Best-of-knowledge original exact proper *F2-rational plane* tritangent spectrum on the split genus-four quadric, refining the existing genus-four F2 curve census by a distinct contact invariant. Xarles (2020) fully enumerates genus-four isomorphism classes and lists point-count/zeta data, but its primary full text does not state the 15-plane proper-contact histogram, extremal orbit or refined plane types. Kulkarni–Ren–Sayyary Namin–Sturmfels (2017) work with real and complex tritangent planes, where all 120 geometric odd-theta tritangents are a different invariant: being geometrically a tritangent neither implies being defined over F2 nor having 3 distinct contacts in char2.

## value

PASS

Counting F2-rational *proper* tritangent planes of canonical genus-four split-quadric curves is a natural arithmetic contact invariant, not a random slice. The theorem supplies the sharp global bound three, the entire all-equations spectrum, and the unique extremal symmetry orbit with plane-type refinement. The finite census is a complete classification of a canonical degree-six geometric problem and is of legitimate mathematical value independently of a larger general-q theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
