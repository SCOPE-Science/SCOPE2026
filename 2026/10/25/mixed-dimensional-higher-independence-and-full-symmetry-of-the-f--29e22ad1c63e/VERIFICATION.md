---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For Q4 with sixteen bit-vector vertices, Ind2 consists of masks with every selected vertex having at most one selected neighbor. Independently enumerated all 65536 masks; 3055 faces including empty, with fvector (16,120,464,964,960,440,80,10) and reduced Euler -15. Independently reconstructed the sequential vertex-toggle matching: 1514 pairs, critical faces 17 three-cells, six four-cells and four five-cells; exact topological sort checked all 13584 directed incidences and found no cycles. Independently performed all signed integral Morse pair cancellations and recovered the exact two degree-four differentials ±([49158]-[49162]), the four critical five-cell boundaries, the rank-four unimodular minor -1, and d²=0, giving H3=Z^16,H4=Z and no torsion. The Morse CW has a primitive 3/4 cancellation and primitive 4/5 cancellation, with residual π4(wedge S3) components absorbed by changing sphere generators; hence an actual wedge of 16 S3 and one S4, not merely matching homology. Independently lifted the primitive 92-term simplicial four-cycle, verified its entire oriented simplicial boundary vanishes and computed its integral action for all 384 group elements; each agrees with sgn(S4), independently of the checked source script. Independently re-enumerated the orientation-weighted Lefschetz trace for all 384 B4 automorphisms: combining this with H4 sign recovered the asserted V⊕W degree-three character exactly. The claim concerns only Q4,r=2 and rational modules, not an infinite hypercube family.

## originality

PASS

Existing higher-independence theory defines Ind2 and classifies paths, cycles, complete multipartite, fully whiskered graphs and trees; its nonperiodic rectangular-grid question does not cover Q4=C4□C4 (a periodic toroidal grid). A previously published ordinary Ind1(Q4) seven-sphere wedge and other 4-cube cut/Čech complexes use different face predicates. The inspected primary family theorems do not imply this exact mixed-degree integral homotopy or B4 representation. Older Salvetti d-independence work was identified by DOI but only abstract could be inspected; that priority risk remains.

## value

PASS

The four-cube is a canonical highly symmetric sixteen-vertex graph. Its Ind2 complex is nonpure and has a genuinely mixed-dimensional integral wedge; the full 384-element rational B4 character and invariant subspace distinguish it from ordinary independence topology. An exact, fully computed homotopy and equivariant invariant for this natural small periodic grid can serve as a reusable benchmark without claiming an entire family formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
