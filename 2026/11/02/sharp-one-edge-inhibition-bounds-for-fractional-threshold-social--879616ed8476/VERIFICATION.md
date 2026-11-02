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

Run `python3 verify.py` with the standard Python 3 interpreter; no dependencies are needed.

The script implements irreversible synchronous adoption by exact rational comparisons. It exhaustively checks the claimed upper bounds for 128,360 graph/seed/edge/threshold instances covering every connected noncomplete labeled graph on three, four or five vertices, using eight fixed rational thresholds. It also tests 64 explicit extremal examples, at and beyond the cutoff graph order.

The universal statement is proved symbolically by the degree bound, the leaf-only high-threshold argument and the low-threshold gate construction in `RESULT.md`. Exhaustion over small graph orders cannot substitute for these arguments, and the program does not check social realism, stochastic modifications or priority in the literature.
