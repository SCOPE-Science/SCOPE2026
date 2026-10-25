---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The ordinary matching complex of P4 square P4 has 24 graph edges and 10012 augmented faces with counts (1,24,224,1044,2593,3388,2150,552,36). Independent endpoint-disjoint enumeration reproduced all counts and exact F2 boundary rank checks, corroborating H4 dimension6 and H5 dimension2. Examined full verify_equivariant.py integral signed differential, elimination formula and inclusion/projection chain maps: 5002 unit pivots leave exactly six degree-four and two degree-five generators with zero residual differential. Source verifies each lifted generator is an original cycle and reprojects correctly, then obtains exact 8x8 induced dihedral matrices and all relations; character in order (1,r²,r,h,d) is H4=(6,2,2,0,-2), H5=(2,-2,0,0,0). Independently enumerated signed invariant matching faces for every D4 symmetry, checking the alternating *reduced Lefschetz* values χ4−χ5=(4,4,2,0,-2) by class, careful with augmented empty-face negative sign. Character orthogonality gives H4=A1+2A2+B1+E, H5=E, and rational transfer on barycentric subdivision gives exactly one quotient H4 invariant. No integral quotient torsion asserted.

## originality

PASS

Published 4x4 Cartesian matching complex wedge^6 S4∨ wedge^2 S5 (same object) establishes nonequivariant ranks, not the dihedral module. Matsushita (2019) handles small-width strips, 3-row reflection work has smaller geometric group and different graph, and the published 4x4 D4 three-cut result has the same group but is a different complex. None imposes the degreewise rational homology characters or distinguishes horizontal from diagonal reflections here. Public search yielded no prior equivalent exact full D4 matching character; hidden computations remain a risk.

## value

PASS

The 4x4 square grid is a canonical small genuinely two-dimensional Cartesian grid with full quarter-turn symmetry. Its mixed-dimensional sphere-wedge homology has two distinct D4 representations, and separating axis/diagonal reflection and identifying the one surviving quotient class is natural geometric equivariant topology, not derivable from Betti ranks. Finite exact object is motivated despite no infinite strip theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
