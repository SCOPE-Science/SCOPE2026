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

Run `python3 verify.py` using Python 3 with only the standard library. The complete observed output is `verify_output.txt`; its final line is `CORONA_JORDAN_DOUBLING_VERIFIED`.

The code checks all integer partitions of dimensions one through eight (66 nilpotent Jordan models), ten path/cycle families at powers two through 64, and exhaustive labelled-state periodic-orbit counts on two small paths and two small cycles. The exhaustive state counts total 82,240. It constructs every graph and matrix afresh from explicit definitions and independently computes ranks via binary elimination, not from stored certificates.

The all-size Jordan and orbit formulas are proved algebraically in `RESULT.md`; finite computations cannot establish them for unbounded graph sizes. No nonnilpotent period-count formula and no independent external validation is asserted.
