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

The finite certificate uses exact arithmetic in \(\mathbb Q(\sqrt5)\). Write
\[
\varphi=\frac{1+\sqrt5}{2},
\qquad
\varphi^2=\varphi+1.
\]
Every coordinate is stored as a pair representing \(a+b\varphi\), and signs are decided exactly by comparing rational squares against \(5\).

For the standard regular icosahedron, the script verifies the exact edge graph, its twenty triangular facets, the six antipodal pairs, and all \(64\) antipodal transversals. Their numbers of wholly contained facets are distributed as
\[
0^{12},\quad 1^{20},\quad 4^{20},\quad 5^{12}.
\]
For the standard regular dodecahedron it verifies the exact edge graph, its twelve pentagonal facets, ten antipodal pairs, and all \(1024\) transversals, with distribution
\[
0^{740},\quad 1^{204},\quad 2^{60},\quad 3^{20}.
\]

For the ordinary dodecahedral number, all \(495\) quadruples of maximal five-facet transversal sets are checked and none covers the twenty icosahedral facets. Five explicit integer halfspace normals are then checked to cover all twenty facets.

The checker also confirms an explicit four-halfspace cover of the twelve dodecahedral facets, consistent with the known ordinary icosahedral value. No finite experiment is used to extrapolate an infinite statement: the only exhaustive steps concern finite Platonic incidence structures, and every case in those structures is enumerated.
