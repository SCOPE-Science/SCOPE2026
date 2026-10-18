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

# Reproducible finite verification

The files `verify_rhombicuboctahedral_euclidean.py` and `rhombicuboctahedron_certificates.json` are complete and self-contained; run `python3 verify_rhombicuboctahedral_euclidean.py` with Python 3 standard library. The program prints `VERIFY_OK` only after replaying every relevant certificate.

It constructs all 24 points exactly as coefficient pairs in \(\mathbb Z[\sqrt2]\), and checks the seven squared-distance shells and their multiplicities. Clique enumeration confirms the face vectors \((24,48,8)\), \((24,84,80,18)\), \((24,132,248,186,48)\), \((24,180,576,906,744,304,48)\), and \((24,216,944,2202,2904,2236,960,192,8)\). It checks the closed connected triangulated surface target: 24 vertices, 66 edges, 44 triangles, every edge in two triangles, every vertex link a circle, Euler characteristic two.

The 5,420 elementary collapse pairs are checked against the current face-poset cofaces and their remaining exact complexes, not merely pair counts: 8 to a 40-edge connected graph; 36 to the surface; 216 and 1,288 onto the included squared-radius-eight complex; 3,872 to a 1,942-face three-dimensional complex. Every one of the 36 new edges at the fifth stage has a verified triangular replacement path through older edges. Graph-distance second and third powers are compared against the exact Euclidean stages for all 276 vertex pairs.

Finally the signed integral third boundary, with 944 rows and 758 columns, is reconstructed from the reduced complex; 751 recorded pivots are confirmed to be units and each row/column elimination is performed over the integers. The final matrix is zero. The proof in `RESULT.md` explains why these checks imply integral homotopy groups and the wedge of seven three-spheres. No computation is extrapolated outside the finite configuration. Independent audit has not been performed.
