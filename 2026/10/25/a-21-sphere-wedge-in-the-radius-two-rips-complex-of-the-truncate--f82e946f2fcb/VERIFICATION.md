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

# Reproducible verification
Run `python3 check.py` in a directory containing `check.py`. The standalone checker reconstructs the icosahedron, obtains its 60-vertex truncation, and verifies every asserted finite numerical fact and every step of the 120 elementary collapses. No optional packages are required. Successful execution prints six PASS/RESULT lines.

The simple-connectivity proof is separate and uses the graph's spherical embedding and explicit triangular fillings of every pentagonal and hexagonal face. The application of Hurewicz and homological Whitehead requires the resulting two-complex to be connected and simply connected, which follows from the stated graph-to-Rips loop reduction and these fillings. It is not replaced by Smith normal forms or a finite random test.

Verified scope: one finite simplicial complex at exact radius two. No higher-radius persistence or integral symmetry representation has been checked. No independent audit is claimed.
