---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Reconstructed Petersen graph as KG(5,2), its fifteen graph edges and all 32768 edge masks; verified matching cardinality counts (1,15,75,145,90,6). Independently reproduced the specified 160-pair discrete Morse matching, topologically sorted all 975 directed Hasse incidences on the 331 nonempty faces, and obtained exactly one critical vertex, five critical 2-cells and five critical 3-cells. Independently computed the signed integral gradient-path boundary from all five critical 3-cells to all five critical 2-cells, finding an identically zero 5×5 matrix (not just zero modulo a prime). Thus Hurewicz π2=Z5 makes every S2 attaching map null and the integral wedge follows. For each of all 120 permutations in S5, independently computed oriented chain traces and the 79-dimensional im(d3) finite-field trace; prime1000003 > 2×79 gives unique integral trace lifts, yielding H2=sgn(g)·fixed_points(g) and H3=choose(fixed_points,2)+two_cycles-fixed_points. Their rational characters identify the two named modules; no claim about integral S5 lattice decomposition.

## originality

PASS

Mondal–Mukherjee–Saha study M_n=M(K_n), with M(K5) itself the Petersen graph; that is not M(Petersen), a 15-vertex 4-dimensional complex. Known Petersen 2-matching, Morse and cut complexes use distinct face conditions; outerplanar matching theorem does not cover nonplanar Petersen. The actual integral homotopy and full degree-split S5 character are not shown as covered.

## value

PASS

The Petersen graph is a highly canonical symmetric cubic graph. Identifying a mixed-dimensional integral homotopy wedge and distinguishing its two five-dimensional rational S5 homology modules supplies structural information beyond face counts and Betti numbers, and a reusable exact benchmark for graph matching-complex calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
