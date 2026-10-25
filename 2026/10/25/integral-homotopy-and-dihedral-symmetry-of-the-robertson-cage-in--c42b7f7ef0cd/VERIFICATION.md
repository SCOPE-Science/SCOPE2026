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

# Reproduction

With the installed version of `networkx` specified in `requirements.txt`, run `python verify_robertson.py`. The script uses Python integer masks and rational-free signed chain reductions, enumerates all independent sets and graph automorphisms, checks Hasse acyclicity explicitly, and reconstructs both cycle actions. A separate full simplicial mod-two boundary calculation checks ranks \(0,18,115,322,380,133,4\), in agreement with the integral Morse result. It checks the precise signed Morse differential, 25-term three-cycle, 56/98/56-term four-cycles, and full dihedral action matrices. No precomputed boundary logs, external graph data, remote downloads, or binary certificates are required.

# Verified scope and limits

All enumeration bounds are finite and exhaustive for the specified graph. The homotopy conclusion additionally uses standard discrete-Morse CW equivalence and the identification of attaching maps from three-sphere wedges by integral degrees. The code does not establish novelty or independent external validation.
