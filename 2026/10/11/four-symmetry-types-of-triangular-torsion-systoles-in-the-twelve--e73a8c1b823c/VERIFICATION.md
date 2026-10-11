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

`verify.py` embeds the complete \(48\)-facet presentation of the twelve-vertex complex and uses only the Python standard library.

It reconstructs
\[
f=(12,60,96,48),
\]
checks that the six missing graph edges form the antipodal matching, enumerates all \(160\) three-vertex cliques, and identifies exactly \(64\) nonfacial triangular cycles.

Exact bit-vector elimination over \(\mathbf F_2\) gives facial-boundary rank \(48\) in a graph cycle space of dimension \(49\). Every one of the \(64\) nonfacial triangles reduces to the unique nonzero class.

The complement graph forces every simplicial automorphism to permute the six antipodal pairs. The script therefore exhausts all \(6!\,2^6=46{,}080\) possible pair-preserving permutations, retains exactly \(24\) facet-preserving maps, and computes the four carrier orbits.

Exact successful output:

`VERIFY_OK f=12,60,96,48 missing_edges=6 H1_F2_dim=1 cliques3=160 facial3=96 essential3=64 aut=24 carrier_orbits=4,12,24,24 reps=159|1212|124|126 orbit_vertex_degrees=1,3,6,6 small_orbit_parallel=yes total_vertex_degree=16`

The integral interpretation uses the published homeomorphism \(K\cong\mathbb{RP}^3\), hence \(H_1(K;\mathbb Z)\cong\mathbb Z/2\), together with the universal coefficient theorem.
