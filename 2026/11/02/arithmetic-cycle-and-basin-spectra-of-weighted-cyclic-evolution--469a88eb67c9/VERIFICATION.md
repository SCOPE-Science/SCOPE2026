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

Execute `python3 verify.py` with Python 3.10 or later; no dependencies are needed. The program builds small prime and extension fields from explicit irreducible polynomials, enumerates every state for each chosen weight configuration, discovers cycle entry times by tracing successors, and independently checks the closed fixed-point/support formulas and inverse-image-tree predecessor counts. It prints `WEIGHTED_CYCLIC_EVOLUTION_DYNAMICS_OK` with the actual number of configurations and states on success.

The executed package check covered 928 weighted configurations, 354173 enumerated states, and all first 32 iterates in each configuration. These are finite corroborations only. The general proof is the algebraic argument in `RESULT.md`, which treats all finite fields, all positive dimensions, and all nonzero weights. This package does not contain or imply an independent audit.
