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

The standalone verifier is `verify_dominance_multipartite.py` (Python 3, standard library only). It enumerates all faces by testing the dominating complements, constructs the claimed explicit matching, validates coverage and expected critical dimensions, topologically sorts the full Hasse orientation to check acyclicity, and computes independent reduced boundary ranks over the binary field. It tests nine explicit multipartite graphs, all of which pass.

The mathematical argument for the complete infinite family is the separate relative-cell homotopy proof in `RESULT.md`, not the finite test output. No integral Smith-normal-form calculation or external formal proof is asserted, because the integer homology and wedge homotopy types already follow from the geometric construction. The result has received self-review only; independent audit has not been performed.
