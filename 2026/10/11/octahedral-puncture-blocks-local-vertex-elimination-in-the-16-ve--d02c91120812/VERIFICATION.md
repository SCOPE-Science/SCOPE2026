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

`verify.py` reconstructs the published 90 tetrahedra and checks the exact finite premises used by the proof. It verifies \(f=(16,106,180,90)\); the complete sorted tetrahedron-incidence degree list; uniqueness of vertex \(16\) at degree \(8\); the eight triangular facets, six vertices, and twelve edges of its octahedral link; the three missing octahedral edges; their presence in the deletion; equality of the deletion boundary with the link; and the fact that every four-subset of the six link vertices contains an opposite pair.

The verifier does not recompute a presentation of the binary-icosahedral group. That part uses the published identification of the complex as the Poincaré homology sphere and the standard fact that removing an open 3-ball preserves the fundamental group. Likewise, integral acyclicity of the puncture follows by Mayer–Vietoris from the sourced integral homology-sphere identification rather than from a Smith-normal-form computation here.

Replay command: `python verify.py`.
