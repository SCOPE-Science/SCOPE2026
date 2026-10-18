---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification of the eight-net incidence theorem

The claim is proved geometrically in `RESULT.md`; the following checks are independent finite reproductions, not independent external validation.

Run from this directory:

```sh
python3 verify_coefficients.py > coefficient_output.replay.txt
python3 verify_geometry.py > geometry_output.replay.txt
cmp coefficient_output.txt coefficient_output.replay.txt
cmp geometry_output.txt geometry_output.replay.txt
```

The first script enumerates 63 nonzero binary ternary conics; checks the exact characteristic-two smoothness discriminant and all 2D and 3D all-smooth subspaces; and enumerates all 168 projective automorphisms to confirm net transitivity. It obtains 28 smooth conics, 56 smooth pencils, eight nets, the 28 pairwise one-conic intersections and stabilizer order 21.

The second script implements \(\mathbf F_8=\mathbf F_2[t]/(t^3+t+1)\) independently; constructs its 73 projective points; confirms 22 degree-three Frobenius orbits, with 14 collinear and eight noncollinear; independently checks all 28 smooth conics for absence of singular points; and establishes the two-net incidence and unique-pencil correspondence with the rational base point. Absence of geometric singularities is established by the proof, not inferred solely from points over \(\mathbf F_8\).

No complete independent audit was performed. Comparison with inaccessible archival literature has a residual priority risk, described in `AUDIT.json`.
