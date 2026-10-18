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

# Reproducing the finite Morse certificate

Run `python3 verify_plane_partitions.py` followed by `python3 verify_triangular_dual.py` with Python 3 and no third-party packages. Both programs are standalone. Their expected exact output is supplied in `plane_partitions_output.txt` and `triangular_dual_output.txt`.

The first program enumerates all monotone \(2\times2\) height arrays, converts them to labeled rhombi, builds all simplices, and applies the specified nine pivot pairings. It also checks the previously known \(2\times2\times1\) and \(2\times2\times2\) cases. The second program builds the \(32\)-triangle hexagonal region, finds adjacent triangle pairs, enumerates perfect matchings recursively without first using the plane partitions, and verifies exact equality with the plane-partition facet family. It then separately repeats the face enumeration and Morse certificate.

Both return \(50\) facets, \(41\) complex vertices, \(2,517,788\) faces including the empty face, and three critical nonempty simplices of dimensions \(0,4,4\). Exact bit-mask integers, rather than floating-point computations, certify every pairing and critical-cell count.

The proof that the stagewise matching is acyclic is mathematical and given in `RESULT.md`; numerical output alone would not establish acyclicity. The finite check does not assert any classification for larger honeycombs. Independent external mathematical audit has not been performed.
