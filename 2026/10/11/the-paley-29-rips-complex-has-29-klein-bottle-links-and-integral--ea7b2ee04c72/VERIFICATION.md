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

# Reproducibility and exact checks

Run `python3 verify.py` in a directory containing the supplied file. Only the Python standard library is required. The program itself reconstructs all finite combinatorial sets and does not load recorded outputs or external paths. It prints `VERIFY_OK` only if all assertions succeed.

The checks include all 29 field residues, the graph's strong regularity and diameter; exhaustive clique enumeration with face counts \((29,203,406,203)\); absence of five-cliques; exactly two tetrahedral cofaces per triangle; connected and nonorientable tetrahedral dual; all 29 vertex links being connected, closed, nonorientable triangulated surfaces of face vector \((14,42,28)\); all 203 edge links being six-cycles; integral elementary unit-pivot reduction of the 175 non-tree-edge coordinate presentation for \(H_1\); and independent binary boundary ranks \((28,175,202)\).

The integral \(H_2\) torsion follows from the explicitly proved signed-dual-incidence Smith-form lemma. The standalone code verifies every hypothesis for this lemma, and does not assert that modulo-two ranks alone prove torsion. The coefficient-field barcode is deduced from the exact integral groups and the verified diameter-two metric.

Expected leading output:

`VERIFY_OK vertices=29 edges=203 triangles=406 tetrahedra=203 triangle_degrees=2 dual_connected=yes dual_nonorientable=yes vertex_links=29_Klein_bottles edge_links=203_C6 unit_d2_pivots=175 mod2_ranks=(28,175,202) H0=Z H1=0 H2=Z^28+Z/2 H3=0`

The second output line reports one concrete orientation conflict between oriented tetrahedra. The calculation is finite and exact; no all-parameter extension and no independent audit are claimed.
