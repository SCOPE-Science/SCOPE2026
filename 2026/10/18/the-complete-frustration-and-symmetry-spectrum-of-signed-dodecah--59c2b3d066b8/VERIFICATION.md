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

The boundary map sends a primal edge to the two incident faces, and is the binary incidence map of the connected dual. Its image is the even masks and its kernel has dimension 30−11=19, exactly the dimension of the contained primal switching-cut space. Thus its fibers are precisely the switching classes, and minimum signature size is minimum dual T-join size. Pairing the odd ends of trails gives the distance-sum lower bound; taking the symmetric difference of shortest paths realizing a pairing gives the upper bound. The full automorphism action on the face masks is that of the dual icosahedron: uniqueness of the spherical embedding of the 3-connected primal identifies the action on faces, and the 20 dual triangles are facial and allow the dual automorphisms to induce primal ones. The bound of 120 follows by specifying the image of a directed edge and an incident triangular face, then propagating across adjacent faces. Independently ran `python3 /workspace/checks/2.py /workspace/source/2026/10/18/the-complete-frustration-and-symmetry-spectrum-of-signed-dodecah--59c2b3d066b8`. A min-plus induction over the 30 distinct edges takes or skips each edge once, tracking minimum size and multiplicity for each syndrome, independently of the uploaded BFS/pairing programs. All 2,048 computed rows agreed with the frozen CSV. The exact histogram was (1,30,315,1058,577,66,1), with all negative-face-weight strata verified and mask 4095 the only one with minimum 6. A separate permutation backtrack found all 120 adjacency automorphisms. Frustration-weighted Burnside gives (1,1,7,20,13,3,1), and the independent maps also verified the 46 frozen representatives and orbit sizes. The full mask has exactly 125 optimal edge subsets; with degree odd at all twelve vertices and total degree twelve, their degrees must all be one. Conversely every perfect matching gives such a subset; the odd facial signs are exactly those of the all-negative primal signing. This is exhaustive for the specified graph only. Both frozen programs, transcript files and CSVs were inspected as evidence; no frozen script was executed or rewritten.

## originality

PASS

Best-of-knowledge pass for the exact dodecahedral frustration distribution and negative-face refinement, its full-symmetry refinement by frustration, and the resulting unique maximizing switching class. Credit prior switching/cut-code theory, the maximum six, ordinary symmetry enumeration machinery, and independently available icosahedral perfect-matching count 125; none is an independent originality basis here. The minima-to-perfect-matchings identification is the equality case in the T-join degree bound, not a new counting technique. No compared result gives the retained frustration-graded census or mechanically identifies the unique deepest coset without the graph-specific calculation. This is not a priority certificate.

## value

PASS

This is an exhaustive, frustration-graded switching-isomorphism classification for a canonical Platonic graph with its natural full symmetry group, not an arbitrary bounded slice. One needs the precise counts, rather than the old covering radius, to benchmark algorithms for minimum signatures, know how common near-maximal behavior is, or select representatives of all maximally frustrated classes up to symmetry. Separating face parity weight from optimum edge count also records when the trivial half-weight lower bound is not attained. The graph-specific, symmetry-graded data and unique extremal class are the useful retained facts, rather than the already-known maximum or a recomputation of the dual matching count. No generalization to other signed graphs is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
