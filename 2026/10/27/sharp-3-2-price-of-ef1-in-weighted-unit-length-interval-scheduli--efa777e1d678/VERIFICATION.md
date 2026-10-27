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

# Verification summary

The theorem rests on a general path-structure and weighted-orientation proof, not finite testing. The bundled standalone `check.py` uses only standard-library exact rational arithmetic. Running `python check.py` produced `PASS 10365 finite assertions (not an exhaustive proof)`. It independently enumerates bounded allocations, checks EF1 and feasibility, and compares welfare with brute-force optima.

The test corpus is finite, and therefore neither certifies all finite inputs nor establishes novelty. The approximation bound is specific to two machines, shared nonnegative item weights, and equal positive job lengths. Independent audit has not been performed.
