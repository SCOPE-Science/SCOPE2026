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

The calculations are exact integer computations over all rotation classes of order-five binary de Bruijn sequences, and the standalone checker uses only Python's standard library. Run `python verify.py cycles.csv`. The output is accepted only if both independent exhaustive cycle generators identify the same \(2048\) cycles, every cycle passes the de Bruijn factor test, two gcd methods agree for the cycle and its reversal, and independent linear-complexity algorithms agree. The exact ten-row marginal and sixteen-row reversal-pair tables, complementary symmetry, sharp reversal ratio, and every row of `cycles.csv` are then checked against independently regenerated values.

The checker does not prove any statement about larger-order de Bruijn cycles. The identified publication-priority risk from an inaccessible relevant 2012 full text is not resolved by numerical verification. No independent scientific audit has been conducted.
