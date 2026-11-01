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

## Reproducible checks

Run `python3 verify.py` from the directory containing the two verification artifacts. The program uses only the Python 3.10+ standard library. It computes clique facets explicitly, performs literal stellar subdivision of each vertex-star facet, verifies every free pair by listing all strict cofaces, and checks equality of the resulting full face set with the midpoint subdivision. It also verifies equivariance of the pair orbits against every graph automorphism for the smaller examples and computes exact integer matrices for the exterior-power action.

Tested finite graphs: complete graphs of orders 4 through 7, cube, triangular prism, complete five-vertex graph with one missing edge, and Petersen graph. Complete group-action checks: \(S_4,S_5,S_6,S_7\) on the integral lattice, with full simplex-level orbit checks for \(S_4,S_5,S_6\). The saved verification output ends with `VERIFY_OK`.

**Unproved by computation alone:** Uniform correctness over infinitely many graphs and the general integral module theorem. These follow instead from the free-face classification and the elementary exterior-algebra proof given in `RESULT.md`. The code is finite corroboration, not infinite exhaustive evidence. Independent mathematical verification is not performed.
