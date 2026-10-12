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

# Reproducibility

Run `python3 verify.py` (Python 3, standard library only). Expected output:

`EXACT_CERTIFICATE_OK indices=2,3,5,40 apery_checked=2..141 high_cutoffs=11,15,71 max_F=258529`

The script computes exact Apéry minimal representatives using Dijkstra's algorithm, from which the Frobenius number and genus are calculated without relying on the general three-generator criterion. It also independently executes the latter criterion on each index and checks the analytic-boundary inequalities and hand-excluded cases.

The theorem for every positive integer index at least two follows from the written polynomial and modular arguments, not from 140 instances of computation. In particular, the upper bounds derived in RESULT.md eliminate all larger indices for each possible common divisor, so the finite set of residual tests is exhaustive.

No independent audit has been performed. Self-review verifies the stated proof and the checks only.
