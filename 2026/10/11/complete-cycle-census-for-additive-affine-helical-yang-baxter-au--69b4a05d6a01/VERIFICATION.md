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

## Method

The packaged `verify.py` uses exact binary-vector arithmetic only and no third-party dependencies. Execute `python3 verify.py` from the package directory. It tests source equation admissibility in all invertible affine rules for dimensions two and three, two-step formula and full cycle counts for every configuration at lattice lengths one to three (and length four in dimension two), and enumerates all dimension-four square-zero operators. It prints `VERIFY_OK 846906` after all assertions.

The proof in `RESULT.md` establishes generality for all positive dimensions and lattice lengths. The finite tests are independent diagnostics, not an exhaustive proof in unbounded sizes. The open-access arXiv preprint was examined in full; a later related manuscript and the full journal version remain uninspected due to access, leaving a literature-priority risk. No independent audit is represented or asserted.
