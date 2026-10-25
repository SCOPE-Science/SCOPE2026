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

# Exact verification

Run `python3 verify_bidirected_k33.py`. This is a self-contained standard-library program specifying the digraph and finite face predicate and reconstructing the complete discrete Morse certificate. It explicitly verifies the 714 face count, the 341 paired face-cover relations, global acyclicity of all 714 oriented Hasse vertices, each of four unique gradient cancellations, the 32 surviving critical cells, and the vanishing of all signed integral Morse boundaries.

The only topological input beyond the certificate is Forman's elementary discrete Morse theorem for a finite simplicial complex, followed by the Hurewicz isomorphism for the simply connected wedge of three-spheres. The verification certifies this particular six-vertex complex only. No external validation has been performed.
