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

The mathematical proof invokes the published nonequivariant sphere theorem for directed path-free and path-missing complexes, and proves the new orbit-path lifting, fixed-coordinate PL equivalence, and signed orbit-face Lefschetz identities explicitly.

Run `python verify_path_orbits.py` in the same directory. The checker exhaustively enumerates 332 essential labeled acyclic directed graphs with up to six vertices under its documented bounded edge cutoff, verifies 405 automorphism actions and tests five subgroups of the small layered network. The expected final markers are `PATH_FREE_PATH_MISSING_FIXED_POINT_CHARACTERS_OK 405 332` and `LAYERED_NETWORK_SUBGROUP_FIXED_POINTS_OK`.

Finite verification cannot certify the all-size statement. The general theorem follows from its explicit combinatorial lemmas and the cited published sphere theorem; no equivariant homotopy equivalence to linear spheres, integral orbit-space classification, or independent human audit is claimed.
