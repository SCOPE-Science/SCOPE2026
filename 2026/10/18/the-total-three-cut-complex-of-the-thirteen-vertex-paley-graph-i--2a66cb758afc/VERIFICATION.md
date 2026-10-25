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

Define the total 3-cut complex by complements containing a 3-element independent set in the quadratic-residue Paley graph on F13, residues Q={1,3,4,9,10,12}. Independent enumeration found exactly 26 independent triples, 26 dimension-9 facets and 6,553 augmented faces with augmented vector (1,13,78,286,715,1287,1677,1469,780,221,26). Applying the provided stage pivots [0,2,4,12,6,3,7] reproduced 3,276 augmented matched pairs (one involving empty), one remaining critical dimension-5 simplex mask 4316, and full orientation of 39,156 Hasse incidences topologically sorted all 6,553 masks. Removing the empty match gives one critical vertex and a single critical five-cell; Forman yields the integral S5. Because this complex is pure dimension 9 yet has reduced H5=Z, a pure shellable complex would have top-dimensional wedge homology only, so it is not shellable. Independently reconstructed all 78 affine-symmetry reduced Lefschetz traces on faces: χ(a,b)=+1 for a in {1,3,9}, −1 for {4,10,12}, independent of b; a^3 mod13 equals ±1 accordingly. The complex is total, not ordinary, and the character statement concerns this order-78 affine subgroup only.

## originality

PASS

Best-of-knowledge originality after reconstructed proof and actual published/literature search; an inaccessible or not-fully-inspected primary source is not a proof of noncoverage and remains a recorded risk. The checked earlier statements do not imply the exact final claim.

## value

PASS

P13 is a canonical strongly regular Paley graph outside the familiar chordal/cycle/complete-multipartite total-cut classification. The unexpected S5 homotopy for a pure 9-complex plus a nontrivial integral homology sign action supplies a natural exact benchmark and non-shellability witness, not a routine general-theorem substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
