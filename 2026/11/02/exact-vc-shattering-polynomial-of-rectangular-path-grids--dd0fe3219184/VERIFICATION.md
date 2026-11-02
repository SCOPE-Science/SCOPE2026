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

# Reproducible checks

Run `python3 grid_shattering_check.py` using the standard Python 3 library. The program performs independent shortest-path tests for convexity on five small grids, enumerates rectangle traces for every support of size at most four on ten grids through \(5\times5\), checks the geometric shattering criterion against those traces, checks the closed coefficient formulas and independently enumerates four-point supports through \(8\times8\).

Expected final output: `ALL_GRID_SHATTERING_CHECKS_PASS`. The final embedded script was extracted from the delivered JSONL and rerun successfully. Tests cover finite small instances only. The all-parameter formulas rely on the explicit proofs in `RESULT.md`; no theorem about online/Littlestone dimension, asymptotic rates for fixed thin widths, or broader graph families is certified by these checks.
