---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Sparse paving rank r≥3 and corank≥3 has exactly the coordinate 2n facets plus one facet per circuit-hyperplane, by connected-flat facet conditions; the coordinate facets are active at all bases, and precisely t(B) hyperplane facets join them. The primitive normals live in N=Z^n/Z·1 and the signed coordinate rays span it saturately, giving torsion-free Cl(X)=Z^(n+h+1) and Cl(U_B)=Z^(1+t(B)). At every vertex n>n−1 rays make U_B singular and non-Q-factorial. Local rational Cartier equations require the unique sign vector a_i=1 for i∈B, −1 otherwise to descend, imposing n=2r; each active H pairs to r−2 so imposes t(B)=0 or r=3. The vector is then integral, hence rational Cartier iff Cartier, no finite nontrivial index. With h>0 some B has t>0; global criterion follows. Exhaustively recomputed Vámos 65 bases, counts t=0,1,2 of 17,16,32; 6 automorphism orbits sizes 1,16,16,8,8,16 with claimed t. These finite checks corroborate, but the universal proof rests on matroid facets and toric divisor sequences.

## originality

PASS

Feichtner–Sturmfels Proposition 2.6 and Joswig–Schröter Proposition 7 give matroid-polytope facet frameworks; Karn–Nasr–Proudfoot–Vecchi §5 states the specific Vámos 5 circuit-hyperplanes and D4×D4 automorphism generators but computes equivariant Kazhdan–Lusztig polynomials, not canonical normal-fan Cartier status. Hibi et al study Gorenstein semigroup rings and a classification in graphic matroids: semigroup-cone Gorensteinness must not be equated to local canonical Cartier status on a normal-fan projective variety. The frozen theorem supplies full arbitrary sparse-paving class-rank and Cartier criteria plus Vámos six-orbit distribution; the inspected primary sources do not logically cover that same result.

## value

PASS

This is a uniform classification of canonical Cartier/Q-Gorenstein behavior at all torus-fixed charts of a large natural matroid class, with a sharp n=2r and r=3 dichotomy, plus an exact nonrepresentable Vámos test case. Integral class-group ranks and no-Q-factorial consequences are natural singularity invariants that distinguish polytope geometry from matroid semigroup-ring conditions. Their application to a nonrepresentable matroid is not an arbitrary narrow calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
