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

# Reproduction
Run `python3 verification.py` with a standard Python 3 interpreter. The script reconstructs each finite field, enumerates **all** unordered three-element shift sets, checks each additive cover by both direct set unions and bitwise masks, and partitions the resulting complete set into affine-square orbits. The expected orbit-size table is embedded as exact integer assertions, and a successful run ends in `VERIFY_OK`.

The finite case list is exhaustive because the mathematical argument in `RESULT.md` uses the standard Hasse bound to exclude all other odd prime-power orders. The checker does not reprove Hasse's theorem or establish literature priority, and it does not constitute an independent mathematical audit.
