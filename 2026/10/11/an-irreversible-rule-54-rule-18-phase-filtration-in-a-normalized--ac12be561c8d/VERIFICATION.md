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

# Reproduction of the exact stripe theorem

Run `python3 verify.py` from the directory containing this file. Only the Python standard library is required; the script contains independent implementations of the two-dimensional normalized field and the induced cyclic-word map. A successful run prints:

`VERIFY_OK assertions=7161 orbit_period=169 rule_regimes=(54,18,0)`

The checker tests all cyclic binary words for heights \(3\) through \(9\), four admissible boundary and interior threshold choices, independent full-field/stripe agreement at selected widths, forbidden triple production by Rule 18, all phases of a 169-state 13-row cycle and the small-height periodic-orbit regime condition. The actual 169-state finite assertion is checked exhaustively along its orbit, whereas the universal-in-height theorem is proved by exact algebra and a local combinatorial argument in `RESULT.md`. No global exhaustive cycle census at height \(13\) is asserted. Independent audit is not performed.
