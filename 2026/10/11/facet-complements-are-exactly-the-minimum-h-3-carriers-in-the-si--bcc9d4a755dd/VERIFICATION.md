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

`verify.py` uses only the Python standard library and reconstructs the complex from the two published facet representatives and the two published permutation generators.

It obtains a group of order \(720\), exactly \(150\) facets, and face vector \((16,120,330,375,150)\). Exact mod-two elimination gives
\[
\operatorname{rank}\partial_3=225,\qquad
\operatorname{rank}\partial_4=149,
\]
hence \(\dim H_3=1\).

Every one of the \(8008\) ten-vertex subsets is tested for a local three-cycle surviving modulo the global four-boundary space; none survives. Every one of the \(4368\) eleven-vertex subsets is then tested. Exactly \(150\) survive globally, and their set is checked to equal exactly the complements of the \(150\) facets.

For each of those \(150\) complements, local chain ranks give one-dimensional \(H_3\), and the surviving local class maps nontrivially to global \(H_3\). Each of the other \(4218\) eleven-vertex induced subcomplexes is checked to have zero local \(H_3\).

Finally, the full published \(S_6\) action is applied to the \(150\) carriers, yielding orbit sizes \(30\) and \(120\) and the two stated representative face vectors.

Exact successful output:

`VERIFY_OK f=16,120,330,375,150 H3_F2_dim=1 min_vertex_support=11 supports11=150 facet_complements=yes other11_local_H3=0 S6_order=720 support_orbits=30,120 rep30_f=11,55,92,52,4 rep120_f=11,55,95,58,7`

All finite ranges used by the claim are exhausted.
