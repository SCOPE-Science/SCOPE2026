---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The primary facet theorem says every maximal chain C with every sign epsilon defines the supporting facet sum_{v in C} epsilon_v x_v<=1, normal Euclidean norm sqrt(|C|); convex hull generators are the signed antichain vectors. A radius-r ball at center c fits iff max_epsilon(sum_C epsilon c)+r sqrt(|C|)<=1, equivalently sum_C |c_v|<=1-r sqrt(|C|). A longest chain bounds r<=1/sqrt(h), and the origin meets all signed inequalities at that radius; the center locus and uniqueness iff longest chains cover ground set follow from equality along longest chains and a small perturbation at any other coordinate. Centered tangencies are exactly 2^h per longest maximal chain. Every generator has squared norm at most w, with equality at maximum antichains; Euclidean convexity bounds the entire hull. Central symmetry and one antipodal max-norm pair force unique circumcenter 0 and R=sqrt(w). Strict Euclidean convexity makes the entire contact set precisely signed maximum antichain indicators; the count is 2^w per maximum antichain. Independently reconstructed boundary cases for chains and antichains; the finite supplied checker is corroborative.

## originality

PASS

The exact full Euclidean height-width radius, incenter-locus and contact classification are derived from prior enriched/unconditional chain definitions and signed facet theorem. Existing Resultary chain-polytope inradius applies to the ordinary nonnegative chain polytope with distinct coordinate constraints, while order/signed-order results apply to different convex bodies. No covering enriched-chain metric theorem found; best-of-knowledge with explicit risk of older unconditional terminology.

## value

PASS

The standard unconditional/enriched chain polytope is a natural reflexive combinatorial polytope, and the exact sharp Euclidean radii recover BOTH classical independent poset invariants height and width. The equality classifications distinguish center rigidity and contact combinatorics even for nonpure posets, supplying a reusable object-specific structural result. It is not an arbitrary tiny instance or merely a changed notation for the ordinary chain polytope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
