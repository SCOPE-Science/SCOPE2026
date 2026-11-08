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

All graph edges and matchings are fully specified; an independent face enumeration reproduced f-vectors (9,18,4), (12,42,44,9), (15,75,145,95,11), (18,117,336,420,192,20) for n=3..6 and mod-two Betti ranks (1,6), (1,0,4), (1,0,2,2), (1,0,0,12). The inspected complete standard-library verifier constructs matched Hasse incidences and topologically sorts them to certify acyclicity. Its explicit critical profiles give n5 five 2-cells and five 3-cells with signed integral differential rank3 and a unit 3x3 determinant -1, and n6 13 3-cells and a 4-cell with primitive coefficient vector (1,1,1,0,...). Since the lower positive skeleton is a wedge of 2- or 3-spheres, the homotopy attaching classes are entirely determined by these integer degrees (pi_m of wedge S^m=Z^k), allowing cancellation and specified wedges. No general n>6 assertion. Source code path verified against exact tree and independently inspected; no claim that my separate mod2 check independently recomputed signed Morse entries.

## originality

PASS

Agarwal–Basak full preprint for exactly the circular-ladder family classifies graph-vertex independence and PERFECT matching complexes, and its Problem26 explicitly asks for the ORDINARY matching complexes. Bayer–Jelić Milutinović–Vega Theorem13 applies to open strings of polygons, not closed cyclic prism. Matsushita and Braun–Hough cover open rectangular ladders. The exact n=4 cube wedge is acknowledged as known baseline. Indexed hexagonal-prism three-cut and open-six-rung matching computations use different simplicial complexes or graphs and do not imply n5/6. Thus n5/n6 complete integral homotopy are additional exact facts despite finite scope.

## value

PASS

Ordinary matching complexes for circular ladders are explicitly identified as a missing natural family in the 2026 primary paper. The first mixed-dimensional wedge at n5, disappearing at n6, is a meaningful finite cutoff, and the contrast with the contractible perfect matching subcomplex at n5 exhibits structural topological sensitivity to the face definition. These exact homotopy classifications are useful beyond numeric Betti recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
