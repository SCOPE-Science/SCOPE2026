---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Bipartiteness and diameter<=4 make every cross-color pair distance 1 or 3, and within-color pairs distance 2 or 4, so VR_<=3=A*B literally. With no 4- or 6-cycles, every same-color distance-two clique has a unique common opposite-color neighbor. Each factor A is the union of entire neighbor simplices intersecting pairwise in at most one vertex. Attaching a cone over each neighborhood simplex (contractible attachment) preserves homotopy and elementary collapses on the unique larger faces leave exactly the original incidence graph G. Therefore A and B each have reduced H1 rank b; join Kunneth gives H3=H1(G) tensor H1(G) free rank b² and the join-suspension equivalence gives wedge b² S³. Join interchange sign is (-1)^((1+1)(1+1))=+1. The canonical positive quadratic tensor C=sum_e pi(e)⊗pi(e), pi orthogonal projection of rational edge chains onto cycles, is nonzero when b>0 and invariant under signed edge permutations and tensor flips. Finite simplicial group rational averaging identifies quotient rational homology with invariants. Standard GQ point/line/incidence counts yield b=s²t² exactly. Independent C8 radius-three join calculation gives b=1 and rank-one third homology, a finite spot check rather than the proof for all graphs.

## originality

PASS

Two published primary mathematical records already give the order-(2,2) Tutte–Coxeter 256-sphere case and its natural S6 tensor-square representation; both are explicitly acknowledged as special cases. Those single-graph claims do not cover all finite diameter-four/girth-eight bipartite graphs, all (s,t) generalized quadrangles or full color-exchanging graph automorphism invariants. Earlier Adamaszek metric-gluing and incidence homotopy work concerns different constructions/thresholds. The novelty is the uniform graph-family structural theorem and full group invariant, not the 256-sphere example.

## value

PASS

The diameter and girth hypotheses are natural structural graph constraints. A uniform Rips homotopy classification, integral tensor module, and full-symmetry nonvanishing theorem gives a qualitative explanation for and extension of isolated generalized-quadrangle calculations. It applies to arbitrary finite generalized quadrangles, including nonclassical ones if they exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
