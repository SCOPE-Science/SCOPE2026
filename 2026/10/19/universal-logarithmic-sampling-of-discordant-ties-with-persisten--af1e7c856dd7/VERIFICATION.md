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

Run `python3 verification/check.py` with Python 3.10+; it needs no third-party packages. The check simulates a three-edge weighted sampler with one receptive edge and two unreceptive edges with distinct decreasing factors, and confirms selected finite-time count and log-weight comparisons. It also simulates a known all-discount comparison regime and verifies an explicitly permanently mixed-receptivity three-agent opinion configuration.

The code was executed successfully from the delivered standalone source. The proof of the almost-sure limits is the geometric-tail/Borel–Cantelli and martingale argument in `RESULT.md`. Numerical paths cannot establish an infinite-time assertion or scientific originality. Independent audit has not been performed.
