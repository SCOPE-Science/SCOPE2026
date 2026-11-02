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

The included standalone `verify.py` computes factor-occurrence crossing masks **directly from each finite source word** for every factor of lengths one through the requested cutoff. For orders \(3\) through \(10\) (as applicable), it enumerates all unordered pairs of source positions and compares the exact global set of valid attractor pairs with the independently constructed local centered-context pair set. It also checks the all-order formula at these test orders and separately checks the four length-five occurrence counts through order \(14\).

The accompanying `verification_output.txt` records the actual results from executing `python verify.py`. The infinite formulas are justified by the symbolic occurrence decomposition and exact adjacent-pair recurrences in `RESULT.md`; enumerated finite cases alone are not treated as proof. The checks do not test all orders, independent publication priority, or other \(k\)-values.
