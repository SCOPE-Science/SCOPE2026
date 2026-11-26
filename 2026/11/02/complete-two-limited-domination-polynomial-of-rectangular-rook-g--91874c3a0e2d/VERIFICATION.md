---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The selected-cell constraint is r_i+c_j≤2, and domination forbids a full omitted row and column simultaneously. Without a full line every incidence degree is at most two. A row of degree two confines all omissions to its two columns; if both columns had extra omissions in different rows, a selected cross cell would see one row omission and two column omissions. Hence the only nonmatchings are the two-edge star, the 3-cell rectangle and the 4-cell rectangle, up to transposition. With a full row there can be at most two full rows, and any other row has at most one omission. Two full rows permit no extra omission; with one full row, two extra omissions in different columns violate the cross constraint, and in the same column give a nonfull column of degree at least three. Each surviving configuration satisfies both constraints directly. The families are disjoint for m,n≥4; the matching count chooses a bijection, each three-cell block has four choices, and the slab counts choose the indicated full lines and optionally one outside cell. The maximal exponents and their coefficients give the stated minimum and multiplicity, including the tied orientations on a square. Independent code testing rook adjacency directly in branches/38eca682-5783-4f93-b41a-da41a44cf453/independent_enum.py matched complete 4×4 and 4×5 histograms and classifications (553 and 1,036 feasible sets, with 12 and 6 minimizers); the proof handles all m,n≥4.

## originality

PASS

Credit is limited to the complete classification of feasible complements and their size polynomial. The rectangular minimum, the minimizing slab classification, and the exact counts of minimizers are already covered by Resultary 3f6b93fa9eef, not just by the previously noted 4×4 special case. They are valid corollaries here but not distinct contributions.

## value

PASS

The value is the rigidity of all feasible complements at the first capacity that permits nonmatching small components, and the resulting full size distribution. It reveals which nonextremal configurations are possible and distinguishes coincident powers arising from different shapes. This is materially stronger than the known optimum and covers a natural infinite graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
