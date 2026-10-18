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
# Reproducibility and limits

Run `python verify.py` using `requirements.txt` from the same directory. This constructs actual figure-eight adjacency matrices, finds the junction-invisible spectral projector by an independent numerical eigenspace calculation, and compares every local site weight and total rank to the closed formulas across many integer pairs. It also tests non-Hermitian sink evolution on selected small networks. A successful finite numerical check is not an infinite-family proof: the proof rests on the exact Dirichlet spectrum, the junction endpoint-coupling equation, and its roots-of-unity sum.

The theorem covers a homogeneous unweighted adjacency model with two cycles meeting at one vertex and a positive-rate one-way sink there. No claim is made about finite-time absorption, spatially displaced sinks, dephasing, flux, unequal bonds, or continuum-edge quantum graphs. The assessment is same-model only; no independent audit has been performed.
