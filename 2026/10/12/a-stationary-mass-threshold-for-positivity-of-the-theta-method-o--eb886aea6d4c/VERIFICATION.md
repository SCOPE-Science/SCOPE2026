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
# Verification

Run `python3 artifacts/check_cycle_theta.py` with the standard Python library. The checker constructs each generator and its \(\theta\)-step independently using rational inverse matrices; it compares exact columns, off-diagonal signs, diagonal formulas, and the scalar positivity condition. Its deterministic output is:

`VERIFY_OK 5346 exact rational transition matrices, 297 strict diagonal-resolvent comparisons, heterogeneous critical example`

This is finite confirmation, not an exhaustive proof over real rates, all dimensions, or all stepsizes. The proof in `RESULT.md` separately derives strict monotonicity, the unique threshold, all endpoint cases, and the asymptotic coefficient; no external solver or unprovided files are required. The equality and limiting assertions are mathematical deductions, not floating-point certificates. Independent validation has not been performed.
