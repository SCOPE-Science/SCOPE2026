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

# Reproduction and scientific bounds
Run `python VERIFY.py` using Python 3 standard library. It independently constructs a grounded weighted Laplacian and its rational inverse; each reconstructed projector row is compared with the exact analytical formula. Verified inputs: four community sizes and eight rational square roots of within/between conductance ratios. Output: `PASS exact rational weighted two-clique projection checks: 752`. The computation does not establish correctness outside the tested finite set. The manuscript proves the universal formula through the Laplacian decomposition and explicit norm optimization. No independent audit or validation was performed.
