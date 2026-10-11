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

`verify.py` embeds the complete forty-tetrahedron presentation and uses only the Python standard library.

It reconstructs
\[
f=(11,51,80,40)
\]
and computes
\[
\operatorname{rank}\partial_2=40,\qquad
\operatorname{rank}\partial_3=39,
\]
so
\[
H_2(K;\mathbf F_2)\cong\mathbf F_2.
\]

For every vertex set of size at most six, the verifier constructs the complete local \(2\)-cycle space and reduces it modulo the global tetrahedral-boundary space. The exact support counts for sizes \(1,\ldots,6\) are
\[
0,0,0,0,0,20.
\]

Each of the twenty six-vertex carriers is checked to have \(15\) edges, \(10\) triangles, no tetrahedra, edge degree two, cyclic vertex links, and Euler characteristic \(1\). Hence every carrier is an induced six-vertex \(\mathbb{RP}^2\).

The verifier also exhausts the full simplicial automorphism group and obtains order \(48\). Its action on the twenty carriers has exactly two orbits of sizes \(12\) and \(8\).

Exact successful output:

`VERIFY_OK f=11,51,80,40 H2_F2_dim=1 min_vertex_support=6 carriers6=20 all_carriers_induced_RP2=yes aut=48 carrier_orbits=12,8 reps=23451011|23491011`
