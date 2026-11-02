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

# Reproducibility and scope

The proof is given in `RESULT.md`, with the up/down incidence commutator and the adjacency eigenvector propagation spelled out explicitly. The independent computations within `verify.py` are finite checks, not a replacement for that proof.

Execute `python verify.py` with Python 3 and NumPy installed. Expected summary: `PASS: 130 spectral restriction ranks, 10 direct modular Kalman ranks; dimensions 1 through 10 (spectral), 1 through 5 (Kalman); two exact prime fields.` The code builds the coordinate-selector sets, constructs Walsh character restrictions and adjacency matrices from their definitions, and computes exact ranks modulo 1000003 and 1000033. No prerecorded result tables are needed.

The result pertains only to the full continuous-time linear consensus system on unweighted undirected hypercubes, with independent scalar controls at a set of vertices. No independent audit has been performed. Historical-coverage risk is recorded separately in `REVIEW.md` and `AUDIT.json`.
