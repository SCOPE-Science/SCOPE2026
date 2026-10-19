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

The mathematical argument is in `RESULT.md`, with a separate analytical proof of the partition-function identity, monotonicity, stationary classification, Lyapunov dissipation, and square-root onset. The finite checks in `checker_published.py` reproduce the moment identity for several integer opinion widths, stationary equations for multiple noise values, dissipativity, an elementary exact three-opinion special case, and sampled numerical trajectories.

Run using Python 3 with NumPy and SciPy: `python checker_published.py`. Actual execution yielded `PASS 444 identity, stationary-phase, dissipation, and trajectory checks`. Finite floating-point consistency tests are not infinite proofs. Bibliographic comparisons may not exhaust unindexed work, and an independent scientific audit has not been carried out.
