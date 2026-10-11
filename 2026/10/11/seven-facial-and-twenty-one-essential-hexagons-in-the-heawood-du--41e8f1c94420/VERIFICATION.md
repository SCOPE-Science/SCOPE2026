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

Run `python3 artifacts/verify.py`. The script uses only the Python standard library and reconstructs the triangulation from the fourteen published facets. It verifies:

- \(21\) edges and \(14\) triangular facets, with each edge in exactly two facets;
- rank \(13\) for the triangle cocycle equations and rank \(6\) for vertex coboundaries;
- exactly \(256\) cocycles and four cohomology cosets of size \(64\);
- zero-class enumerator \(1+7t^6+21t^{10}+35t^{12}\);
- identical nonzero-class enumerators \(7t^6+7t^8+21t^{10}+21t^{12}+8t^{14}\);
- a connected cubic bipartite dual graph with two parts of size \(7\) and the Fano incidence property;
- exactly \(28\) simple six-cycles, equal as edge supports to all weight-six cocycles;
- exactly seven trivial six-cycles, equal to the seven vertex coboundaries;
- closure of the two published generators to a facet-preserving group of order \(42\);
- cycle-support orbit sizes \(7\) and \(21\), with the essential orbit split \(7,7,7\) among the three nonzero classes.

Successful replay prints the exact summary stored in `artifacts/verification_output.txt`. The finite computation proves statements only for this fixed triangulation. The interpretation of nonzero dual-cycle class as essential uses standard mod-two Poincaré duality for a closed orientable surface.
