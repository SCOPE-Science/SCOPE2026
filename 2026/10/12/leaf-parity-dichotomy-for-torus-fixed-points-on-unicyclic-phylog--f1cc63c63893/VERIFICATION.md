---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Local tripod tetrahedron inequalities give 0<=all edges<=1 and full dimension. In fractional edge support every internal vertex has degree >=2 and at most one independent active equation; each tree component has at least two original-leaf endpoints and E>I, while a cycle-plus-tail component has E>I. Thus a vertex can be either wholly binary or fractional exactly on the unique cycle. At its cycle vertices, unit leg 0 forces neighboring cycle coordinates equal, unit leg 1 forces sum 1. Odd branch-leg parity uniquely forces all cycle coordinates 1/2; even parity leaves a free parameter and hence is not a vertex. Rooted trivalent binary propagation maps leaf assignments to branch leg values, yielding exactly two binary vertices per even leaf-parity assignment (2^n total) and one half-cycle vertex per odd assignment (2^(n-1)). Torus-orbit stratification gives complex Euler char 3*2^(n-1). The exact analytic proof supports arbitrary graph shape, with finite active-facet tests for three graph shapes used only as checks.

## originality

PASS

Buczyńska 2012 Theorem 2.33 gives an odd-cycle-leg parity condition for degree-two semigroup generators, but generators need not be polytope extreme vertices. Its deformation/Hilbert-function invariance does not imply an exact fixed-point count or leaf-parity fiber classification. Earlier Buczyńska–Wiśniewski treats trees; later phylogenetic-semigroup paper bounds generators. No stronger all-unicyclic Euler/fixed-point count located in Resultary or targeted literature. Novelty is only the classification of vertices and exact fixed-point count, not parity generators or local polytope equations.

## value

PASS

Torus-fixed-point numbers and ordinary topological Euler characteristic are natural geometric invariants of phylogenetic toric varieties. The complete combinatorial classification for every trivalent genus-one network is structurally useful and shape independent; it cannot be recovered from Hilbert series invariance alone. It is a motivated invariant rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
