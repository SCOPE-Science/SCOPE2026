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
Run `python3 verify_octahedron.py` and `python3 verify_cube.py` using Python 3.8 or later and no third-party packages. Both computations are deterministic, exact and exhaustive: the first runs over every permutation of six labels and then every labeled automorphism of the octahedral graph; the second runs over all 4096 orientations of twelve cube edges and checks all 254 nontrivial directed cuts for each one. The first prints `OCTAHEDRON_ACYCLIC_ORBITS_PASS`; the second prints `CUBE_DIRECTED_CUT_ORIENTATIONS_PASS`. Output agreement is a check of the finite theorem, not an independent human audit. The code does not verify the historical originality claim.
