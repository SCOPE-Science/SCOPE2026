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

# Exact finite-state checks

Run `python3 verify.py` with Python 3, no third-party packages required. This constructs the Rule 22 overlap relations directly from its complete local truth table, closes all right products from the identity, and checks the resulting 2375 Boolean relations. It checks that exactly two relations have first cyclic return at multiplier three and none at four, that a mixed output word cannot reach either exceptional relation, and that each all-one word has its predicted return. It also enumerates all 2046 binary cyclic words of lengths 1 through 10 and compares actual same-period preimages with the graph criterion.

These are exact integer operations. Exhaustive closure plus the four-vertex cycle bound, as explained in `RESULT.md`, proves all positive spatial periods. The 2046-word comparison is an independent finite cross-check, not an infinite extrapolation.

The check completed with:

`VERIFY_OK: 2375 relations exhaustively closed; exactly two triple-only states; no quadruple-only state; no mixed-word triple case; 2046 exact ring tests`

No independent mathematical audit or external verification is asserted.
