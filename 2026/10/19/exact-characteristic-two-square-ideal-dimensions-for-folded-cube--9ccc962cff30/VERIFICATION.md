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

The Python 3 standalone checker `verify.py` was executed against the packaged scientific formula on exactly nine graph dimensions, \(2\le d\le10\). It uses integer XOR rows for GF(2) adjacency matrices and pivot elimination. All nine checks passed. The general theorem is established by the normal-form and tensor-complex proof in RESULT.md, not by the finite tests. No independent audit was performed.
