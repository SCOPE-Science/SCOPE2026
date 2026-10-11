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

# Reproducible mathematical checks

Execute `python3 verify.py` in the directory containing this file, with the Python standard library only. The verifier rebuilds every candidate integer polar potential in 18 small parameter instances, checks polar extremum, tangent-facet count and sign profiles, and verifies the rational rank of the contact normals. It additionally enumerates all integer graph potentials for five small graphs and checks that the connected-tight-edge criterion reproduces the listed polar vertices.

Actual run result: `ALL_EXACT_CHECKS_PASSED cases=18 polar_vertices=126256 direct_facets=5`.

The general strict-activation argument, parity balancing, and contact-span dimension are written explicitly in `RESULT.md`; finite cases and code are corroborative, not exhaustive over all parameters. No external or independent audit has been conducted.
