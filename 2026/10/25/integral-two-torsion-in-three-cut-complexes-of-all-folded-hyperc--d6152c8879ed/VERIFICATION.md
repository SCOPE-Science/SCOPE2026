---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Checked precise Alexander-dual face predicate: 0/1-simplices complete; triangles correspond exactly to connected graph triples (induced 2-paths); tetrahedra to induced squares; no 5-vertex dual faces by triangle-free Mantel bound. For n≥5 the antipodal quotient of Q_n has unique common-neighbor square completions, so each square tetrahedron collapses along a unique triangle and then a free diagonal edge, leaving the square-filled graph plus b far-distance edges. Its square-filled subcomplex is the 2-skeleton of the cubical CW quotient of the n-cube boundary by the free antipodal map, homeomorphic to RP^(n-1). Consequently H1=Z/2, H2=Z^h where h=2^(n-4)(n^2−5n+8)−1, and adding b far edges gives H1=Z^b⊕Z/2. Integral UCT places the Z/2 Ext class in H², while duality shifts it to H~_{N−5}(Δ3), alongside free H~_{N−4}=Z^b. Independently checked n=5 N16 q40,b0,h15, and n=6 N32 q120,b160,h55. Infinite n follows from the covering-space and collapse argument, not these finite samples.

## originality

PASS

The genuine ordinary three-cut edge-disjoint-square theorem is close but its hypotheses fail for folded cubes because each cube edge belongs to n−1 squares. General cut-complex papers study different graph families; published folded-cube square Čech and neighborhood results share projective 2-skeleton geometry but not the same Alexander-dual predicate. The full integral ordinary Δ3 theorem survives best-of-knowledge with a risk of stronger square-complex or Stanley–Reisner formulations.

## value

PASS

A uniform infinite family of highly symmetric folded cubical graphs has integral next-to-top torsion and complete explicit free ranks, yielding nonshellability at every n≥5. The proof explains the exact Z/2 obstruction through a projective-space 2-skeleton and integral UCT rather than ad hoc finite computations. This structurally motivated classification is not a routine special case of the edge-disjoint-squares theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
