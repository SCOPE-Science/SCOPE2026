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

I inspected the complete RESULT.md and the actual standard-library verify.py at the frozen source blob. The graph has 24 vertices and 37 edges. The checker builds every matching as a 37-bit mask; I independently reconstructed the monomer–dimer column-transfer dynamic program and obtained all 1,222,549 faces, with the exact claimed f-vector (37,584,5161,28191,99183,227262,335396,308330,165871,46801,5580,153) and reduced Euler characteristic -94. The source constructs a deterministic sequence of pivot-edge matchings on the entire nonempty face poset, checks disjoint pairing and exact counts 611,209 pairs/131 critical cells, and verifies acyclicity by a topological sort of all 8,827,379 oriented Hasse incidences. This is the crucial nonheuristic Morse hypothesis, not merely a count of critical cells. The remaining CW model has one degree-zero, 112 degree-seven and 18 degree-eight critical cells. The gradient-path recursion defines the signed 112x18 integral differential; the specified 182-entry ±1 matrix admits 18 unimodular unit pivots, hence primitive image and zero degree-eight homology. As the 7-skeleton is a wedge of 7-spheres and Hurewicz isomorphism identifies all 8-cell attaching maps with their integer degree vectors, the unit reduction cancels 18 sphere pairs, leaving 94 S7 wedges. The nontrivial million-face Hasse/Differential certificate code was read and evaluated logically, not fully re-executed in this environment; the independent exact f-vector check is narrower than the full homotopy theorem. No generalization to arbitrary widths is inferred.

## originality

PASS

The withdrawn Goyal–Shukla–Singh full-family wedge-of-spheres theorem is explicitly retracted and cannot serve as decisive validated prior coverage. Chauhan–Sharma–Shukla arXiv:2609.27366 (Sept 2026), with exactly the 3xn graph family, does prove vanishing ranges, nonzero degree n-1, and connectivity according to its accessible abstract, but that does not imply a full integral homotopy classification and precise width-eight 94-fold S7 wedge without attaching-map control. The highly relevant complete 2026 paper could NOT be read: arXiv/OA access failed, authorized Oxford access reported vpn_disconnected; this is explicitly a residual possible-coverage risk rather than a fabricated whole-paper NOT_COVERING or automatic FAIL. Related Resultary 4x4 grids and other Morse complexes are different dimensions/objects. Best-of-knowledge O passes only for the stronger exact width-eight homotopy classification; if the inaccessible source already gives an equivalent width-eight theorem, this should be revised.

## value

PASS

The exact integral homotopy type of a canonical 3xn grid at n=8 is a natural finite classification and sharp test of whether the ordinary matching complex is a single-degree sphere wedge. A complete acyclic matching plus primitive attaching differential resolves information that connectivity or Betti data alone cannot provide, particularly after a claimed general wedge classification was retracted. It is independently useful as a width-eight benchmark; no paper-sized or all-width theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
