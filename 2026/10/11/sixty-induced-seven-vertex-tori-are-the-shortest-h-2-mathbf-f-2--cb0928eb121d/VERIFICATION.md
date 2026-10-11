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
# Verification

`verify.py` uses only the Python standard library and reconstructs the fifteen-vertex three-torus from the six published cyclic tetrahedron generators.

It computes
\[
\operatorname{rank}\partial_2=88,\qquad
\operatorname{rank}\partial_3=89,
\]
hence
\[
\dim_{\mathbf F_2}H_2=3.
\]

Every vertex subset of size at most seven is exhaustively processed. The script constructs the full local \(2\)-cycle space and reduces each local cycle modulo the global tetrahedral-boundary space. All supports of size at most six have zero image. Exactly sixty seven-subsets have nonzero image, each of rank one.

For each minimum support the script verifies the induced face vector \((7,21,14)\), absence of tetrahedra, degree two at every edge, and a consistent orientation across all fourteen triangles. Thus all sixty supports are induced tori.

Their ambient homology classes, in the basis given by three displayed representative tori, have coordinates
\[
001,\quad010,\quad100,\quad111,
\]
each exactly fifteen times.

The script also verifies all \(120\) affine maps
\[
x\mapsto ux+v\pmod {15},
\qquad u\in\{\pm1,\pm2,\pm4,\pm8\},
\]
on the complete tetrahedron set. One affine orbit contains all sixty minimum carriers, and translations give a fifteen-element orbit inside each represented class.

Exact successful output:

`VERIFY_OK f=15,105,180,90 H2_F2_dim=3 min_vertex_support=7 supports7=60 all_supports_induced_orientable_tori=yes class_counts=15,15,15,15 classes=001|010|100|111 affine_auts_checked=120 support_orbit=60 translation_orbits=15_per_class`
