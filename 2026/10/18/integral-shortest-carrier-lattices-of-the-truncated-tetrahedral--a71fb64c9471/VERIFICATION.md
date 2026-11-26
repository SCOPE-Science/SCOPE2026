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

In a vertex-minimal flag complex with nonzero reduced H_d, deleting any vertex gives zero H_d, so the link has nonzero reduced H_{d−1}. The vertex is not a cone point. Inducting from d=0 gives at least 2d+2 vertices. At equality the link is the cross-polytope boundary and the deletion must fill a nonzero multiple of its fundamental cycle. Such a filling uses the only nonneighbor as apex, so every link facet has that apex, forcing the suspension. For d=3 in a matching complex the four nonedges of this octahedral complex correspond to intersecting graph-edge pairs; different pairs have disjoint endpoints and together use all twelve vertices. This yields exactly the spanning P3-factor classification once the classes are shown nonzero. The only graph triangles are the four first-coordinate triples, since reversal edges are a matching between them; permuting these triples determines every vertex, and each symbol permutation acts. A separate exact integer calculation from the full boundary maps, using unimodular Smith decompositions rather than the supplied discrete-Morse verifier, reproduces the face vector (18,117,332,390,144,8), integral H3=Z^22, all 111 cycles with coordinate gcd 1, and unit determinant for the stated 22 columns. It reproduces S4 orbit sizes (12,12,24,3,24,6,24,6), ranks (8,11,14,3,13,6,16,6), each saturated, and the generating pairs (1,6),(2,6),(5,6),(6,7). The 19 full-rank triples all have unit Smith factors except for one final factor 2 for (3,4,6). See /workspace/branches/63a6cbee-f07e-47b4-9d39-6b1d1d969cab/independent_lattice_replay.py and independent_replay_output.txt. The source Morse description is consistent: reverse the matched covers in the full face poset; cancellation of a matched degree-(3,4) pair replaces the pivot by the other faces with the stated unit-coefficient signs, and the verifier checks all degree-four boundaries. No uploaded program was executed.

## originality

PASS

The distinction is the exact minimum-support integral lattice of the specified directed-pair graph, including the exceptional full-rank but index-two selection of symmetry orbits. The ordinary 22-sphere homotopy type is already covered. The strongest indexed analogue treats the Dürer graph rather than the truncated tetrahedron and has materially different carrier and parity data.

## value

PASS

This is an intrinsic finite problem on a standard polyhedral graph: the least induced supports detecting nonzero integral degree-three classes, and how their symmetry classes generate. The exact support classification and specified basis are usable at the chain level. In particular the unique index-two triple among rationally generating triples is an explicit obstruction to extrapolating integral generation from rational span or a sphere count. The choice of invariant is natural independently of the numerical computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
