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

A fresh exact implementation generated the open-neighborhood faces from the common-witness condition and checked all oriented Hasse covers. For n=6 it found 8620 faces, 4238 matching pairs and 41940 covers; for n=7 it found 136220 faces, 67723 pairs and 839580 covers. Both directed graphs are acyclic. The critical profiles are (1,0,1,142) and (1,0,1,772) with no further cells. Exact oriented cancellation from degree three to degree two reproduced the respective rows with 31(+2), 23(−2), 88(0), and 125(+2), 131(−2), 1(−4), 515(0). Indeed the signed Morse differential uses alternating paths through the matched 2-to-3 incidences, all unit pivots; unrelated dimensions are not needed for this row. Each degree row has gcd 2. The Morse CW model has a single 0-cell, no 1-cells and one 2-cell, so its 2-skeleton is S² and the attaching maps of 3-cells are determined by their degrees. A unimodular change on the wedge of attaching 2-spheres is realized by a homology equivalence of simply connected CW complexes, hence a homotopy equivalence. Its cofiber gives the degree-two Moore space plus 141 or 771 free S³ summands. At n=5 the independently checked profile is one vertex and eleven 3-cells; at n=4 the graph is K4 and the complex the boundary of a tetrahedron. This establishes the asserted first two occurrences in the finite range, not a map between the two cases.

## originality

PASS

The distinguishing contribution is the integral homotopy classification in the two first tetrahedral parameters, especially the n=7 Moore summand and its 771 three-spheres. A later catalogue record gives the identical n=6 answer only. Earlier rank-two triangular computations and same-day closed-neighborhood or rank-two models do not supply the n=7 result or a broader theorem covering both.

## value

PASS

This is a natural graph family and the first torsion boundary is a meaningful finite cutoff. An integral homotopy type at both first tetrahedral parameters, rather than field Betti numbers, determines whether the attaching maps give an actual Moore-space summand and records the exact free sphere counts. The n=7 case remains distinct even accounting for the later n=6 overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
