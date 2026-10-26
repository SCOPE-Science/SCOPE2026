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

# Verification procedure

Run `python3 verify_rook.py` with Python 3 and its standard library. The program independently tests chronological blue-only forcing, a simultaneous forcing implementation, and the structural forest/leaf/isolate criterion on all `2^(m*n)` white configurations for grid sizes (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (3,3), (3,4), (3,5), and (4,4). It calculates every minimum set, recomputes connected components under one-edge exchanges, checks the exact Stirling-number count, and confirms the thin crown line-graph isomorphism and all its adjacencies for sizes 4 through 12. The expected terminal marker is `VERIFY_OK`.

The all-parameter claims require the mathematical proof in RESULT.md. The finite searches are cross-checks, not an exhaustive check of all parameter pairs; no independent validation has been performed.
